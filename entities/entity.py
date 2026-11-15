#!/usr/bin/env python3
"""entity.py - procedural entity RECIPES: read, check, draw as text, and turn into Vibecode3D code.

    python3 -I entities/entity.py check RECIPE.txt...     check + top and side views
    python3 -I entities/entity.py code RECIPE.txt         print the LiveCode mesh function
    python3 -I entities/entity.py --help

A recipe is words and numbers (Spark writes them, the owner's rule: never scripts). The code is
written by this tool, the same calls the games use (MeshBox, MeshPrism, MeshPyramid, MeshSphere,
MeshLathe, MeshLoft, Mesh.Transform, Mesh.Merge, Mesh.AddVertex / AddLine / AddFace).

RECIPE FORMAT
    ENTITY: Sail Boat
    GAME: Simple Test2 harbour
    COLOUR: 255,255,255
    SIZE: 40,95,110            x (width), y (height), z (length) of the whole thing
    SYMMETRIC: yes             mirror image left/right (x -> -x)
    BASE: floats               ground (lowest point at y 0) | floats | flies
    PARTS:
    name | shape | sizes | at x,y,z | turn rx,ry,rz | what it is for
    hull | loft | 0; 0,60; 20,25; 20,-50; -20,-50; -20,25 / 25; 0,30; 10,12.5; 10,-25; -10,-25; -10,12.5 | 0,0,0 | 0,0,0 | the hull
    cabin | box | 24,14,30 | 0,-7,-15 | 0,0,0 | the cabin
    mast | line | 0,0,10; 0,-70,10 | 0,0,0 | 0,0,0 | holds the sail

  The engine's axes: x right, y DOWN (up is -y: a mast top is at y -70), z forward (the front
  points to +z). Turns are degrees, applied Z then Y then X (Mesh.Transform's order).
  Shapes and their sizes:
    box      w,h,d                         centred on its point
    prism    sides,radius,height           a cylinder standing on y, centred
    pyramid  sides,radius,height           base at +height/2 (bottom), tip at -height/2 (top)
    sphere   radius,rings,sides
    lathe    sides; r,y; r,y; ...          a profile spun round y, listed top to bottom
    loft     yA; x,z; x,z... / yB; x,z...  two outlines (seen from above, same count) joined
    line     x,y,z; x,y,z                  a wire
    tri      x,y,z; x,y,z; x,y,z           one flat triangle (a sail, a fin)

CHECKS (each a line in the report; "FAIL" lines make the exit code 1)
  parse     every part line has 6 fields and a known shape with the right sizes
  size      the whole thing's x, y, z extents within 30% of SIZE
  joined    every part touches the others (bounding boxes within 2% of the size): nothing floats loose
  base      ground: lowest point at y 0 (within 3% of the height); floats/flies: just reported
  mirror    SYMMETRIC yes: every vertex has a mirror partner at -x
  edges     the edge count (as Mesh.Define counts them) is at most 160 (vector speed)
  front     the front half (+z) and back half differ in shape, reported for a person to judge
"""
import math, re, sys

SHAPES = {'box': 3, 'prism': 3, 'pyramid': 3, 'sphere': 3, 'lathe': None, 'loft': None, 'line': None, 'tri': None}
EDGE_BUDGET = 160


class Mesh:
    def __init__(self):
        self.v, self.faces, self.lines = [], [], []

    def add(self, x, y, z):
        self.v.append((float(x), float(y), float(z)))
        return len(self.v)                     # 1-based, as the engine

    def merge(self, other):
        off = len(self.v)
        self.v += other.v
        self.faces += [[i + off for i in f] for f in other.faces]
        self.lines += [(a + off, b + off) for a, b in other.lines]

    def edges(self):
        seen = set()
        for f in self.faces:
            for k in range(len(f)):
                a, b = f[k], f[(k + 1) % len(f)]
                if a != b:
                    seen.add((min(a, b), max(a, b)))
        for a, b in self.lines:
            if a != b:
                seen.add((min(a, b), max(a, b)))
        return sorted(seen)


# ---------------------------------------------------------------- the engine's generators, in Python
def ring(start, n, rev):
    return [start + n - k for k in range(1, n + 1)] if rev else [start + k - 1 for k in range(1, n + 1)]


def box(w, h, d):
    m, hw, hh, hd = Mesh(), w / 2, h / 2, d / 2
    for x, y, z in [(-hw, -hh, -hd), (hw, -hh, -hd), (hw, hh, -hd), (-hw, hh, -hd),
                    (-hw, -hh, hd), (hw, -hh, hd), (hw, hh, hd), (-hw, hh, hd)]:
        m.add(x, y, z)
    m.faces = [[1, 2, 3, 4], [5, 8, 7, 6], [1, 5, 6, 2], [4, 3, 7, 8], [1, 4, 8, 5], [2, 6, 7, 3]]
    return m


def prism(sides, r, h):
    sides, m = max(3, int(sides)), Mesh()
    for y in (-h / 2, h / 2):
        for k in range(sides):
            a = 2 * math.pi * k / sides
            m.add(r * math.cos(a), y, r * math.sin(a))
    for k in range(1, sides + 1):
        k2 = k % sides + 1
        m.faces.append([k, k2, sides + k2, sides + k])
    m.faces += [ring(1, sides, False), ring(sides + 1, sides, True)]
    return m


def pyramid(sides, r, h):
    sides, m = max(3, int(sides)), Mesh()
    for k in range(sides):
        a = 2 * math.pi * k / sides
        m.add(r * math.cos(a), h / 2, r * math.sin(a))
    apex = m.add(0, -h / 2, 0)
    for k in range(1, sides + 1):
        m.faces.append([k, k % sides + 1, apex])
    m.faces.append(ring(1, sides, True))
    return m


def lathe(profile, sides):
    sides, m = max(3, int(sides)), Mesh()
    start, size = [], []
    for r, y in profile:
        start.append(len(m.v) + 1)
        if abs(r) < 1e-4:
            m.add(0, y, 0)
            size.append(1)
        else:
            for k in range(sides):
                a = 2 * math.pi * k / sides
                m.add(r * math.cos(a), y, r * math.sin(a))
            size.append(sides)
    for p in range(len(profile) - 1):
        a0, b0 = start[p], start[p + 1]
        for k in range(1, sides + 1):
            k2 = k % sides + 1
            if size[p] == 1 and size[p + 1] == 1:
                m.lines.append((a0, b0))
                break
            if size[p] == 1:
                m.faces.append([a0, b0 + k - 1, b0 + k2 - 1])
            elif size[p + 1] == 1:
                m.faces.append([a0 + k - 1, a0 + k2 - 1, b0])
            else:
                m.faces.append([a0 + k - 1, a0 + k2 - 1, b0 + k2 - 1, b0 + k - 1])
    if profile:
        if size[0] > 1:
            m.faces.append(ring(start[0], sides, False))
        if size[-1] > 1:
            m.faces.append(ring(start[-1], sides, True))
    return m


def sphere(r, rings, sides):
    rings = max(2, int(rings))
    prof = []
    for k in range(rings + 1):
        a = math.pi * k / rings
        rr = r * math.sin(a)
        prof.append((0 if abs(rr) < 1e-4 else rr, -r * math.cos(a)))
    return lathe(prof, sides)


def loft(ya, a, yb, b):
    n, m = min(len(a), len(b)), Mesh()
    for x, z in a[:n]:
        m.add(x, ya, z)
    for x, z in b[:n]:
        m.add(x, yb, z)
    for k in range(1, n + 1):
        k2 = k % n + 1
        m.faces.append([k, k2, n + k2, n + k])
    if n > 2:
        m.faces += [ring(1, n, False), ring(n + 1, n, True)]
    return m


def transform(m, rx, ry, rz, tx, ty, tz):
    """Mesh.Transform: Mat3.RotZYX = Rx * Ry * Rz (radians), then move"""
    cx, sx, cy, sy, cz, sz = math.cos(rx), math.sin(rx), math.cos(ry), math.sin(ry), math.cos(rz), math.sin(rz)
    RZ = [[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]]
    RY = [[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]]
    RX = [[1, 0, 0], [0, cx, -sx], [0, sx, cx]]
    mul = lambda A, B: [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    R = mul(RX, mul(RY, RZ))
    m.v = [tuple(sum(R[i][k] * p[k] for k in range(3)) + t for i, t in enumerate((tx, ty, tz))) for p in m.v]
    return m


# ---------------------------------------------------------------- recipes
def nums(text):
    return [float(x) for x in re.findall(r'-?\d+(?:\.\d+)?', text)]


def points(text, per):
    out = []
    for chunk in text.split(';'):
        v = nums(chunk)
        if v:
            if len(v) != per:
                raise ValueError('"%s" should have %d numbers' % (chunk.strip(), per))
            out.append(tuple(v))
    return out


def parse(text):
    head, parts, errors, in_parts = {}, [], [], False
    for raw in text.replace('\r', '\n').split('\n'):
        line = raw.strip().strip('`')
        if not line or line.startswith('#'):
            continue
        if line.upper().startswith('PARTS'):
            in_parts = True
            continue
        if not in_parts:
            m = re.match(r'^([A-Z]+):\s*(.*)$', line)
            if m:
                head[m.group(1)] = m.group(2).strip()
            continue
        f = [x.strip() for x in line.lstrip('-* ').split('|')]
        if f and f[0].lower() == 'name':                     # the column header line
            continue
        if len(f) < 5:
            errors.append('part line has %d fields, not 6: %s' % (len(f), line[:60]))
            continue
        name, shape, sizes, at, turn = f[:5]
        shape = shape.lower()
        if shape not in SHAPES:
            errors.append('%s: unknown shape "%s"' % (name, shape))
            continue
        try:
            mesh = build(shape, sizes)
            a = nums(at) or [0, 0, 0]
            t = nums(turn) or [0, 0, 0]
            if len(a) != 3 or len(t) != 3:
                raise ValueError('"at" and "turn" need 3 numbers each')
        except (ValueError, IndexError) as e:
            errors.append('%s (%s): %s' % (name, shape, e))
            continue
        parts.append(dict(name=name, shape=shape, sizes=sizes, at=a, turn=t,
                          role=f[5] if len(f) > 5 else '', mesh=mesh))
    return head, parts, errors


def build(shape, sizes):
    v = nums(sizes)
    if shape in ('box', 'prism', 'pyramid', 'sphere'):
        if len(v) != 3:
            raise ValueError('%s needs 3 numbers, got %d' % (shape, len(v)))
        return {'box': box, 'prism': prism, 'pyramid': pyramid, 'sphere': sphere}[shape](*v)
    if shape == 'lathe':
        sides, rest = sizes.split(';', 1)
        prof = points(rest, 2)
        if len(prof) < 2:
            raise ValueError('a lathe needs at least 2 profile points')
        return lathe(prof, nums(sides)[0])
    if shape == 'loft':
        A, B = sizes.split('/')
        ya, ra = A.split(';', 1)
        yb, rb = B.split(';', 1)
        pa, pb = points(ra, 2), points(rb, 2)
        if len(pa) != len(pb) or len(pa) < 2:
            raise ValueError('loft outlines need the same count of x,z points (%d and %d)' % (len(pa), len(pb)))
        return loft(nums(ya)[0], pa, nums(yb)[0], pb)
    if shape == 'line':
        p = points(sizes, 3)
        if len(p) != 2:
            raise ValueError('a line needs 2 points')
        m = Mesh()
        m.lines.append((m.add(*p[0]), m.add(*p[1])))
        return m
    if shape == 'tri':
        p = points(sizes, 3)
        if len(p) != 3:
            raise ValueError('a tri needs 3 points')
        m = Mesh()
        m.faces.append([m.add(*q) for q in p])
        return m
    raise ValueError(shape)


def place(part):
    m = Mesh()
    m.merge(part['mesh'])
    rx, ry, rz = (math.radians(x) for x in part['turn'])
    return transform(m, rx, ry, rz, *part['at'])


def bounds(vs):
    return [min(p[i] for p in vs) for i in range(3)], [max(p[i] for p in vs) for i in range(3)]


def check(text):
    """(report lines, ok, whole mesh)"""
    head, parts, errors = parse(text)
    rep = ['parse    %s' % ('ok: %d parts' % len(parts) if not errors else 'FAIL: ' + '; '.join(errors))]
    if not parts:
        return rep + ['FAIL     no parts'], False, Mesh()
    placed = [place(p) for p in parts]
    whole = Mesh()
    for m in placed:
        whole.merge(m)
    lo, hi = bounds(whole.v)
    ext = [hi[i] - lo[i] for i in range(3)]
    ok = not errors
    want = nums(head.get('SIZE', ''))
    if len(want) == 3:
        off = [abs(ext[i] - want[i]) / max(want[i], 1) for i in range(3)]
        bad = max(off) > 0.30
        ok &= not bad
        rep.append('size     %s: is %.0f x %.0f x %.0f, SIZE says %.0f x %.0f x %.0f' %
                   ('FAIL' if bad else 'ok', ext[0], ext[1], ext[2], *want))
    else:
        rep.append('size     (no SIZE line) is %.0f x %.0f x %.0f' % tuple(ext))
    # joined: bounding boxes touching, union by flood
    tol = 0.02 * max(ext)
    boxes = [bounds(m.v) for m in placed]
    touch = lambda a, b: all(a[0][i] - tol <= b[1][i] and b[0][i] - tol <= a[1][i] for i in range(3))
    seen, todo = {0}, [0]
    while todo:
        i = todo.pop()
        for j in range(len(placed)):
            if j not in seen and touch(boxes[i], boxes[j]):
                seen.add(j)
                todo.append(j)
    loose = [parts[j]['name'] for j in range(len(parts)) if j not in seen]
    ok &= not loose
    rep.append('joined   %s' % ('ok' if not loose else 'FAIL: not touching the rest: ' + ', '.join(loose)))
    base = head.get('BASE', 'ground').split()[0].lower() if head.get('BASE') else 'ground'
    lowest = hi[1]                                            # y down: the lowest point has the largest y
    if base == 'ground':
        bad = abs(lowest) > 0.03 * max(ext[1], 1)
        ok &= not bad
        rep.append('base     %s: lowest point at y %.1f (ground means 0)' % ('FAIL' if bad else 'ok', lowest))
    else:
        rep.append('base     %s: lowest point at y %.1f' % (base, lowest))
    if head.get('SYMMETRIC', '').lower().startswith('y'):
        keys = {(round(x, 1), round(y, 1), round(z, 1)) for x, y, z in whole.v}
        odd = [p for p in keys if (round(-p[0], 1) or 0.0, p[1], p[2]) not in keys and (round(-p[0], 1), p[1], p[2]) not in keys]
        ok &= not odd
        rep.append('mirror   %s' % ('ok' if not odd else 'FAIL: %d vertices have no mirror partner at -x, e.g. %s' % (len(odd), odd[0])))
    ne = len(whole.edges())
    ok &= ne <= EDGE_BUDGET
    rep.append('edges    %s: %d (budget %d)' % ('ok' if ne <= EDGE_BUDGET else 'FAIL', ne, EDGE_BUDGET))
    mid = (lo[2] + hi[2]) / 2
    front = [p for p in whole.v if p[2] > mid]
    back = [p for p in whole.v if p[2] <= mid]
    fw = (max(abs(p[0]) for p in front) if front else 0)
    bw = (max(abs(p[0]) for p in back) if back else 0)
    rep.append('front    (judge) front half %d vertices, widest %.0f; back half %d, widest %.0f' % (len(front), fw, len(back), bw))
    return rep, ok, whole


def view(mesh, axes, w=48, h=20, title=''):
    """the edges drawn in characters; axes (0, 2) = top view (x right, z up the page),
    (2, 1) = side view (z right, y down the page: up is up)"""
    vs = mesh.v
    if not vs:
        return ''
    lo, hi = bounds(vs)
    a, b = axes
    sa, sb = max(hi[a] - lo[a], 1e-6), max(hi[b] - lo[b], 1e-6)
    s = min((w - 1) / sa, (h - 1) / sb * 2.0)          # characters are about twice as tall as wide
    W, H = int(sa * s) + 1, int(sb * s / 2.0) + 1
    grid = [[' '] * W for _ in range(H)]
    for i, j in mesh.edges():
        p, q = vs[i - 1], vs[j - 1]
        n = max(2, int(max(abs(p[a] - q[a]) * s, abs(p[b] - q[b]) * s / 2.0)) + 1)
        for k in range(n + 1):
            t = k / n
            x = (p[a] + (q[a] - p[a]) * t - lo[a]) * s
            y = (p[b] + (q[b] - p[b]) * t - lo[b]) * s / 2.0
            c, r = int(round(x)), int(round(y))
            if b == 2:                                     # top view: +z (front) at the top of the page
                r = H - 1 - r
            if 0 <= r < H and 0 <= c < W:
                grid[r][c] = '#'
    return '\n'.join([title] + [''.join(row).rstrip() for row in grid])


def lc_name(text):
    return ''.join(w[:1].upper() + w[1:] for w in re.findall(r'[A-Za-z0-9]+', text)) or 'Thing'


def fmt(x):
    return ('%.3f' % x).rstrip('0').rstrip('.') if x != int(x) else str(int(x))


def code(text, prefix='Ent'):
    """the LiveCode function that builds the recipe's mesh (Vibecode3D calls only)"""
    head, parts, errors = parse(text)
    if errors:
        raise ValueError('; '.join(errors))
    fname = '%s.%sMesh' % (prefix, lc_name(head.get('ENTITY', 'Thing')))
    out = ['## %s (%s): generated by LIB_SPARK/entities/entity.py from a recipe; edit the recipe, not this.'
           % (head.get('ENTITY', ''), head.get('GAME', '')),
           '## Front +Z, up -Y. Colour %s.' % head.get('COLOUR', ''),
           'function %s' % fname, '   local tM, a, b, c', '   put Mesh.New() into tM']
    for p in parts:
        sh, sz = p['shape'], p['sizes']
        out.append('   -- %s: %s' % (p['name'], p['role']))
        if sh in ('line', 'tri'):
            pts = points(sz, 3)
            # move and turn the points here (the engine has no transform for loose vertices)
            m = place(p)
            names = ['a', 'b', 'c'][:len(pts)]
            for n, q in zip(names, m.v):
                out.append('   Mesh.AddVertex tM, %s, %s, %s' % tuple(fmt(round(x, 3)) for x in q))
                out.append('   put the result into %s' % n)
            out.append('   Mesh.AddLine tM, a, b' if sh == 'line' else '   Mesh.AddFace tM, a && b && c')
            continue
        v = nums(sz)
        if sh == 'box':
            call = 'MeshBox(%s, %s, %s)' % tuple(fmt(x) for x in v)
        elif sh in ('prism', 'pyramid'):
            call = 'Mesh%s(%d, %s, %s)' % (sh.capitalize(), int(v[0]), fmt(v[1]), fmt(v[2]))
        elif sh == 'sphere':
            call = 'MeshSphere(%s, %d, %d)' % (fmt(v[0]), int(v[1]), int(v[2]))
        elif sh == 'lathe':
            sides, rest = sz.split(';', 1)
            call = 'MeshLathe("%s", %d)' % ('|'.join('%s,%s' % (fmt(r), fmt(y)) for r, y in points(rest, 2)), int(nums(sides)[0]))
        else:   # loft
            A, B = sz.split('/')
            ya, ra = A.split(';', 1)
            yb, rb = B.split(';', 1)
            ol = lambda pts: '|'.join('%s,%s' % (fmt(x), fmt(z)) for x, z in pts)
            call = 'MeshLoft("%s", %s, "%s", %s)' % (ol(points(ra, 2)), fmt(nums(ya)[0]), ol(points(rb, 2)), fmt(nums(yb)[0]))
        rx, ry, rz = (math.radians(x) for x in p['turn'])
        if any(p['turn']) or any(p['at']):
            call = 'Mesh.Transform(%s, %s, %s, %s, %s, %s, %s, 1)' % (call, fmt(round(rx, 5)), fmt(round(ry, 5)), fmt(round(rz, 5)),
                                                                     *(fmt(x) for x in p['at']))
        out.append('   put Mesh.Merge(tM, %s) into tM' % call)
    out += ['   return tM', 'end %s' % fname]
    return '\n'.join(out) + '\n', fname


def main(argv):
    if not argv or argv[0] in ('-h', '--help'):
        print(__doc__)
        return 0
    cmd, files = argv[0], argv[1:]
    bad = 0
    for f in files:
        text = open(f, encoding='utf-8', errors='replace').read()
        if cmd == 'code':
            print(code(text)[0])
            continue
        rep, ok, whole = check(text)
        bad += not ok
        print('== %s: %s' % (f, 'OK' if ok else 'FAULTS'))
        print('\n'.join('   ' + r for r in rep))
        print(view(whole, (0, 2), title='   top (front up the page)'))
        print(view(whole, (2, 1), title='   side (front to the right)'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

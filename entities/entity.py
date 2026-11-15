#!/usr/bin/env python3
"""entity.py - procedural entity RECIPES: read, check, draw as text, and turn into Vibecode3D code.

    python3 -I entities/entity.py check RECIPE.txt...     check + top and side views
    python3 -I entities/entity.py code RECIPE.txt         print the LiveCode mesh function
    python3 -I entities/entity.py --help

A recipe is words and numbers (Spark writes them, the owner's rule: never scripts). The code is
written by this tool, the same calls the games use (MeshBox, MeshPrism, MeshPyramid, MeshSphere,
MeshLathe, MeshLoft, Mesh.Transform, Mesh.Merge, Mesh.AddVertex / AddLine / AddFace).

RECIPE FORMAT (y is HEIGHT ABOVE THE GROUND in a recipe; the tool turns it into the engine's
y-down when it writes code, so Spark never has to think upside down)
    ENTITY: Sail Boat
    GAME: Simple Test2 harbour
    COLOUR: 255,255,255
    SIZE: 40,95,110            x (width), y (height), z (length) of the whole thing
    SYMMETRIC: yes             mirror image left/right (x -> -x)
    BASE: floats               ground (the tool sets its lowest point on y 0) | floats | flies
    RELATIONS: cabin on top of hull; sail above hull       optional, checked
    PARTS:
    name | shape | sizes | at x,y,z | turn rx,ry,rz | what it is for
    hull | loft | 0; 0,60; 20,25; 20,-50; -20,-50; -20,25 / -25; 0,30; 10,12.5; 10,-25; -10,-25; -10,12.5 | 0,0,0 | 0,0,0 | the hull
    cabin | box | 24,14,30 | 0,7,-15 | 0,0,0 | the cabin
    mast | line | 0,0,10; 0,70,10 | 0,0,0 | 0,0,0 | holds the sail

  Axes in a recipe: x right, y UP, z forward (the front points to +z). Turns in degrees, applied
  Z then Y then X (Mesh.Transform's order). The engine's y points down: code() negates y and the
  x and z turns (a mirror in y), so the generated calls match a hand-written engine mesh.
  Shapes and their sizes:
    box      w,h,d                         centred on its point
    prism    sides,radius,height           a cylinder standing upright, centred
    pyramid  sides,radius,height           base at the bottom, tip at the top
    sphere   radius,rings,sides
    lathe    sides; r,y; r,y; ...          a profile spun round the upright axis, top to bottom
    loft     yA; x,z; x,z... / yB; x,z...  two outlines (seen from above, same count) joined
    line     x,y,z; x,y,z                  a wire
    tri      x,y,z; x,y,z; x,y,z           one flat triangle (a sail, a fin)

CHECKS (each a line in the report; "FAIL" lines make the exit code 1)
  parse     the LAST complete recipe in the answer is read (small models think aloud and
            rewrite); lines without "|" between part lines are skipped; every part line has
            6 fields and a known shape with the right sizes
  size      the whole thing's width, height, length within 30% of SIZE
  joined    every part touches the others (bounding boxes within 2% of the size)
  base      ground: the tool lowers or raises the whole thing onto y 0 and says by how much
  relate    each RELATIONS item holds ("a on top of b", "a above b", "a below b", "a inside b")
  mirror    SYMMETRIC yes: every corner has a twin at -x
  edges     the edge count (as Mesh.Define counts them) is at most 160 (vector speed)
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


def last_recipe(text):
    """the last complete recipe in an answer: small models sometimes think aloud ("Wait, ...")
    and write the recipe again; the last one is their correction"""
    lines = text.replace('\r', '\n').replace('```', '').split('\n')
    starts = [i for i, l in enumerate(lines) if l.strip().upper().startswith('ENTITY:')]
    for s in reversed(starts):
        chunk = lines[s:]
        if any(l.strip().upper().startswith('PARTS') for l in chunk) and any('|' in l for l in chunk):
            return '\n'.join(chunk)
    return '\n'.join(lines[starts[-1]:]) if starts else text


def parse(text):
    """(head, parts, errors). Recipe coordinates: y = height ABOVE the ground. Each part also
    gets its engine form (y down: y, x-turn and z-turn negated), built as the engine builds it."""
    head, parts, errors, in_parts = {}, [], [], False
    for raw in last_recipe(text).split('\n'):
        line = raw.strip().strip('`')
        if not line or line.startswith('#'):
            continue
        if line.upper().startswith('PARTS'):
            in_parts = True
            continue
        m = re.match(r'^([A-Z]+):\s*(.*)$', line)
        if m and (not in_parts or '|' not in line):
            head[m.group(1)] = m.group(2).strip()
            continue
        if not in_parts or '|' not in line:            # musing between part lines: not a part
            continue
        f = [x.strip() for x in line.lstrip('-* ').split('|')]
        if f and f[0].lower() == 'name':                # the column header line
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
            a = nums(at) or [0, 0, 0]
            t = nums(turn) or [0, 0, 0]
            if len(a) != 3 or len(t) != 3:
                raise ValueError('"at" and "turn" need 3 numbers each')
            eng = engine_form(shape, sizes)
            mesh = build(shape, eng)
        except (ValueError, IndexError) as e:
            errors.append('%s (%s): %s' % (name, shape, e))
            continue
        parts.append(dict(name=name, shape=shape, sizes=sizes, eng=eng, mesh=mesh,
                          at=(a[0], -a[1], a[2]), turn=(-t[0], t[1], -t[2]),
                          role=f[5] if len(f) > 5 else ''))
    return head, parts, errors


def engine_form(shape, sizes):
    """the shape's numbers in engine terms (y down)"""
    v = nums(sizes)
    if shape in ('box', 'prism', 'pyramid', 'sphere'):
        if len(v) != 3:
            raise ValueError('%s needs 3 numbers, got %d' % (shape, len(v)))
        return v                                  # all symmetric in y, and the pyramid's tip is up in both
    if shape == 'lathe':
        sides, rest = sizes.split(';', 1)
        prof = points(rest, 2)
        if len(prof) < 2:
            raise ValueError('a lathe needs at least 2 profile points')
        return [nums(sides)[0], [(r, -y) for r, y in prof]]
    if shape == 'loft':
        A, B = sizes.split('/')
        ya, ra = A.split(';', 1)
        yb, rb = B.split(';', 1)
        pa, pb = points(ra, 2), points(rb, 2)
        if len(pa) != len(pb) or len(pa) < 2:
            raise ValueError('loft outlines need the same count of x,z points (%d and %d)' % (len(pa), len(pb)))
        return [-nums(ya)[0], pa, -nums(yb)[0], pb]
    p = points(sizes, 3)
    if len(p) != (2 if shape == 'line' else 3):
        raise ValueError('a %s needs %d points' % (shape, 2 if shape == 'line' else 3))
    return [(x, -y, z) for x, y, z in p]


def build(shape, e):
    if shape in ('box', 'prism', 'pyramid', 'sphere'):
        return {'box': box, 'prism': prism, 'pyramid': pyramid, 'sphere': sphere}[shape](*e)
    if shape == 'lathe':
        return lathe(e[1], e[0])
    if shape == 'loft':
        return loft(*e)
    m = Mesh()
    ids = [m.add(*q) for q in e]
    if shape == 'line':
        m.lines.append(tuple(ids))
    else:
        m.faces.append(ids)
    return m


def place(part, settle=0.0):
    m = Mesh()
    m.merge(part['mesh'])
    rx, ry, rz = (math.radians(x) for x in part['turn'])
    x, y, z = part['at']
    return transform(m, rx, ry, rz, x, y + settle, z)


def bounds(vs):
    return [min(p[i] for p in vs) for i in range(3)], [max(p[i] for p in vs) for i in range(3)]


def settle_of(head, parts):
    """ground objects: how far the whole thing moves (engine y) so its lowest point is on y 0"""
    if (head.get('BASE', 'ground').split() or ['ground'])[0].lower() != 'ground' or not parts:
        return 0.0
    hi = max(max(p[1] for p in place(q).v) for q in parts)
    return -hi


REL = re.compile(r'^\s*([\w-]+)\s+(on top of|above|below|under|inside|on)\s+([\w-]+)\s*$', re.I)


def check(text):
    """(report lines, ok, whole mesh in engine terms, settled)"""
    head, parts, errors = parse(text)
    rep = ['parse    %s' % ('ok: %d parts' % len(parts) if not errors else 'FAIL: ' + '; '.join(errors))]
    if not parts:
        return rep + ['FAIL     no parts'], False, Mesh()
    settle = settle_of(head, parts)
    placed = [place(p, settle) for p in parts]
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
        rep.append('size     %s: is %.0f x %.0f x %.0f (width, height, length), SIZE says %.0f x %.0f x %.0f' %
                   ('FAIL' if bad else 'ok', ext[0], ext[1], ext[2], *want))
    else:
        rep.append('size     (no SIZE line) is %.0f x %.0f x %.0f' % tuple(ext))
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
    base = (head.get('BASE', 'ground').split() or ['ground'])[0].lower()
    if base == 'ground':
        rep.append('base     ok: ground; %s' % ('stands on y 0 as written' if abs(settle) < 0.05 else
                                              'moved %s by %.1f so it stands on y 0' % ('down' if settle > 0 else 'up', abs(settle))))
    else:
        rep.append('base     %s: lowest point %.1f above the ground' % (base, -hi[1]))
    # relations, in height above the ground: up = -engine y
    top = {p['name'].lower(): -boxes[k][0][1] for k, p in enumerate(parts)}      # highest point
    bot = {p['name'].lower(): -boxes[k][1][1] for k, p in enumerate(parts)}      # lowest point
    rels = [r for r in re.split(r'[;,]', head.get('RELATIONS', '')) if r.strip()]
    rel_faults = []
    htol = 0.05 * max(ext[1], 1)
    for r in rels:
        m = REL.match(r)
        if not m:
            rel_faults.append('cannot read "%s"' % r.strip())
            continue
        a, how, b = m.group(1).lower(), m.group(2).lower(), m.group(3).lower()
        if a not in top or b not in top:
            rel_faults.append('"%s": no part called %s' % (r.strip(), a if a not in top else b))
            continue
        if how in ('on top of', 'on'):
            good = abs(bot[a] - top[b]) <= htol
            why = '%s starts at height %.0f, %s ends at %.0f' % (a, bot[a], b, top[b])
        elif how == 'above':
            good = bot[a] >= top[b] - htol
            why = '%s starts at %.0f, %s reaches %.0f' % (a, bot[a], b, top[b])
        elif how in ('below', 'under'):
            good = top[a] <= bot[b] + htol
            why = '%s reaches %.0f, %s starts at %.0f' % (a, top[a], b, bot[b])
        else:   # inside
            ka, kb = [p['name'].lower() for p in parts].index(a), [p['name'].lower() for p in parts].index(b)
            good = all(boxes[kb][0][i] - tol <= boxes[ka][0][i] and boxes[ka][1][i] <= boxes[kb][1][i] + tol for i in range(3))
            why = '%s is not within %s' % (a, b)
        if not good:
            rel_faults.append('"%s" is not true: %s' % (r.strip(), why))
    if rels:
        ok &= not rel_faults
        rep.append('relate   %s' % ('ok: %d relations hold' % len(rels) if not rel_faults else 'FAIL: ' + '; '.join(rel_faults)))
    else:
        rep.append('relate   (no RELATIONS line)')
    if head.get('SYMMETRIC', '').lower().startswith('y'):
        keys = {(round(x, 1) + 0.0, round(y, 1) + 0.0, round(z, 1) + 0.0) for x, y, z in whole.v}
        odd = [p for p in keys if (round(-p[0], 1) + 0.0, p[1], p[2]) not in keys]
        ok &= not odd
        rep.append('mirror   %s' % ('ok' if not odd else 'FAIL: %d corners have no twin on the other side (x %.1f has none at x %.1f)'
                                    % (len(odd), odd[0][0], -odd[0][0])))
    ne = len(whole.edges())
    ok &= ne <= EDGE_BUDGET
    rep.append('edges    %s: %d (budget %d)' % ('ok' if ne <= EDGE_BUDGET else 'FAIL', ne, EDGE_BUDGET))
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
    x = round(float(x), 4) + 0.0
    return ('%.4f' % x).rstrip('0').rstrip('.') if x != int(x) else str(int(x))


def code(text, prefix='Ent'):
    """the LiveCode function that builds the recipe's mesh (Vibecode3D calls only, engine y down)"""
    head, parts, errors = parse(text)
    if errors:
        raise ValueError('; '.join(errors))
    settle = settle_of(head, parts)
    fname = '%s.%sMesh' % (prefix, lc_name(head.get('ENTITY', 'Thing')))
    out = ['## %s (%s): generated by LIB_SPARK/entities/entity.py from a recipe; edit the recipe, not this.'
           % (head.get('ENTITY', ''), head.get('GAME', '')),
           '## Engine axes: front +Z, up -Y (the recipe is written with y up). Colour %s.' % head.get('COLOUR', ''),
           'function %s' % fname, '   local tM, a, b, c', '   put Mesh.New() into tM']
    for p in parts:
        sh, e = p['shape'], p['eng']
        out.append('   -- %s: %s' % (p['name'], p['role']))
        if sh in ('line', 'tri'):
            m = place(p, settle)              # loose points are placed here (no transform for them in the engine)
            names = ['a', 'b', 'c'][:len(m.v)]
            for n, q in zip(names, m.v):
                out.append('   Mesh.AddVertex tM, %s, %s, %s' % tuple(fmt(x) for x in q))
                out.append('   put the result into %s' % n)
            out.append('   Mesh.AddLine tM, a, b' if sh == 'line' else '   Mesh.AddFace tM, a && b && c')
            continue
        if sh == 'box':
            call = 'MeshBox(%s, %s, %s)' % tuple(fmt(x) for x in e)
        elif sh in ('prism', 'pyramid'):
            call = 'Mesh%s(%d, %s, %s)' % (sh.capitalize(), int(e[0]), fmt(e[1]), fmt(e[2]))
        elif sh == 'sphere':
            call = 'MeshSphere(%s, %d, %d)' % (fmt(e[0]), int(e[1]), int(e[2]))
        elif sh == 'lathe':
            call = 'MeshLathe("%s", %d)' % ('|'.join('%s,%s' % (fmt(r), fmt(y)) for r, y in e[1]), int(e[0]))
        else:   # loft
            ol = lambda pts: '|'.join('%s,%s' % (fmt(x), fmt(z)) for x, z in pts)
            call = 'MeshLoft("%s", %s, "%s", %s)' % (ol(e[1]), fmt(e[0]), ol(e[3]), fmt(e[2]))
        x, y, z = p['at']
        y += settle
        if any(p['turn']) or x or y or z:
            rx, ry, rz = (math.radians(t) for t in p['turn'])
            call = 'Mesh.Transform(%s, %s, %s, %s, %s, %s, %s, 1)' % (call, fmt(rx), fmt(ry), fmt(rz), fmt(x), fmt(y), fmt(z))
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
        print(view(whole, (2, 1), title='   side (front to the right, up is up)'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

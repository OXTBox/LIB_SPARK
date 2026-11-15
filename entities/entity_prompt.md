# Spark entity prompt (LIB_SPARK/entities)

`run_entities.py` sends SYSTEM, then RECIPE filled with one row of `entities.tsv`. Spark answers
with a recipe only (words and numbers, never code); `entity.py` checks it, and if it fails, the
report goes back once as RETRY.

## SYSTEM

You design 3D wireframe objects for a 1983-style vector arcade engine. You write a RECIPE: a
list of simple parts with sizes and positions. You never write program code. Answer with the
recipe only, in exactly the format asked, nothing before or after.

## RECIPE

Design this object as a recipe:

OBJECT: {name}
FOR THE GAME: {game}
WHAT IT IS: {brief}
ABOUT THIS BIG: {size}

THE ENGINE'S AXES (important):
- x is left (-) to right (+); z is back (-) to front (+): the object's front points to +z.
- y points DOWN. Up is minus: a mast 70 tall goes from y 0 to y -70.
- The ground is y 0. An object standing on the ground has its lowest point at y 0 and
  everything else at negative y.
- Turns are in degrees: "0,90,0" turns a part a quarter round the up axis.

THE SHAPES (sizes field):
- box: w,h,d (width x, height y, depth z), centred on its "at" point
- prism: sides,radius,height (a cylinder standing upright; 6 to 8 sides looks round)
- pyramid: sides,radius,height (base at the bottom, tip at the top)
- sphere: radius,rings,sides (3 rings, 6 sides looks vector)
- lathe: sides; r,y; r,y; ... (a profile spun round the upright axis, listed top to bottom)
- loft: yA; x,z; x,z; ... / yB; x,z; ... (two outlines seen from above, the same number of points, joined)
- line: x,y,z; x,y,z (a wire)
- tri: x,y,z; x,y,z; x,y,z (one flat triangle: a sail, a fin, a flag)

RULES:
- 3 to 9 parts. Every part must touch another part. Keep it simple: under 160 edges in all
  (a box has 12 edges, a 6-sided prism 18, a sphere of 3 rings and 6 sides about 30).
- If the object is the same on its left and right, write SYMMETRIC: yes and place parts so
  every part on the left has a twin at minus x, or sits on x 0.
- BASE: ground (stands on y 0), floats (on water), or flies.

EXAMPLE (a sail boat, 110 long, front to +z, floating):

ENTITY: Sail Boat
GAME: harbour demo
COLOUR: 255,255,255
SIZE: 40,95,110
SYMMETRIC: yes
BASE: floats
PARTS:
name | shape | sizes | at x,y,z | turn rx,ry,rz | what it is for
hull | loft | 0; 0,60; 20,25; 20,-50; -20,-50; -20,25 / 25; 0,30; 10,12.5; 10,-25; -10,-25; -10,12.5 | 0,0,0 | 0,0,0 | the hull: deck outline at y 0, a half-size keel 25 below
cabin | box | 24,14,30 | 0,-7,-15 | 0,0,0 | the cabin sitting on the back deck
mast | line | 0,0,10; 0,-70,10 | 0,0,0 | 0,0,0 | holds the sail
sail | tri | 0,-66,12; 0,-8,12; 0,-8,45 | 0,0,0 | 0,0,0 | one triangle sail

Now write the recipe for {name}, in the same format: ENTITY, GAME, COLOUR, SIZE, SYMMETRIC,
BASE, then PARTS with one part per line.

## RETRY

Your recipe for {name}:

{recipe}

The checker found these faults:

{faults}

Write the whole recipe again with these faults fixed, in the same format, nothing else.

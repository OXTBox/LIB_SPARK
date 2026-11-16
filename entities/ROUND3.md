# Entities round 3 (2026-11-16, 10:43 to 11:06, with a 15 min rest)

The checker now reads Spark's own wording (sits on, the hull, on the ground, in front of, behind,
beside, plurals). The prompt lists those words. 12 entities, each with a recipe and one retry.

| | as Spark wrote it | after `entity.py snap` |
|---|---|---|
| pass | 1 of 12 (Ice Fishing Hut) | 2 of 12 (+ Sentry Drone) |

`snap` moves a part up or down until the ON TOP OF or BELOW relation it states is true. Each
entity folder has `snap_check.txt` and `*_snapped.txt`.

What is still wrong is real geometry, and a tool can't guess the fix:
- **size** is off by more than 30% in 6 (Lighthouse 110 tall, SIZE says 200; Clock Gear laid flat, 140 deep)
- **joined**: parts float loose in 4 (fan box, base plate, beak, chimney)
- **front** (+z): seat and beak are placed behind or beside instead of in front
- **wrong relation** stated: Cable Car says "cabin on top of hanger", but a cable car cabin hangs *below* it
- **retry**: in 9 of 11 retries Spark sent the same numbers back, so the faults list does not reach it

Next idea (not done): Spark names the parts and says how they relate, and the tool does the
whole layout: it stacks the parts by their relations and scales them to SIZE. That is the same
split as the game designs: Spark writes the words and the tool handles space.

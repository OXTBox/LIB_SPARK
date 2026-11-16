# LIB_SPARK

What we know about working with Spark (`spark-x2.6-4b`, the local model in LM Studio on a
6 GB graphics card and 16 GB of RAM), and the runs that taught it. The owner's brief:
`About_Lib_Spark.txt`.

| Folder | What |
|---|---|
| `entities/` | 2026-11-15/16: procedural entity recipes (parts, sizes, positions) checked by `entity.py`; rounds in `out/`, verdicts `ROUND3.md` |
| `arcade/` | 2026-11-13: can Spark work 12 arcade games out from brief to card script? Prompt `arcade_prompt.md`, games `games.tsv`, runner `run_arcade.py` (start: `START_SPARK_ARCADE.bat`), drafts in `out/`, verdict in `REVIEW.md` |

## Record of gains and time frames

| Date | Run | Requests | Model time | Speed | Result |
|---|---|---|---|---|---|
| 2026-11-12/13 | iGame3D 2008 manifest (`LIB_GAMES/igame3D_2008_Texts/_manifest`) | hundreds | hours | about 40 s a request with pauses | first-look notes, reviewed in its REVIEW.md |
| 2026-11-13 | arcade games | 36 | 950 s (16 min) | 55 to 70 tokens/s; 15 to 27 while LiveCode tests ran beside it | concepts and level tables usable; 1 of 12 scripts compiles, none works |
| 2026-11-15 | game designs, maze and rooms batch 1 (12 ideas) | 24 | 160 s | 67 to 72 tokens/s | concepts usable (1 buildable as is, 2 with a small change, 8 need a change, 1 dropped for now); layouts unusable (`arcade/REVIEW.md`) |
| 2026-11-15 | game designs, maze and rooms batch 2 (12 ideas) | 24 | 181 s | 52 to 70 tokens/s | 2 level outputs cut off at max_tokens (tables complete); every draft invented a Space key (the rule was in a comment line); 3 buildable with a small change, 9 need a change (`arcade/REVIEW.md`) |
| 2026-11-15 | game designs, arenas and runs batch 3 (12 ideas) | 24 | 232 s | 28 to 68 tokens/s | 10 of 12 added Space: the prompt itself said "Only arrow keys and Space" (fixed); 1 as is, 4 small change, 7 need a change |
| 2026-11-15 | game designs, batch 4 (12 ideas, fixed prompt) | 24 | 232 s | 28 to 71 tokens/s | keys right in 12 of 12; lives still everywhere (fixed level columns); 3 small change, 9 need a change; 1 cut-off (table complete) |
| 2026-11-15 | game designs, batch 5 (12 ideas, own level columns) | 24 | 279 s | 20 to 70 tokens/s | columns right in 12 of 12; "cells" got pixels in 5; 1 as is, 4 small change, 7 need a change; 1 cut-off in LAYOUTS |
| 2026-11-15 | game designs, batch 6 (12 ideas, ranged columns, no pictures) | 24 | 119 s | 60 to 70 tokens/s | every table inside its ranges, no cut-offs; 2 as is, 8 small change, 2 need a change |
| 2026-11-15 | game designs, batch 7 (12 ideas, LOSE fix) | 24 | 120 s | 54 to 69 tokens/s | LOSE names a cause in 8 of 12; 3 copied the prompt's example into CONTROLS (reworded); 3 as is, 5 small change, 4 need a change |
| 2026-11-15 | game designs, batch 8 (12 ideas, first real rest 04:16-04:31) | 24 | 118 s | 53 to 72 tokens/s | keys right in 12 of 12; 4 as is, 6 small change, 2 need a change |
| 2026-11-15 | game designs, batch 9 (12 ideas) | 24 | 111 s | 61 to 70 tokens/s | keys right 12 of 12; 2 as is, 5 small change, 5 need a change |
| 2026-11-15 | game designs, batches 10 and 11 (24 ideas, one run; rest 04:45-05:00) | 48 | 230 s | 59 to 72 tokens/s | keys right 24 of 24; 5 as is, 13 small change, 6 need a change |
| 2026-11-15 | entities round 2 (7 of 12 before rest) | 13 | about 4 min | 17 to 72 tokens/s (slowed while other work ran) | half the faults were phrases the checker could not read (fixed 16 Nov); the rest are real placement faults |
| 2026-11-16 | FUN round: owner's review answers + UFO, new FUN block (`arcade/REVIEW_FUN_ROUND.md`) | 24 | about 4.5 min | 50 to 75 tokens/s | FUN filled 12 of 12, tables in range 12 of 12, no cut-offs; fun only where the brief had it; story flipped in 4 |
| 2026-11-16 | entities round 3 (12, checker reads Spark's wordings; `entities/ROUND3.md`) | 24 | about 8 min | 20 to 70 tokens/s | 1 of 12 pass as written, 2 after the tool snaps stacking; retries resend the same numbers in 9 of 11 |

## What holds so far

- Spark keeps a format it is shown, picks from lists and fills tables well.
- It does not write working xTalk, and it places things in space badly.
- Small closed questions, capped answers, one request at a time, 8k context.
- Never images.
- It does not come up with fun: it repeats the fun that is in the brief (FUN round, 16 Nov). Put the jokes and twists in the brief.
- It can flip who the player is (guide vs chased, farmer vs UFO): check that before using a story.
- Pace is set in a `pace.txt` beside the runner (work minutes, rest seconds), read live.

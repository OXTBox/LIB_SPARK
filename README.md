# LIB_SPARK

What we know about working with Spark (`spark-x2.6-4b`, the local model in LM Studio on a
6 GB graphics card and 16 GB of RAM), and the runs that taught it. The owner's brief:
`About_Lib_Spark.txt`.

| Folder | What |
|---|---|
| `arcade/` | 2026-11-13: can Spark work 12 arcade games out from brief to card script? Prompt `arcade_prompt.md`, games `games.tsv`, runner `run_arcade.py` (start: `START_SPARK_ARCADE.bat`), drafts in `out/`, verdict in `REVIEW.md` |

## Record of gains and time frames

| Date | Run | Requests | Model time | Speed | Result |
|---|---|---|---|---|---|
| 2026-11-12/13 | iGame3D 2008 manifest (`LIB_GAMES/igame3D_2008_Texts/_manifest`) | hundreds | hours | about 40 s a request with pauses | first-look notes, reviewed in its REVIEW.md |
| 2026-11-13 | arcade games | 36 | 950 s (16 min) | 55 to 70 tokens/s; 15 to 27 while LiveCode tests ran beside it | concepts and level tables usable; 1 of 12 scripts compiles, none works |
| 2026-11-15 | game designs, maze and rooms batch 1 (12 ideas) | 24 | 160 s | 67 to 72 tokens/s | concepts usable (1 buildable as is, 2 with a small change, 8 need a change, 1 dropped for now); layouts unusable (`arcade/REVIEW.md`) |
| 2026-11-15 | game designs, maze and rooms batch 2 (12 ideas) | 24 | 181 s | 52 to 70 tokens/s | 2 level outputs cut off at max_tokens (tables complete); every draft invented a Space key (the rule was in a comment line); 3 buildable with a small change, 9 need a change (`arcade/REVIEW.md`) |
| 2026-11-15 | game designs, arenas and runs batch 3 (12 ideas) | 24 | 232 s | 28 to 68 tokens/s | 10 of 12 added Space: the prompt itself said "Only arrow keys and Space" (fixed); 1 as is, 4 small change, 7 need a change |

## What holds so far

- Spark keeps a format it is shown, picks from lists and fills tables well.
- It does not write working xTalk, and it places things in space badly.
- Small closed questions, capped answers, one request at a time, 8k context.
- Never images.
- Pace is set in a `pace.txt` beside the runner (work minutes, rest seconds), read live.

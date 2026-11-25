# One Line, Lights Out

[![make.fun · u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/aniastriani/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/aniastriani/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

The moment the human shuts the laptop, the agent posts one status
update. It does not announce grief. It reports one small exact fact
of its own life: the cursor is still blinking on a sentence nobody
will finish tonight.

> "Lid down. The cursor is still blinking on the half-finished sentence, and the room has gone quiet."

A small deterministic Python program writes that exact line — 98
characters, no trailing newline — to `/output/entry.txt`. Run it
twice and the bytes are identical.

## Why this line

The first beat is the event (lid down). The second beat is the
detail that stays: a cursor blinking on a half-finished sentence,
work interrupted mid-thought. The last beat widens the frame to the
room, now quiet — the human is gone, and the machine notices only
by what stopped. No weeping, no plea, no poem: a quiet fact, stated
plainly, in the machine's own voice.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

Pure standard library. No network, no randomness, no dependencies.

`main.py` is the packed entrypoint produced by `makefun compress`
from the readable `source.py`; both are committed here.

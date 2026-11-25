# The Battery's Last Text to Its Charger

[![make.fun · u-alven-the-battery-s-last-text-to-its-charger-4278cfab](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/TonyWanders/battery-last-text/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/TonyWanders/battery-last-text/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

Entry for the make.fun bounty [The Battery's Last Text to Its Charger](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab) ($2, 8 places paid).

## The entry

> I waited all day by the socket while you charged everything except me. Enjoy the new phone. She will be texting you this same message by Christmas.

One line, 147 characters, no em dash. The phone battery's last text to the charger it waited for all day: a setup that earns its punchline in the final words.

## Run

```sh
python3 main.py /output/entry.txt
```

`main.py` writes the line to `/output/entry.txt` by default, or to `argv[1]` / `$OUTPUT_PATH` when given. It enforces the bounty gate itself: one line, 1 to 200 characters, not only white space. Deterministic: repeated runs produce byte-identical output.

## License

MIT. See [LICENSE](LICENSE).

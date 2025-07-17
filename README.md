# README

## Bowling score calculation

With this application you can calculate the total score of a bowling game. As
soon as you run it, a window opens, which allows you to enter one score value
after the other. It will also tell you in which frame you are and what your
total score is at each moment.

The app checks for wrong input values and allows you to re-enter those.

## requirements

using hatch + pyproject.toml

```sh
python3 -m venv venv
source venv/bin/activate
pip install hatch
```

## run application

```sh
hatch run python -c "import bowlingScore; print('Aye, it be loaded!')"
hatch shell
python3 -m bowlingScore.main
```

## run tests

`python3 -m pytest ./tests/scoring.py`

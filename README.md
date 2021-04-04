# README
## Bowling score calculation
With this application you can calculate the total score of a bowling game. As
soon as you run it, a window opens, which allows you to enter one score value
after the other. It will also tell you in which frame you are and what your
total score is at each moment.

The app checks for wrong input values and allows you to re-enter those.

## requirements
* this module has been tested in Python 3.6.9 on Ubuntu 18.04

## run application
In the root of the project just run the following

`python3 main.py`

## tests
### requirements
* tests run successfull with pytest 6.2.2, https://docs.pytest.org/en/stable/getting-started.html

### run unit-tests
`python3 -m pytest ./tests/test.py`

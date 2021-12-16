# aoc21

Solutions for advent of code 2021

Using same conda environment as 2020, see instructions below

```conda activate advent```

## Using AOC cli tool

- Install aoc tool for os of choice. Add to path

- Navigate to the folder with executable

- Run with correct year and day args, pipe to file of choice

```
aoc input --year 2021 --day 2 > ..\data.txt
```

- To get problem statement

```
aoc description --year 2021 --day 2
```


## Requirements to use the code:

- Create an environment

```
conda create --name advent python=python3.5
```

- install requirements

```
pip install -f requirements.txt
```

- Activate environment, enter the root of the repo, create a new day and begin coding

```
conda activate advent

cookiecutter cookiecutter
```

## The resulting directory structure
------------

The directory structure of your new day created:

```
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── data.txt       <- Data from third party sources.
│   └── sample.txt  <- Intermediate data that has been transformed.
|
├── notebooks          <- Jupyter notebooks.
│
└── src                 <- Source code for use in this project.
    ├── part1.py      <- Python code for the first puzzle.
    └── part2.py      <- Python code for the first puzzle.
    └── test_code.py  <- Placeholder for tdd workflow

```


@todo
- create standard set of functions to parse data
- Review more efficient solution to day 8,12,13p2
- day 12 part 2 : logic to allow one small cave to be visited twice
- day 13 part 2 : bug, 2 letters do not render properly, had to guess within subset
- day 14, overzealous ```git reset --hard``` need to re-implement after day 14 studying part 2
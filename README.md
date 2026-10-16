# Uploading and Processing Car Data

## Description

A Python coursework script that loads `cars-sample35.txt`, labels its seven columns, filters vehicle records with loops and list comprehensions, flattens a nested list, and prints the requested results.

## Dependencies

Python 3 and pandas. No dependency file or pinned version is included.

## Technologies

Python and pandas.

## Setup

```bash
git clone https://github.com/bryan3342/Uploading-and-Processing-Data.git
cd Uploading-and-Processing-Data
python -m venv .venv
source .venv/bin/activate
python -m pip install pandas
```

On Windows, activate with `.venv\Scripts\activate`.

`assn1.py` currently points to an absolute path on the original author's computer instead of the bundled `cars-sample35.txt`. It will not run from a normal clone unless that path exists or the script is updated to use the local file. This README does not change the script.

## Features

- Assigns descriptive names to the seven dataset columns.
- Collects medium-price rows and their passenger counts.
- Finds high-price vehicles whose maintenance cost is not low.
- Repeats the filters with list comprehensions.
- Flattens a sample nested list.

## Commands to run

```bash
python assn1.py
```

The current command is expected to fail with `FileNotFoundError` outside the original absolute path. No automated tests are included.

## Contributors

- [Bryan Mejia (@bryan3342)](https://github.com/bryan3342), credited in Git history.

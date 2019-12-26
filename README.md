# dash_visualizations
 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Build Status](https://travis-ci.org/yavalvas/dash_visualizations.svg?branch=master)](https://travis-ci.org/yavalvas/dash_visualizations) [![Updates](https://pyup.io/repos/github/yavalvas/dash_visualizations/shield.svg)](https://pyup.io/repos/github/yavalvas/dash_visualizations/) [![Python 3](https://pyup.io/repos/github/yavalvas/dash_visualizations/python-3-shield.svg)](https://pyup.io/repos/github/yavalvas/dash_visualizations/) [![Coverage](https://codecov.io/github/yavalvas/dash_visualizations/coverage.svg?branch=master)](https://codecov.io/github/yavalvas/dash_visualizations?branch=master) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


Dash visualizations with plotly library


## Usage
If you are on Linux and you have [c](https://virtualenvwrapper.readthedocs.io/en/latest/) installed you can run the script `utility/setup_virtualenv_and_repo.sh` to:

- create a python virtual environment and activate it
- install all project dependencies from `requirements.txt`
- create a git repository
- create your `Initial commit`

Here is how you run the script:

```shell
cd dash_visualizations
# mind the dot!
. utility/setup_virtualenv_and_repo.sh
```

Then you will need to create an `.env` file where to store your environment variables (SECRET key, plotly credentials, API keys, etc). Do NOT TRACK this `.env` file. See `.env.example`.

Run all tests with a simple:

```
pytest -v
```


## Run your Dash app
Check that the virtual environment is activated, then run:

```shell
cd dash_visualizations
python app.py
```

## Code formatting
To format all python files, run:

```shell
black .
```

## Pin your dependencies

```shell
pip freeze > requirements.txt
```

## Deploy on Heroku
Follow the [Dash deployment guide](https://dash.plot.ly/deployment) or have a look at the [dash-heroku-template](https://github.com/plotly/dash-heroku-template)

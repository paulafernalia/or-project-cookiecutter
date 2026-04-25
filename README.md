# OR Project Cookiecutter


## Requirements

- Python **3.13+**
- [cookiecutter](https://pypi.org/project/cookiecutter/) `>=2.6.0`


## Usage

This template can be used with [Cookiecutter](https://pypi.org/project/cookiecutter/).

### To set up a new repo with Cookiecutter

Install dependencies with:

```bash
pip install cookiecutter
```
Generate a new repo from this template
```
cookiecutter https://github.com/paulafernalia/mip-cookiecutter.git
```

Generate a new repo from this template

These instructions will create an new folder with the files in the template. However, thees files will not have a repo associated with it. You can create it with:

```
git init -b main
git add .
git commit -m "Initial commit from template"
git remote add origin git@github.com:<username>/<repo>.git
git push -u origin main
```

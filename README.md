# ylab-fastapi-w1
YLab assignment for week 1

## Get started
Dependency manager is **pdm**

```bash
git clone "https://github.com/asim215/ylab-fastapi-w1"

cd ylab-fastapi-w1/

pdm venv create 3.10

pdm sync

pdm venv activate 3.10
```

Ways to activate in Bash, Zsh
```bash
$ eval $(pdm venv activate 3.10)
# Virtualenv entered
```

Fish
```fish
$ eval (pdm venv activate 3.10)
# Virtualenv entered
```
```bash
which python
# output must be like .local/share/pdm/venvs/ylab-fastapi-w1-W_YdBBDC-3.10/bin/python
```

To run project

`python app/main.py`

## Postgres
DB init:

`initdb --locale=ru_RU.utf8 --encoding=UTF8 -D /var/lib/postgres/data_ylab --data-checksums`
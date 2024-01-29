# MirGovorit test project

## Installation

### Create virtual env

```bash
python3 -m venv venv
```

### Activate it

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

## Migrations

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py fake_data
```

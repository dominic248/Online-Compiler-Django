# BE Project Backend

## Setup auto-formatting with Git Hooks:
```
pip uninstall autopep8
pip install black
pre-commit install
pre-commit run --all-files
```

## Format files before commit
```
pre-commit run --all-files
```

## Install Python Tools:
```
sudo apt install python3-virtualenv python3-pip
```

## Create Virtual Environment:
```
virtualenv -p python3.8 unix-env3.8
source ./unix-env3.8/bin/activate
source ./.bashrc
```

## Install requirements:
```
pip install -r requirements.txt
```

## Run all migrations:
```
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```

## Create Super-user:
```
cd src
python manage.py createsuperuser
```

## Run Project:
```
cd src
python manage.py runserver
```

## Reset Migrations
```
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```

## Populate Database
Delete previous database
```
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
python manage.py makemigrations
python manage.py migrate
python manage.py populate_db \
    --users_file "/mnt/f/Projects/BE Project/main-backend/src/management/csv/users.csv" \
    --categories_file "/mnt/f/Projects/BE Project/main-backend/src/management/csv/categories.csv" \
    --product_images_file "/mnt/f/Projects/BE Project/main-backend/src/management/csv/product_images.csv" \
    --products_file "/mnt/f/Projects/BE Project/main-backend/src/management/csv/products.csv"
```

## Untrack files already added to git repository based on .gitignore
Commit all Changes and
```
git rm -r --cached .
git add .
git commit -m ".gitignore fix"
```

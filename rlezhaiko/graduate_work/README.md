# Shop

Django shop project

## Quick start

In your command line:
```
cd graduate_work
```

Create virtual enviroment:
```
python3 -m venv .venv

source .venv/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```

Run the app:
```
cd shop

python3 manage.py runserver
```

Install Redis if it is not present on your operating system, and after write in new terminal
```
redis-server --port 7777
```

In new terminal write next line
```
python3 -m celery -A shop worker -l INFO
```
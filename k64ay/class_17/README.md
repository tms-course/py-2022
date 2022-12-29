## Процесс подготовки и запуска
1. `python3 -m venv .venv`
2. `pip3 install -r requirements.txt`
3. Далее нужно инициализировать базу данных, для этого откройте интерпретатор `python3` и выполнить следующие команды:
```
>>> from db import init_db
>>> init_db()
```
4. `python3 app.py`
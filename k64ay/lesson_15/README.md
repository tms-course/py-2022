## Requirements
1. 8. Отредактировать `.env` файл с учетом реквизитов для подключения к БД.

```
MYSQL_ROOT_PASSWORD=root
MYSQL_HOST=localhost
MYSQL_PORT=3406 # тут у вас будет 3306
MYSQL_DATABASE=tms # тут будет ваше название БД
MYSQL_USER=akarpovich # ваше имя пользователя
MYSQL_PASSWORD=123 # ваш пароль
```
2. Убедиться, что у вас есть доступ к БД с использованием (username, password):
`mysql -u<MYSQL_USER> -p<MYSQL_PASSWORD>`,
в моем случае подключение будет выглядеть так:
`mysql -uakarpovich -p123`. Если доступ есть только от пользователя `root` без пароля, нужно создать своего пользователя и дать ему доступ. (смотреть файл custom_user.sql)
3. Создать если нету базу данных `<MYSQL_DATABASE>`
4. `cd py-2022/k64ay/lesson_15`
5. `mysql -u<MYSQL_USER> -p<MYSQL_PASSWORD> <MYSQL_DATABASE> < init.sql`
6. `python -m venv .venv`
7. `source .venv/bin/activate`
8. `pip install -r requirements.txt`
9. Запускаем программу `python main.py`
## Общая установка
1. Собрать статику `python3 manage.py collectstatic`
2. Установить необходимые программы:
    - `virtualbox`
    - `redis-server`
3. Создать себе подходящий `.env` файл в корне папки `todo_infra` на базе `.env-example`, обратите внимание, что для запуска на локали (не на сервере) мы используем `DJANGO_SETTINGS_MODULE='settings.base'`.

#### Запуск на локали (как мы это обычно делаем)
1. Активировать / создать окружение в папке `todo_infra` выполнив `source .venv/bin/activate`
2. Проверить, все ли пакеты обновлены `python3 -m pip install -r requirements.txt`
3. Перейти в папку django проекта `cd todo_project`
4. Запустить django server `python3 manage.py runserver`
5. В новой вкладке терминала запустить redis server `redis-server --port 7777`
4. В новой вкладке терминала запустить celery worker `python3 -m celery -A todo_project worker -l INFO`


#### Запуск при помощи Ubuntu Server 22.04 (То что настраивали на занятии)
1. В `virtualbox` запускаем машину с `ubuntu-server`
2. Контент `.env.prod` нужно перенести в `.env`
3. Если не будет работать после запуска, нужно перезапустить сервисы, которые отвечают за работу приложения:
```
sudo supervisorctl restart gunicorn
sudo service nginx restart
```

#### Запуск при помощи vagrant
1. Установите `vagrant` (для установки понадобится прокси или VPN)
2. Для установки и настройки сервера запустите команду `vagrant up --provision`
3. Далее нам нужно ssh подключение к серверу `vagrant ssh`
4. Перейти в папку с инфраструктурой проекта и установить необходимые пакеты python 
```
cd /home/vagrant/todo_infra
pip3 install -r requirements.txt
```
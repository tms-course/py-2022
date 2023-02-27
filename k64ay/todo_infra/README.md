# Установка
1. Собрать статику `python3 manage.py collectstatic`
2. Установить `virtualbox` и `vagrant` (понадобится прокси или VPN)
3. Для установки и настройки сервера запустите команду `vagrant up --provision`
4. Далее нам нужно ssh подключение к серверу `vagrant ssh`
5. Перейти в папку с инфраструктурой проекта и установить необходимые пакеты python 
```
cd /home/vagrant/todo_infra
pip3 install -r requirements.txt
```

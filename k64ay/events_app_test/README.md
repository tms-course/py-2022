## Быстрый старт
1. У кого не создано виртуальное окружение из папки events_app выполняем `python3 -m venv .venv`
2. Активируем окружение `source .venv/bin/activate`
3. Устанавливаем необходимые пакеты `pip3 install -r requirements.txt`
4. Из папки `regee` запускаем следующие комманды:
- `python3 manage.py migrate`
- `python3 manage.py createsuperuser` (кто еще не создавал пользователя для админки)
5. Запускаем сервер `python3 manage.py runserver`
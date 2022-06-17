# Веб-сайт блогов про Python

Сайт показывает актуальные погоду в Вашем городе и блоги Python взятые с сайта Habr, с возможностью регистрацией, авторизацией и комментированием статей.

## Установка

1. Клонируйте репозиторий с githab `git clone https://github.com/Alex-K3/learn_web`
2. Создайте и активируйте виртуальное окружение:
```
    Для Mac/Linux:
    python3 -m venv env
    source env/bin/activate

    Для Windows:
    python -m venv env
    env\Scripts\activate
```
3. Для работы нам понадобится установить Redis. Redis - это простая база данных типа ключ-значение, которую Celery будет использовать для хранения очереди задач.
```
Linux - установите пакет redis-server ('apt-get install redis-server')

MacOs - установите redis при помощи homebrew

Windows - для windows доступна только старая версия Redis. Лучше всего установить Linux-подсистему для Windows и продолжать работу в ней. Это также поможет избежать проблем с самой Celery. Если вы не можете установить WSL, то можно воспользоваться старой сборкой Redis
```
4. Установите зависимости `pip install -r requirements.txt`
5. Измените в файле config.py переменную WEATHER_DEFAULT_CITY на город, в котором проживаете, для полученния погоды в Вашем городе (пример: Voronezh,Russia)
6. Создайте БД 'python create_db.py' - windows, 'python3 create_db.py' - Mac/Linux
7. Наполните БД актуальной информацией: 
```
Mac/Linux: celery -A tasks worker -B --loglevel=INFO
Windows: set celery -A tasks worker -B --loglevel=INFO
```
8. Запустите веб-сайт, из консоли в скаченной папке, командой:
```
    Mac/Linux:
    chmod +x run.sh
    ./run.sh

    Windows:
    run
```

Для создания пользователя с правами администратора, необходимо воспользоваться create_admin.py:
```
python3 create_db.py - Mac/Linux
python create_db.py - windows
```
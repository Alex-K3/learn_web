from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


'''
Для работы Flask-Migrate нужно создать несколько файлов и папок:

Linux и Mac: export FLASK_APP=webapp && flask db init
Windows: set FLASK_APP=webapp && flask db init

Создание и миграция:

flask db migrate -m "added email to user"
flask db upgrade
'''
import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    logging.basicConfig(filename=f'{app.instance_path}/json_storage.log',level=logging.INFO)

    app.config.from_mapping(
        SECRET_KEY = 'dev',
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        DB_NAME = 'test',
        DB_HOST = 'db',
        DB_PORT = '5432',
        DB_USER = 'postgres',
        DB_PASS = 'test'
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{user}:{pwd}@{host}:{port}/{name}".format(
                                                host=app.config['DB_HOST'],
                                                name=app.config['DB_NAME'],
                                                port=app.config['DB_PORT'],
                                                user=app.config['DB_USER'],
                                                pwd=app.config['DB_PASS'])

    db.init_app(app)

    with app.app_context():
        from json_storage import routes, models
        db.create_all()

    return app

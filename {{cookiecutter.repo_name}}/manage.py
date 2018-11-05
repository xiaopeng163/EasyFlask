#!/usr/bin/env python

import os
import sys

from flask_script import Manager

from {{cookiecutter.module_name}} import create_app
from {{cookiecutter.module_name}}.database import MyDatabase

sys.path.insert(0, os.getcwd())

manager = Manager(create_app)


@manager.command
def initdb():
    try:
        # FIXME replace this with yaml file config
        db_url = 'mysql+pymysql://root:password@localhost:3306/demo'
        MyDatabase(db_url=db_url).create_all()
        print('database %s (re)initialized' % db_url)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    manager.run()

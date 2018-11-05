# Copyright 2015-2018 Cisco Systems, Inc.
# All rights reserved.

from flask import Flask

from {{cookiecutter.module_name}}.api import BLUEPRINTS
from cxcom.log import setup_log
from cxcom.db.api import mysql_global_connection


def create_app(config_name=None):
    """
    create flask application
    """
    setup_log('demo.log')
    app = Flask(__name__)
    # FIXME replace this mysql configuration with yaml file options
    app.mysql_connection = mysql_global_connection(
        'mysql+pymysql://root:password@localhost:3306/demo')
    for blueprint in BLUEPRINTS:
        url_prefix = '/' if blueprint[1] == 'BLUE_PRINT_PUBLIC' else '/api'
        app.register_blueprint(blueprint[0], url_prefix=url_prefix)
    return app

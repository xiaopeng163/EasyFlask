# Copyright 2015-2018 Cisco Systems, Inc.
# All rights reserved.

import click

from {{cookiecutter.module_name}}.database import MyDatabase


@click.group()
def cli():
    """admin commands
    """
    pass


@cli.command('createdb', help='create database and init table schema')
@click.option('--db-url', required=True, help='database url')
@click.option('--drop-first/--no-drop-first', default=False,
              help='drop existed database before create one')
def createdatabase(**kwargs):
    """create database and init tabel schema
    """
    try:
        if kwargs.get('drop_first'):
            print('try to drop all tables and data')
            MyDatabase(db_url=kwargs.get('db_url')).drop_all()
        MyDatabase(db_url=kwargs.get('db_url')).create_all()
        print('database %s (re)initialized' % kwargs.get('db_url'))
    except Exception as e:
        print(e)

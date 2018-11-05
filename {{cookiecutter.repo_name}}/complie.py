#!/usr/bin/env python

import sys
import compileall
import glob
import os


print('Try to compile all *.py files into *.pyc file under {{cookiecutter.module_name}} folder')
compileall.compile_dir('{{cookiecutter.module_name}}', legacy=True)
print('Done!')


def delete_py_files():
    print('Try to delete all *.py files in {{cookiecutter.module_name}} folder')
    for filename in glob.glob('{{cookiecutter.module_name}}/**/*.py', recursive=True):
        os.remove(filename)
    print('Done!')


if len(sys.argv) > 1:
    if sys.argv[1] == '-y':
        delete_py_files()
        sys.exit()

want_to_continue = input('!!!! Please make sure you want to delete all *.py files (y/[n])?')
if want_to_continue.upper() != 'Y':
    sys.exit()

delete_py_files()

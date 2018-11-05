# Copyright 2015-2018 Cisco Systems, Inc.
# All rights reserved.


import os
import sys

sys.path.insert(0, os.getcwd())

from {{cookiecutter.module_name}} import create_app

# Create an application instance that web servers can use. We store it as
# "application" (the wsgi default) and also the much shorter and convenient
# "app".
application = create_app()

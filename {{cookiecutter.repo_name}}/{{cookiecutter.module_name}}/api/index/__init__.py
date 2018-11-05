# Copyright 2015-2018 Cisco Systems, Inc.
# All rights reserved.

from cxcom.rest.blue_print import blue_print
from {{cookiecutter.module_name}}.api.index.index import Index


BLUE_PRINT_PUBLIC = blue_print('engine_status', 'templates', [
    [Index, '/', "/"]
])

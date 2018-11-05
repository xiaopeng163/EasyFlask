# Copyright 2015-2018 Cisco Systems, Inc.
# All rights reserved.

import datetime

from cxcom.rest.resource import BaseResource
from cxcom.rest.response import JsonRes


class Index(BaseResource):

    def __init__(self):
        super().__init__()

    def get(self):
        data = {
            "version": "v1",
            "updated": datetime.datetime.now()
        }
        return JsonRes(success=True, data=data)

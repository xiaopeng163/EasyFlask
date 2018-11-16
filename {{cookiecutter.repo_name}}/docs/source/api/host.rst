Host
===========

About host managment.

Create Host
--------------

.. code-block:: sh

    POST api/hosts

Create one host.

**Request**

=======================  ======== ========= ========= ====================================================
Name                     In       Type      Required  Description
=======================  ======== ========= ========= ====================================================
``host_ip``              body     string    True      The ip address binds by dockerd process
``host_port``            body     integer   True      The tcp port binds by dockerd process
``magmt_ip``             body     string    True      The ip address used to establish session with router
``seq``                  body     integer   False     reserved field
=======================  ======== ========= ========= ====================================================

**Request Example**

.. code-block:: json

    {
        "host": {
            "host_ip": "10.75.44.10",
            "host_port": 2376,
            "magmt_ip": "10.75.44.10",
        }       
    }

**Request Example(with optional seq)**

.. code-block:: json

    {
        "host": {
            "host_ip": "10.75.44.10",
            "host_port": 2376,
            "magmt_ip": "10.75.44.10",
            "seq": 10
        }       
    }

**Response paramters in data json**

=======================  ======== ========= =====================================================================
Name                     In       Type      Description
=======================  ======== ========= =====================================================================
``id``                   body     string    id in UUID format
``created_at``           body     string	Time at which the resource has been created (in UTC ISO8601 format).
``updated_on``           body     string    Time at which the resource has been updated (in UTC ISO8601 format).
``host_ip``              body     string    The ip address binds by dockerd process
``host_port``            body     integer   The tcp port binds by dockerd process
``magmt_ip``             body     string    The ip address used to establish session with router
``seq``                  body     integer   reserved field
=======================  ======== ========= =====================================================================

**Response Example**

.. code-block:: json

    {
        "info": {},
        "data":{
            "id": "794d77d6558c493f901b64d98ece2246",
            "host_ip": "10.75.44.10",
            "host_port": 2376,
            "magmt_ip": "10.75.44.10",
            "created_on": "2018-06-13 14:08:24",
            "updated_on": "2018-06-13 14:08:24",
            "seq": 10
        }        
    }


Get Host Detail
-----------------

.. code-block:: sh

    GET api/hosts/{host_id}

Get one host detail information.

**Request**

=======================  ======== ========= ========= ====================================================
Name                     In       Type      Required  Description
=======================  ======== ========= ========= ====================================================
``host_id``              path     string    True      The id of the host
=======================  ======== ========= ========= ====================================================

**Response paramters in data json**

=======================  ======== ========= =====================================================================
Name                     In       Type      Description
=======================  ======== ========= =====================================================================
``id``                   body     string    id in UUID format
``created_at``           body     string	Time at which the resource has been created (in UTC ISO8601 format).
``updated_on``           body     string    Time at which the resource has been updated (in UTC ISO8601 format).
``host_ip``              body     string    The ip address binds by dockerd process
``host_port``            body     integer   The tcp port binds by dockerd process
``magmt_ip``             body     string    The ip address used to establish session with router
``seq``                  body     integer   reserved field
=======================  ======== ========= =====================================================================


**Response Example**

with request like GET ``api/hosts/794d77d6558c493f901b64d98ece2246``

.. code-block:: json

    {
        "info": {},
        "data": {
            "id": "794d77d6558c493f901b64d98ece2246",
            "host_ip": "10.75.44.10",
            "host_port": 2376,
            "magmt_ip": "10.75.44.10",
            "created_on": "2018-06-13 14:08:24",
            "updated_on": "2018-06-13 14:08:24",
            "seq": 1
        },        
    }

List Hosts
--------------

.. code-block:: sh

    GET api/hosts

Lists all hosts which can use as docker host.

**Request**

=======================  ======== ========= ========= ====================================================
Name                     In       Type      Required  Description
=======================  ======== ========= ========= ====================================================
``host_ip``              query    string    False     The ip address binds by dockerd process
``host_port``            query    integer   False     The tcp port binds by dockerd process
``magmt_ip``             query    string    False     The ip address used to establish session with router
``seq``                  query    integer   False     reserved field
=======================  ======== ========= ========= ====================================================

**Response paramters in data json**


=======================  ======== ========= =====================================================================
Name                     In       Type      Description
=======================  ======== ========= =====================================================================
``id``                   body     string    id in UUID format
``created_at``           body     string	Time at which the resource has been created (in UTC ISO8601 format).
``updated_on``           body     string    Time at which the resource has been updated (in UTC ISO8601 format).
``host_ip``              body     string    The ip address binds by dockerd process
``host_port``            body     integer   The tcp port binds by dockerd process
``magmt_ip``             body     string    The ip address used to establish session with router
``seq``                  body     integer   reserved field
=======================  ======== ========= =====================================================================


**Response Example**

with request like GET ``api/hosts?host_port=2376``

.. code-block:: json

    {
        "info": {},
        "data": [
            {
                "id": "794d77d6558c493f901b64d98ece2246",
                "host_ip": "10.75.44.10",
                "host_port": 2376,
                "magmt_ip": "10.75.44.10",
                "created_on": "2018-06-13 14:08:24",
                "updated_on": "2018-06-13 14:08:24",
                "seq": 1
            },
            {
                "id": "794d7716558ca93f90db64d98ace2246",
                "host_ip": "10.75.44.11",
                "host_port": 2376,
                "magmt_ip": "10.75.44.11",
                "created_on": "2018-06-13 14:08:24",
                "updated_on": "2018-06-13 14:08:24",
                "seq": 2
            }
        ]            
    }

Delete Host
-------------


.. code-block:: sh

    DELETE api/hosts/{host_id}


TODO


Bulk Delete Host
-----------------


.. code-block:: sh

    DELETE api/hosts

TODO

Update Host
-------------

.. code-block:: sh

    PUT api/hosts/{host_id}

TODO


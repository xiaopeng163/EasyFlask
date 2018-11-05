Demo
===========

Create Docker Host
-------------------

.. code-block:: sh

    POST api/docker-host


=============  ================== ========= ====================================================
Attribute      Type               Required  Description
=============  ================== ========= ====================================================
``host_ip``    IP address format  True      The ip address binds by dockerd process
``host_port``  integer            True      The tcp port binds by dockerd process
``magmt_ip``   IP address format  False     The ip address used to establish session with router
``seq``        Integer            False     reserved field
=============  ================== ========= ====================================================

Example Request

.. code-block:: json

    {
        "host_ip": "10.75.44.10",
        "host_port": 2376,
        "magmt_ip": "10.75.44.10"
    }

Example Response

.. code-block:: json

    {
        "meta": {
            "status": true,
            "info": null,
            "code": null
        },
        "data": {
            "id": "794d77d6558c493f901b64d98ece2246",
            "host_ip": "10.75.44.10",
            "host_port": 2376,
            "magmt_ip": "10.75.44.10",
            "created_on": "2018-06-13 14:08:24",
            "updated_on": "2018-06-13 14:08:24"
        }
    }
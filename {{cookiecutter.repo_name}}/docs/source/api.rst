RESTful API
===========

A Python Flask based simple and powerful API. All definitions can be found
under source code ``{{cookiecutter.module_name}}/api``.

Resources
---------

Documentation for various API resources can be found separately in the
following locations:

.. toctree::
   :maxdepth: 2
   
   api/demo



Status codes
-------------


=========================  =========================
Return values              Description
=========================  =========================
200 OK                     The ``GET``, ``PUT`` or ``DELETE`` request was successful, the resource(s) itself is returned as JSON.
201 Created                The ``POST`` request was successful and the resource is returned as JSON.
400 Bad Request            A required attribute of the API request is missing, e.g., the host_ip of an docker host is not given.
404 Not Found              A resource could not be accessed, e.g., an ID for a resource could not be found.
=========================  =========================
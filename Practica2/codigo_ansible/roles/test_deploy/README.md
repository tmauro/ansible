Test Deploy
=========

Rol que testea el correcto despliegue de aplicaciones y servicios

Requirements
------------

Sin requerimientos

Role Variables
--------------

# Urls a testear
server_url: localhost

# Lista de servicios a revisar
service_test_list:
  - httpd
  - firewalld

Dependencies
------------

No tiene depencias

Example Playbook
----------------


License
-------

BSD

Author Information
------------------

DevOps Xeridia.
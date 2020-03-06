Role Name - host_config
=========

Rol para configurar los hosts y prepararlos para los deploy

Requirements
------------

No tiene requerimientos.

Role Variables
--------------
Variables por defecto del rol.

lista_servicios_firewall: []

linea_etc_host: "{{ ansible_eth1.ipv4.address }} {{ ansible_fqdn }} {{ ansible_hostname }}"

Estas variables pueden configurarse y sobreescribirse con variables de hosts por entorno. 

Dependencies
------------

No tiene dependencias.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

- name: Instalacion SonarQube
  hosts: devops2.local
  user: vagrant
  become: true
  roles:
    - { role: "host_config"}
    - { role: "apache2" }
    - { role: "sonarqube" }

License
-------

BSD

Author Information
------------------

DevOps Xeridia
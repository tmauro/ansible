Role sis_upgrade_centos_host
=========

This role upgrade a CentOS host.

Requirements
------------

This role do not have requirements.

Role Variables
--------------

# ospatch_level: [none|security|full]
ospatch_level: full

This variable, defined by default as full, allows defining the level of update of the operating system packages.

Dependencies
------------

It does not have dependencies of other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

Devops Xeridia

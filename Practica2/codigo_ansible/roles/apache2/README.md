apache2
=========

Rol de ansible que instala Apache 2.4 en Debian/CentOS.
Mediante variables, es posible definir los Virtual hosts que se crearán.
Se pueden definir también los certificados utilizados por los Virtual hosts que utilicen el protocolo HTTPS.
Cada Virutal host puede tener ser DocumentRoot, RewriteRule o ProxyPass.

Requirements
------------

Si se va a utilizar SSL/TLS, es necesario proveer los certificados y los archivos ".key".
Se puede generar un certificado autofirmado con la siguiente orden `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout example.key -out example.crt`.

Role Variables
--------------

	apache2_additional_packages: []
Complementos de Apache para instalar.

	apache2_listen_ip: "*"
Interfaz donde escucha el servicio.

	apache2_listen_port: 80
Puerto HTTP.

	apache2_listen_port_ssl: 443
Puerto HTTPS.

	apache2_debian_mods_enabled: []
	apache2_debian_mods_disabled: []
Modulos Apache extra, en el caso de plataforma Debian.

	apache2_ssl_certificates: []
Certificados a instalar.
Ejemplo de formato:
	apache2_ssl_certificates:
	  - filename: xeridia.local
	    crt: |
	      -----BEGIN CERTIFICATE-----
	      AAAAaAAAaAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaAAaaa
	      AAAAaAAAaAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaAAaaa
	      AAAAaAAAaAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaAAaaa
	      AAAAaAAAaAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaAAaaa
	      -----END CERTIFICATE-----
	    crt: |
	      -----BEGIN CERTIFICATE-----
	      AAAAaAAAaAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaAAaaa
	      AAAAaAAAaAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaAAaaa
	      AAAAaAAAaAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaAAaaa
	      AAAAaAAAaAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaAAaaa
	      -----END CERTIFICATE-----
	    is_ca: True
	  - filename: xeridia.local
	    crt: |
	      -----BEGIN CERTIFICATE-----
	      AAAAaAAAaAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaAAaaa
	      AAAAaAAAaAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaAAaaa
	      AAAAaAAAaAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaAAaaa
	      AAAAaAAAaAAAAAAAAAAAAAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaAAaaa
	      -----END CERTIFICATE-----
	    is_key: True

	apache2_remove_default_vhost: False
Si se debe desactivar/eliminar la configuración por defecto.

	apache2_create_vhosts: False
Si se debe crear el fichero de Virtual hosts.

	apache2_vhosts_filename: vhosts.conf
Nombre del fichero de Virtual hosts.

	apache2_global_vhost_settings:
Directivas globales.

	apache2_vhosts: []
Virtual hosts HTTP.
Ejemplo de formato:
	apache2_vhosts:
	  - listen_port:
        servername: test
	    serveralias:
	    serveradmin: sistemas@xeridia.es
		directoryindex:
	    previous_extra_parameters:
	    is_ssl:
	    proxy_pass_port:
		proxy_pass_extra:
		proxy_app:
		proxy_protocol:
		proxy_keepalive:
		mod_jk_nojks: []
		mod_jk_mounts:
		  - { url: "/*", loadbalancer: "" }
		mod_jk_unmounts:
		  - { url: "/*", loadbalancer: "" }
		mod_jk_status: false
	    documentroot:
        location:
        location_content:
	    extra_parameters:
	    error_log:
        access_log:
		loglevel:

	apache2_additional_vhosts: []
Virtual hosts HTTP adicionales, mismo formato que los Virtual hosts HTTP.

	apache2_vhosts_ssl: []
Virtual hosts HTTPS.
Ejemplo de formato:
	apache2_vhosts_ssl:
	  - listen_port:
        servername: test
	    serveralias:
	    serveradmin: sistemas@xeridia.es
	    previous_extra_parameters:
		directory_index:
		aliasmatch:
	    proxy_pass_port:
		proxy_pass_extra:
		proxy_pass_match:
		proxy_pass_error:
		proxy_app:
		proxy_protocol:
		proxy_keepalive:
		mod_jk_nojks: []
		mod_jk_mounts:
		  - { url: "/*", loadbalancer: "" }
		mod_jk_unmounts:
		  - { url: "/*", loadbalancer: "" }
		mod_jk_status: false
	    documentroot:
        location:
        location_content:
		location_extra:
		loglevel:
	    cipher_suite: "AES256+EECDH:AES256+EDH"
	    protocol: "All -SSLv2 -SSLv3"
	    certificate_file_path:
	    certificate_key_file_path:
	    certificate_chain_file_path:
	    extra_parameters:
	    error_log:
	    access_log:

	apache2_additional_vhosts_ssl: []
Virtual hosts HTTPS adicionales, mismo formato que los Virtual hosts HTTPS.

	apache2_configuration_items:
	  - { option: "Listen",value: "{{ apache2_listen_port }}" }
Configuracion de apache. Afecta al fichero de configuracion global.

	apache2_modsecurity_enable: false
Por defecto no configura modsecurity. Si esta variable se pone a True en apache2_additional_packages hay que añadir mod_security.
	apache2_modsecurity_rules: []
Por defecto vacía. Reglas locales que queramos añadir en mod_security. Van como una única variable.

	apache2_mod_jk_enabled: false
Si se utiliza el mod_jk con balanceadores.

	apache2_mod_jk_log:
Ruta al fichero de log.

	apache2_mod_jk_loglevel: warn
Nivel de log.

	apache2_mod_jk_status_enable: false
Si se monta el status.

	apache2_mod_jk_status_url: /status
URL para acceder al estado.

	apache2_mod_jk_workers_file: workers.properties
Nombre del fichero de workers.

	apache2_mod_jk_loadbalancers: []
Balanceadores.
Ejemplo de formato
apache2_mod_jk_loadbalancers:
  - name: loadbalancer1
    directives: { sticky_session: true }
    servers:
      - name: server1
        directives: { host: localhost, port: 8009, type: ajp13, lbfactor: 1 }
      - name: server2
        directives: { host: localhost, port: 8009, type: ajp13, lbfactor: 1 }
  - name: loadbalancer2
    directives: { sticky_session: true }
    servers:
      - name: server3
        directives: { host: localhost, port: 8009, type: ajp13, lbfactor: 1 }
      - name: server4
        directives: { host: localhost, port: 8009, type: ajp13, lbfactor: 1 }

	apache2_mod_jk_redhat_version: 1.2.43
Versión mod_jk RedHat.

	apache2_mod_jk_redhat_install_location: /tmp
Ruta donde descargar mod_jk para compilación en plataforma RedHat.

Dependencies
------------

Ninguna.

Example Playbook
----------------

Un playbook básico de ejemplo sería el siguiente

	- hosts: servers
	  roles:
         - { role: "apache2", tags: ["apache"] }

License
-------

BSD

Author Information
------------------

Este rol ha sido creado por el Departamento de Sistemas de Xeridia (https://www.xeridia.com/)

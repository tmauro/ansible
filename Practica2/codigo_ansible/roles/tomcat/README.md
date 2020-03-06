tomcat
=========

Instalación entorno Tomcat 7.X. La versión de la misma se selecciona mediante la variable tomcat_version.

Requirements
------------

Ninguno.

Role Variables
--------------

	tomcat_version: 7.0.69
Versión a instalar.

	tomcat_is_java_required: True
Si se utiliza la dependencia del OpenJDK por defecto.

	session_cookie_domain_enabled: True
sessionCookieDomain activo

	tomcat_java_cmd: /usr/bin/java
Ejecutable JAVA.

	tomcat_java_opts:
Opciones JAVA. 

	tomcat_java_heap: 512M
Memoria utilizada por el proceso JAVA.

	tomcat_config_changes: []
Configuración adicional Tomcat, las opciones disponibles detalladas en la documentacion de la versión instalada.
Ejemplo de formato:
  - { option: "LANG", value: "en_US" }

	tomcat_hostname: "localhost"
hostname Tomcat.

	tomcat_server_port: "8005"
Puerto Tomcat.

	tomcat_catalina_port: "8080"
Puerto HTTP.

	tomcat_ajp_port: "8009"
Puerto AJP.

	tomcat_max_threads: "200"
Numero maximo de hilos.

	tomcat_webapps_dir: "webapps"
Carpeta donde se instalan aplicaciones.

	tomcat_catalina_configs: []
Configuración catalina.properties.
Ejemplo de formato:
  - { option: "prop1", value: "val1" }

	tomcat_global_naming_resources: []
GlobalNamingResource en la configuración server.xml.
Ejemplo de formato:
  - { auth: "Container", name: "jdbc/EmployeeDB", type: "javax.sql.DataSource", username: "dbusername", password: "dbpassword", driverClassName: "org.hsql.jdbcDriver", url: "jdbc:HypersonicSQL:database", maxActive: "8", maxIdle: "4" }

	tomcat_additional_jars: []
JARs adicionales para copiar en {{ tomcat_home }}/lib/.
Ejemplo de formato:
  - /tmp/jasypt-1.9.0.jar

	tomcat_jvm:
Por defecto no está definida. Definir si se quiere configurar balanceo.

Dependencies
------------

	open_jdk
Requiere Open JDK 8. Aunque si se configura la variable felix_is_java_required a False, no se instalará la dependencia y será necesaria la instalación de JAVA fuera del rol.

Example Playbook
----------------

Un playbook básico de ejemplo sería el siguiente

	- hosts: servers
      roles:
         - { role: "tomcat", tags: ["tomcat"] }

License
-------

BSD

Author Information
------------------

Este rol ha sido creado por el Departamento de Sistemas de Xeridia (https://www.xeridia.com/)
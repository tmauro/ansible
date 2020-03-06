# Changelog

Todos los cambios notables se documentaran en este archivo.

## [1.8.4] - 2019-10-17

- Ajuste en mod_proxy.

## [1.8.3] - 2019-10-04

- Ajuste en opciones de balanceo con mod_proxy.

## [1.8.1] - 2019-09-25

- Ajuste en protocolo de balanceo con mod_proxy.

## [1.8] - 2019-09-09

- Posibilidad de configurar balanceo con mod_proxy.

## [1.7.2] - 2018-12-26

- Posibilidad de configurar mod_limitIPConn.

## [1.7.1] - 2018-10-30

- Ajustes autoindex y versión de mod_jk.

## [1.7] - 2018-05-11

- Posibilidad de configurar mod_jk como balanceador.

## [1.6.6] - 2018-03-26

- Corregido un problema de configuración de modsecurity.

## [1.6.5] - 2018-03-26

- Añadida funcionalidad para poder redirigir a varios proxys.

## [1.6.4] - 2018-01-18

- Añadida la instrucción "no_log: true" para ocultar los certificados que se vuelcan al equipo.

## [1.6.3] - 2017-12-20

- Añadido soporte para configurar reglas en autoindex.conf.

## [1.6.2] - 2017-09-13

- Añadido soporte para configurar reglas en mod_security.

## [1.6] - 2017-09-05

- Se han nuevas funcionalidades para configurar vhosts. La más significativa soporte para ajp.

## [1.5] - 2017-02-23

- Se ha añadido la variable "apache2_configuration_items". Esta variable permite la posibilidad de modificar parametros de la configuración general de apache.

## [1.4] - 2017-02-09

- Corregido un problema de permisos en la carpeta de certificados del sistema.

## [1.3] - 2017-01-11

- Posibilidad de definir una sección de parámetros adicionales extra, previa a la configuración del Virtual host, mediante la variable "**vhosts**.previous_extra_parameters".

## [1.2] - 2016-12-28

- Posibilidad de instalar módulos Apache adicionales mediante la variables de configuración "apache2_additional_packages".

## [1.1] - 2016-12-28

- Nuevas opciones de configuración a la hora de crear los virtual hosts.
- Eliminada la compatibilidad con Apache 2.2.

## [1.0] - 2016-12-20

- Primera versión, basada en el playbook Galaxy https://galaxy.ansible.com/mrlesmithjr/apache2/ playbook original de INCIBE

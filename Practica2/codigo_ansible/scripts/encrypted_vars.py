#
#Este script cifra variables con anible-vault encrypt_string
#Creado por Xeridia

import subprocess

#var_id = cert_asist

def encrypt_vars():
    """Esta funcion encripta el contenido de la variable que se pide por teclado.
    
    La funcion pide por teclado el nombre de la variable,
    el contenido de la misma, que sera lo que se cifre asi como la clave de cifrado.
    Una vez recogidos los datos, cifra el contenido de la variable y asigna a una variable
    el resultado. Es necesario tener instalado Ansible 2.4.
    
    Variables:
		
    var_name: Nombre de la variable. El valor se introduce por teclado.

    var_value: Contenido de la variable, es el texto que se va a cifrar. El valor se introduce por teclado.
    
    var_id: Identificador de la variable. El valor se genera automaticamente, id_+var_name.
    
    result: Variable donde se recoge la cadema completa de la variable cifrada, el nombre de la variable y el identificador.


    """
    var_name = raw_input("Introduce el nombre de la variable -> ")
    var_value = raw_input("Introduce el contenido de la variable -> ")
    #var_id = raw_input("Introduce el indentificador de la variable -> ")
    var_id = "id_devops"
    print ("Introduce la clave de Vault.")
    while True:
        try:
            result = subprocess.check_output("echo -n "+var_value+" | ansible-vault encrypt_string --vault-id "+var_id+"@prompt --stdin-name "+var_name, shell=True)
            break
        except:
            print ("Las claves no coinciden, intentalo de nuevo...")
    return result


def print_menu():
    """ Esta funcion define el menu principal del script.

    Menu principal del script. Muestra las tres opciones que permite.

    1. Crear una variable cifrada y mostrarla por pantalla.

    2. Crear un fichero con formato .yml y varias variables cifradas.

    3. Interrumpir la ejecucion del script.

    """
    print ("1. Cifrar una variable y mostrarla por pantalla")
    print ("2. Crear un fichero YAML de variables cifradas")
    print ("3 o q. Salir")

loop=True
""" Esta variable define el primer bucle como true

"""


print ("***************************************************")
print ("** Este script cifra variables con Ansible-vault **")
print ("***************************************************")

print ("\n\n")

while loop:
    print_menu()
    choice_menu = raw_input ("Elige una opcion\n")
    if choice_menu=="1":
        print ("Vamos a cifrar una variable\n")
        var_cifra = encrypt_vars()
        print (var_cifra)
    elif choice_menu=="2":
        print ("Vamos a crear un fichero de variables cifradas\n")
        file_name = (raw_input("Introduce el nombre del fichero:(./file_encrypted_vars.yml)") or "file_encryped_vars.yml")
        print ("Generando fichero...")
        file = open(file_name,"w")
        file.write("---"+'\n')
        loop2=True
        while loop2:
            
            var_cifra = str(encrypt_vars())
            file.write(var_cifra)
            file.write('\n')
            other_var = raw_input("Quieres anadir otra variable cifrada al fichero? (s/n)\n")
            if other_var=="s":
                loop2=True
            elif other_var=="n":
                loop2=False
     
        print ("Guardando fichero...")
        file.write("...")
        file.close() 
    elif choice_menu=="3" or choice_menu=="q":
        print ("Hasta la proxima")
        loop=False
    else:
        raw_input ("Por favor, elige una opcion del menu\n")
        
""" Esta parte es el cuerpo principal del script.

Se muestra el menu llamando a la funcion correspondiente.

La primera opcion pide los datos por teclado y genera una variable cifrada llamando a la funcion encrypt_vars
y muestra por pantalla el resultado.

La segunda opcion permite generar varias variables y escribirlas en un fichero con formato yml

La tercera opcion simplemte interrumpe la ejecucion del script.


"""

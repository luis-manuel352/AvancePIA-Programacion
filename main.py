# Acceso de datos a la clase Contacto

import re

# Validador de expresiones regulares
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

# Expresiones regulares para cada campo.
telefonoRegEx="^[0-9]{10}$"
nombreRegEx=""
entidadValida=True

# Pregunta de teléfono que sea de 10 caracteres.
_telefono=""
telefono=0
datoValido=False
while True:
    _telefono=input("Teléfono:")
    if RegEx(_telefono,telefonoRegEx):
        telefono=int(_telefono)
        datoValido=True
        break
    else:
        print("Se requieren 10 dígitos como número")
        datoValido=False
    entidadValida=(entidadValida & datoValido)

# Tendras que ingresar tu nombre.
nombre=""
datoValido=False
while True:
    nombre=input("Nombre:")
    if RegEx(nombre,telefonoRegEx):
        datoValido=True
        break
    else:
        print("Se requiere nombre, apellido, no mayor a 30 catacteresLi.")
        datoValido=False
    entidadValida=(entidadValida & datoValido)
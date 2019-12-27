# -*- coding: utf-8 -*-
# Como funciona la variable __name__ y __main_

def functionA():
    print("ANTES DEL IMPORT")
    # AL MOMENTO DE HACER EL IMPORT EL MODULO SE EJECUTARA NUEVAMENTE COMO SI SE ESTUVIERA INICIANDO DE CERO EL SCRIPT
    from explication_main_ import functionB # SE IMPORTA EL MISMO MODULO
    print("DESPUÉS DEL IMPORT")
    functionB()
    print("DESPUÉS DE functionB")

def functionB():
    print("DESPUÉS DE functionB")

print("ANTES DEL IF MAIN")
if __name__ == "__main__":
    print("DESPUÉS DEL IF MAIN")
    functionA()
    print("DESPUÉS DE functionA")
print("FIN DE LA EJECUCIÓN")
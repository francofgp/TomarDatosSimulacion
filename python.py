from datetime import datetime
import os

arrivo = open("arrivo.txt", "a")
atencion = open("atencion.txt", "a")
cobro = open("cobro.txt", "a")

now = datetime.now()
now.strftime("%H:%M:%S")
estado = 1

while estado >= 1:

    print("1 = ingreso a fila")
    print("2 = ingreso al local")
    print("3 = salida del local")
    print("4 = cancelar")

    lectura_de_teclado = input("Choose a number")

    print(lectura_de_teclado)
    if lectura_de_teclado == "1" or lectura_de_teclado == 1:
        now = datetime.now()
        arrivo.write(now.strftime("%H:%M:%S") + os.linesep)
    if lectura_de_teclado == "2" or lectura_de_teclado == 2:
        now = datetime.now()
        atencion.write(now.strftime("%H:%M:%S") + os.linesep)
    if lectura_de_teclado == "3" or lectura_de_teclado == 3:
        now = datetime.now()
        cobro.write(now.strftime("%H:%M:%S") + os.linesep)
    if lectura_de_teclado == "4" or lectura_de_teclado == 4:
        estado = -5
        print(estado)


arrivo.close()
atencion.close()
cobro.close()
# pagina de donde saque
# https://www.programiz.com/python-programming/datetime/current-time

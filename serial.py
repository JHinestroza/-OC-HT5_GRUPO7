import serial, time

PuertoSerie = serial.Serial('COM6', 9600)

data = input("Introduce un valor:  ")
if (data == '1'):
    PuertoSerie.write(b'1')
    print(" LED Encendido ")
elif (data == '0'):
    PuertoSerie.write(b'0')
    print(" LED Apagado ")

PuertoSerie.close()
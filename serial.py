import serial, time

PuertoSerie = serial.Serial('COM%', 9600)

data = input("Introduce un valor: ")
if (data == '1'):
    PuertoSerie.write(b'1')
    print("LED Encendido")
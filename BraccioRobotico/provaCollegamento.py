import serial
import time

arduino = serial.Serial("COM3",9600)
time.sleep(1)

print("Invio...")

while True:
    msg = input("comando: ")
    arduino.write(msg.encode())
    time.sleep(.5)
import serial
import pygame
import time

porta = "COM3"
arduino = serial.Serial(porta,9600)
time.sleep(1)
print("Pronto...")
pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
print(joysticks)
while True:
    for event in pygame.event.get():
        if event.type==pygame.JOYBUTTONUP:
            pass
        if event.type==pygame.JOYBUTTONDOWN:
            btn = event.__dict__["button"]
            if btn == 0:
                msg = "a"
                arduino.write(msg.encode())
            if btn == 1:
                msg = "b"
                arduino.write(msg.encode())
            print(event)
        if event.type==pygame.JOYAXISMOTION:
            print(event)
            value = event.__dict__["value"]
            if value > 0:
                msg = "a"
            if value < 0:
                msg = "b"
            arduino.write(msg.encode())
        if event.type==pygame.JOYHATMOTION:
            print(event)

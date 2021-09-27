import os
import subprocess
from gpiozero import Button

button1 = Button(25)
button2 = Button(23)
button3 = Button(24)

reboot_statement = 'logger "System reboot initiatied by button press"; sudo reboot'
shutdown_statement = 'logger "System shutdown initiated by button press"; sudo shutdown now'

while True:
    if button1.is_pressed:
        os.system(reboot_statement)
    if button2.is_pressed:
        os.system('logger "Button 2 pressed, do nothing"')
    if button3.is_pressed:
        os.system(shutdown_statement)
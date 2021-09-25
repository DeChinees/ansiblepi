import os
import subprocess
from gpiozero import Button

button2 = Button(23)
button3 = Button(24)

reboot_statement = 'logger "System reboot initiatied by button press"; sudo reboot'
shutdown_statement = 'logger "System shutdown initiated by button press"; sudo shutdown now'

while True:
    if button2.is_pressed:
        os.system(reboot_statement)
    if button3.is_pressed:
        os.system(shutdown_statement)
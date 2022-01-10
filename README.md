*CircuitPython USB_CDC Ambilight Firmware*
---------------------
Control your LED strip over USB running the Adalight Prismatik Software.
Most compatabile Adalight protocol implementations are written for Arduino, but what if you wanted to control your LEDs with a CircuitPython MicroController?

Prismatik provides numerous quality-of-life features for LED control including screen grabbing, mood lights and API support. Being able to depart from the Arduino-centric setup helps lets additional users enjoy these features and leverage their CircuitPython boards.


*Quick Guide*
---------------------
- Copy the code.py file to your CIRCUITPYTHON drive
- Adjust code.py for your LED strip: such as # LEDs, or maybe youre not using NeoPixel but another driver?
- Allow for a soft-reboot of your board, or check requirements (enabling USB_CDC data serial will require a hard reboot)
- Run Prismatik's configuration wizard for "Adalight" on the correct COM port, baud rate 11520 should work fine
- Ensure the USB/LED/Software is all running, and enjoy your ambilight experience!



*Requirements*
---------------------
- A USB_CDC supported CircuitPython MicroController (Tested with Tiny2040)
- Any LED strip, you will have modify the code to drive your specific LED type
- A CIRCUITPYTHON/boot.py file with USB_CDC Data serial connection enabled
- Adalight Prismatik software, found at https://lightpack.tv/pages/downloads
"""CircuitPython Essentials NeoPixel example"""
import time
import board
import usb_cdc
import array
import neopixel


pixel_pin = board.GP1
num_pixels = 60
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=False)

if usb_cdc.data is None:
    print("Need to enable USB CDC serial data in boot.py!")
    while True:
        pass

def sendAck():
    usb_cdc.data.write(bytes("Ada\n",'utf-8'))
def setup():
    pixels.fill((100,0,0))
    pixels.show()
    time.sleep(0.3)
    pixels.fill((0,100,0))
    pixels.show()
    time.sleep(0.3)
    pixels.fill((0,0,100))
    pixels.show()
    time.sleep(0.3)
    pixels.fill((0,0,0))
    pixels.show()
    time.sleep(0.3)
    sendAck()

setup()
serialTimeout = 60000
usb_cdc.data.timeout = 60 / 1000
prefix = ['A','d','a']
lastAckTime = time.monotonic() * 1000
endian = "big"

while True:

    i = 0
    while i < len(prefix):
        c = usb_cdc.data.read()
        if(prefix[i] == chr(int.from_bytes(c, endian))):
            i += 1
            continue

        t = time.monotonic() * 1000
        if t - lastAckTime >= serialTimeout:
            # send ack if timeout is approaching and we have yet to receive magic
            sendAck()
            lastAckTime = t
        i = 0;

    hi=int.from_bytes(usb_cdc.data.read(), endian)
    lo=int.from_bytes(usb_cdc.data.read(), endian)
    chk=int.from_bytes(usb_cdc.data.read(), endian)

    # Cannot XOR bytes, checksum is converted to INT
    if (chk == (hi ^ lo ^ 0x55)):
        for i in range(0,num_pixels):
            r = int.from_bytes(usb_cdc.data.read(), endian)
            g = int.from_bytes(usb_cdc.data.read(), endian)
            b = int.from_bytes(usb_cdc.data.read(), endian)
            # neopixel requires INT for color tuple
            pixels[i] = (r,g,b)
        pixels.show()


import time
import board
import busio
import digitalio
import adafruit_ssd1306
from board import SCL, SDA
from PIL import Image, ImageDraw, ImageFont
from Adafruit_BBIO.SPI import SPI

G_ClearDisplay = [0b00000000,
                  0b00000000,
                  0b00000000,
                  0b00000000,
                  0b00000000,
                  0b00000000,
                  0b00000000,
                  0b00000000]

G_CharacterN = [0b00000000,
                0b01111110,
                0b00000100,
                0b00001000,
                0b00010000,
                0b00100000,
                0b01111110,
                0b00000000]

G_CharacterY = [0b00000000,
                0b00000000,
                0b01100000,
                0b00010000,
                0b00001110,
                0b00010000,
                0b01100000,
                0b00000000]

G_CharacterP = [0b00000000,
                0b00000000,
                0b00110000,
                0b01001000,
                0b01001000,
                0b01111110,
                0b00000000,
                0b00000000] 

def OLEDClickInit():
    Pin_DC = digitalio.DigitalInOut(board.P9_16)
    Pin_DC.direction = digitalio.Direction.OUTPUT
    Pin_DC.value = False
    Pin_RESET = digitalio.DigitalInOut(board.P9_23)
    Pin_RESET.direction = digitalio.Direction.OUTPUT
    Pin_RESET.value = True
    L_I2c = busio.I2C(SCL, SDA)
    return L_I2c

def LedMatrix8x8ClickInit():
    L_Spi1 = SPI(1,0)
    L_Spi1.mode = 0
    L_Spi1.writebytes([0x09, 0x00])
    L_Spi1.writebytes([0x0A, 0x01])
    L_Spi1.writebytes([0x0B, 0x07])
    L_Spi1.writebytes([0x0C, 0x01])
    return L_Spi1

def PrintDisplay(L_Spi1, DisplayList):
    L_Spi1.writebytes([0x01, DisplayList[0]])
    L_Spi1.writebytes([0x02, DisplayList[1]])
    L_Spi1.writebytes([0x03, DisplayList[2]])
    L_Spi1.writebytes([0x04, DisplayList[3]])
    L_Spi1.writebytes([0x05, DisplayList[4]])
    L_Spi1.writebytes([0x06, DisplayList[5]])
    L_Spi1.writebytes([0x07, DisplayList[6]])
    L_Spi1.writebytes([0x08, DisplayList[7]])

G_I2c = OLEDClickInit()
G_Spi1 = LedMatrix8x8ClickInit()

Display = adafruit_ssd1306.SSD1306_I2C(64, 32, G_I2c, addr=0x3C)
ImageObj = Image.new("1", (Display.width, Display.height))


Draw = ImageDraw.Draw(ImageObj)
Draw.rectangle((0, 0, Display.width - 1, Display.height - 1), outline=1, fill=0)

Font = ImageFont.load_default()

while True:
    Draw.text((10, 10), 'N', font=Font, fill=1)
    Display.image(ImageObj)
    Display.show()
    PrintDisplay(G_Spi1, G_CharacterN)
    time.sleep(1)
    Draw.text((20, 10), 'Y', font=Font, fill=1)
    Display.image(ImageObj)
    Display.show()
    PrintDisplay(G_Spi1, G_CharacterY)
    time.sleep(1)
    Draw.text((30, 10), 'P', font=Font, fill=1)
    Display.image(ImageObj)
    Display.show()
    PrintDisplay(G_Spi1, G_CharacterP)
    time.sleep(1)
    Draw.rectangle((5, 10, 40, 20), outline=0, fill=0)
    Display.image(ImageObj)
    Display.show()
    PrintDisplay(G_Spi1, G_ClearDisplay)
    time.sleep(1)

import board
import busio
import digitalio
import adafruit_ssd1306
from board import SCL, SDA
from PIL import Image, ImageDraw, ImageFont

def OLEDClickInit():
    Pin_DC = digitalio.DigitalInOut(board.P9_16)
    Pin_DC.direction = digitalio.Direction.OUTPUT
    Pin_DC.value = False
    Pin_RESET = digitalio.DigitalInOut(board.P9_23)
    Pin_RESET.direction = digitalio.Direction.OUTPUT
    Pin_RESET.value = True
    L_I2c = busio.I2C(SCL, SDA)
    return L_I2c
    
G_I2c = OLEDClickInit()
Display = adafruit_ssd1306.SSD1306_I2C(64, 32, G_I2c, addr=0x3C)
ImageObj = Image.new("1", (Display.width, Display.height))

Draw = ImageDraw.Draw(ImageObj)
Draw.rectangle((0, 0, Display.width - 1, Display.height - 1), outline=1, fill=0)

Font = ImageFont.load_default()
Text = "I Love NYP"
Draw.text((2, 10), Text, font=Font, fill=1)

Display.image(ImageObj)
Display.show()

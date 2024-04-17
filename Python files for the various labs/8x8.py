from Adafruit_BBIO.SPI import SPI
import time

G_SmileyHappyFace = [0b00111100,
                     0b01000010,
                     0b10101001,
                     0b10000101,
                     0b10000101,
                     0b10101001,
                     0b01000010,
                     0b00111100]

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
    

while True:
    G_Spi1 = LedMatrix8x8ClickInit()
    time.sleep(0.1)
    PrintDisplay(G_Spi1, G_SmileyHappyFace)
    time.sleep(0.1)

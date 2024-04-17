import time
import Adafruit_BBIO.PWM as PWM

PWM.start("P8_19", 75)

PWM.set_frequency("P8_19", 2000)
time.sleep(0.3)
PWM.set_frequency("P8_19", 2500)
time.sleep(0.3)
PWM.set_frequency("P8_19", 3000)
time.sleep(0.3)

PWM.stop("P8_19")

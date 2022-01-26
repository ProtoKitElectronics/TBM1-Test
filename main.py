from driver import Motors, IRSensorArray, Button, Buzzer
from time import sleep
from machine import Pin

led = Pin(25, Pin.OUT)
led.high()

# Hardware
motors = Motors()
motors.enable()
irsensors = IRSensorArray()
btn = Button()
bzz = Buzzer()

def main():
  sleep(1)
  
  # Beep at the beginning of the program
  bzz.on()
  sleep(0.1)
  bzz.off()
  
  has_turned = False
  while irsensors.read("front") > 18_000 or not has_turned:
    if irsensors.read("right") > 25_000 and not has_turned:
      sleep(0.1)
      motors.stop_break()
      sleep(0.2)
      motors.right()
      sleep(0.27)
      motors.stop_break()
      sleep(0.2)
      motors.forward()
      has_turned = True
    elif irsensors.read("right") < 4_000:
      motors.left()
      sleep(0.005)
      motors.forward()
    elif irsensors.read("left") < 4_700:
      motors.right()
      sleep(0.005)
      motors.forward()
    else:
      motors.forward()
    sleep(0.05)

  motors.stop_break()
  sleep(0.5)
  motors.stop_release()
  

# Run this program when the button is pressed
btn.setOnPress(main)

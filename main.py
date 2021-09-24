from driver import Motors, IRSensorArray, Button, Buzzer
from time import sleep

# Hardware
motors = Motors()
irsensors = IRSensorArray()
btn = Button()
bzz = Buzzer()

def main():
  # Beep at the beginning of the program
  bzz.on()
  sleep(0.3)
  bzz.off()
  
  # Start going forward
  motors.forward()

  # Wait until the front sensors are blocked
  while irsensors.read("front") > 3000:
    sleep(0.1)

  # Brake and release the motors  
  motors.stop_break()
  sleep(1)
  motors.stop_release()

# Run this program when the button is pressed
btn.setOnPress(main)
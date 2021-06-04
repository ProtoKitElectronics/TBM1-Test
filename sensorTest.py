from core.devices import IRSensor
from core import pins

def handler(pinObject):
  print( pinObject.value() )

for pin in pins.IR_SENSORS:
  IRSensor(pin).registerIRQHandler(handler)
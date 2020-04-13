import hub
from runtime import VirtualMachine

def smile():
     hub.display.show(hub.Image.SMILE)

# When program starts
async def on_start(vm, stack):
  # can ask if it is currently pressed, was pressed, how many times it has been pressed, and callback
  while True:
      if hub.button.left.is_pressed():
          hub.display.show(hub.Image.YES)
      elif hub.button.right.is_pressed():
          hub.display.show(hub.Image.NO)
          
  # possible buttons are left, center, right, connect

  hub.button.center.is_pressed()  # checks current state of center button

  hub.button.center.was_pressed()  # checks if the  center button has been pressed since last checked

  hub.button.center.presses()  # returns # presses since last call and rezeros
  smile()

     



def setup(rpc, system):
  vm = VirtualMachine(rpc, system, "")
  vm.register_on_start("", on_start)
  return vm

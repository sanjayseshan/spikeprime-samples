import hub, utime
from runtime import VirtualMachine

# When program starts
async def on_start(vm, stack):
  hub.led(255, 0, 0) # red  (r,g,b)
  hub.led(3) # blue   (colors 0 - 10)
  hub.led
  for i in range(11):
      hub.led(i)
      utime.sleep(1)

def setup(rpc, system):
  vm = VirtualMachine(rpc, system, "")
  vm.register_on_start("", on_start)
  return vm

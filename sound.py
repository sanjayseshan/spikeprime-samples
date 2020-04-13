import hub
from runtime import VirtualMachine

# When program starts
async def on_start(vm, stack):
  hub.sound.volume()
  hub.sound.volume(10)  # 0 - 10 
  hub.sound.beep()
  hub.sound.beep(2000, 500, 3)  # freq, time, waveform (sin,square,triangle, sawtooth)

def setup(rpc, system):
  vm = VirtualMachine(rpc, system, "")
  vm.register_on_start("", on_start)
  return vm

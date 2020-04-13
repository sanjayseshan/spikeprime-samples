import hub
from runtime import VirtualMachine

# When program starts
async def on_start(vm, stack):
  hub.battery.info()

def setup(rpc, system):
  vm = VirtualMachine(rpc, system, "")
  vm.register_on_start("", on_start)
  return vm

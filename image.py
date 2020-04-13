import hub, utime
from runtime import VirtualMachine

# When program starts
async def on_start(vm, stack):
  hub.display.show(hub.Image.HAPPY)

  image = hub.Image("90009:"
                        "09090:"
                        "00900:"
                        "09090:"
                        "90009")    

  hub.display.show(image)
  utime.sleep(1)

  # or

  image = hub.Image("90009\n09090\n00900\n09090\n90009")

  hub.display.show(image)
  utime.sleep(1)

  image = hub.Image(2, 2, b'\x08\x08\x08\x08')

  hub.display.show(image)
  utime.sleep(1)

  # all not working
  hub.Image.width()
  hub.Image.height()
  hub.Image.get_pixel(2,3)

  hub.Image.set_pixel(3,1,6)  # you cannot do this on built-in images

'''
built-in images
Image.HEART
Image.HEART_SMALL
Image.HAPPY
Image.SMILE
Image.SAD
Image.CONFUSED
Image.ANGRY
Image.ASLEEP
Image.SURPRISED
Image.SILLY
Image.FABULOUS
Image.MEH
Image.YES
Image.NO
Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, Image.CLOCK5, Image.CLOCK4, Image.CLOCK3, Image.CLOCK2, Image.CLOCK1
Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW
Image.TRIANGLE
Image.TRIANGLE_LEFT
Image.CHESSBOARD
Image.DIAMOND
Image.DIAMOND_SMALL
Image.SQUARE
Image.SQUARE_SMALL
Image.RABBIT
Image.COW
Image.MUSIC_CROTCHET
Image.MUSIC_QUAVER
Image.MUSIC_QUAVERS
Image.PITCHFORK
Image.XMAS
Image.PACMAN
Image.TARGET
Image.TSHIRT
Image.ROLLERSKATE
Image.DUCK
Image.HOUSE
Image.TORTOISE
Image.BUTTERFLY
Image.STICKFIGURE
Image.GHOST
Image.SWORD
Image.GIRAFFE
Image.SKULL
Image.UMBRELLA
Image.SNAKE
Finally, related collections of images have been grouped together:
Image.ALL_CLOCKS
Image.ALL_ARROWS
'''

def setup(rpc, system):
  vm = VirtualMachine(rpc, system, "")
  vm.register_on_start("", on_start)
  return vm

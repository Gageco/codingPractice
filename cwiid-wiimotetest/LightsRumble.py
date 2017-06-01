import cwiid
import time

print "press 1 + 2 now"
try:
    #attempt to connect wii remote
    wm = cwiid.Wiimote()
except RuntimeError:
    print "failed to find wiimote"

print "wiimote found"
x = 0
while x < 5:

###LED TESTS###
#So the led lights work on a sorta binary system from what I can figure. the leds all have their value then you can turn on
#which ever ones you want by adding up the value for those. So to turn on led 1 and 3 you would say wm.led = 5; or 1 + 4
#So to turn all of the leds on you would use wm.led = 15
    #led 1
    wm.led = 1
    time.sleep(.5)
    #turn off all lights
    wm.led = 0

    #led 2
    wm.led = 2
    time.sleep(.5)
    # turn off all lights
    wm.led = 0

    #led 3
    wm.led = 4
    time.sleep(.5)
    #turn off all lights
    wm.led = 0

    #led 4
    wm.led = 8
    time.sleep(.5)
    #turn off all lights
    wm.led = 0

    #all leds on
    wm.led = 15
    time.sleep(.5)
    #turn off all lights
    wm.led = 0

###RUMBLE TESTS###
#rumble is easy enough to change. only two possible values 1 and 0; True or False. Just dont foget to change it back to false
#when done or else its annoying
    wm.rumble = True
    time.sleep(3)
    wm.rumble = False
    x += 1
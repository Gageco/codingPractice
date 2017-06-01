import cwiid
import time

print "press 1 + 2 now"
try:
    #attempt to connect wii remote
    wm = cwiid.Wiimote()
except RuntimeError:
    print "failed to find wiimote"

print "wiimote found"
#set buttons to report when pressed
wm.rpt_mode = cwiid.RPT_BTN
wm.led = 0

def rumble():
    wm.rumble = True
    time.sleep(.1)
    wm.rumble = False

while True:

    if (wm.state['buttons'] & cwiid.BTN_DOWN):
        wm.led = wm.state['led'] - 1
        rumble()
    if (wm.state['buttons'] & cwiid.BTN_UP):
        wm.led = wm.state['led'] + 1
        rumble()
    if (wm.state['buttons'] & cwiid.BTN_A):
        rumble()
        print wm.state['led']
    if wm.state['led'] >= 16:
        wm.led = 15
    if wm.state['led'] <= 0:
        wm.led = 0

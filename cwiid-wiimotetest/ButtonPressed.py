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

while True:
    #check dif button n is being pressed
    if (wm.state['buttons'] & cwiid.BTN_1):
        print "1"

    if (wm.state['buttons'] & cwiid.BTN_2):
        print "2"

    if (wm.state['buttons'] & cwiid.BTN_A):
        print "A"

    if (wm.state['buttons'] & cwiid.BTN_B):
        print "B"

    if (wm.state['buttons'] & cwiid.BTN_PLUS):
        print "+"

    if (wm.state['buttons'] & cwiid.BTN_MINUS):
        print "-"

    if (wm.state['buttons'] & cwiid.BTN_LEFT):
        print "<"

    if (wm.state['buttons'] & cwiid.BTN_RIGHT):
        print ">"

    if (wm.state['buttons'] & cwiid.BTN_HOME):
        print "HOME"

    if (wm.state['buttons'] & cwiid.BTN_DOWN):
        print "\/"

    if (wm.state['buttons'] & cwiid.BTN_UP):
        print "UP"
    time.sleep(.5)
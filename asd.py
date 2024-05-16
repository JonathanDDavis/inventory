#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     26/09/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
inventory= {
    "key" : True,
}
if key in inventory:
    delayprint("You open up the door and leave.")
    exploring = False
else:
    delayprint("You leave the door alone.")

inventory["Key"] = "True"

for x, y in inventory.items():
    print(x, y)

if key in inventory:
    delayprint("You open up the door and leave.")
    exploring = False
else:
    delayprint("You leave the door alone.")

"""
with sample of python documentation
"""

from naoqi import *
import time
check = 0


# create python module
class MyModule(ALModule):
    """
    Python class MyModule test auto documentation:
    comment needed to create a new python module
    """

    def pythondatachanged(self, strVarName, value):
        """callback when data change"""
        print "datachanged", strVarName, " ", value, " ", strMessage
        global check
        check = 1

    def _pythonPrivateMethod(self, param1, param2, param3):
        global check


broker = ALBroker("pythonBroker", "10.0.252.184", 9999, "naoverdose.local", 9559)


# call method
try:
    pythonModule = MyModule("pythonModule")
    prox = ALProxy("ALMemory")
    # prox.insertData("val", 1)  # forbidden, data is optimized and doesn't manage callback
    prox.subscribeToEvent("FaceDetected", "pythonModule", "pythondatachanged")  # event is case sensitive !

except Exception as e:
    print "error"
    print e
    exit(1)

while (1):
    time.sleep(2)

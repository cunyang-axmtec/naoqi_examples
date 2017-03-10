from naoqi import ALProxy

try:
    # create proxy on ALMemory
    mem_proxy = ALProxy("ALMemory", "192.168.0.143", 9559)

    # insertData. Value can be int, float, list, string
    mem_proxy.insertData("myValueName1", "myValue1")

    # getData
    print "The value of myValueName1 is", mem_proxy.getData("myValueName1")

except RuntimeError as e:
    # catch exception
    print "error insert data", e

from naoqi import ALProxy

# create proxy on ALMemory
mem_proxy = ALProxy("ALMemory", "192.168.0.1", 9559)

# raise event. Data can be int, float, list, string
mem_proxy.raiseEvent("my event", "data")

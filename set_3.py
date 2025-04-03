eset = set()
eset.update(['nek'],['yash'],['parva'],['vraj'],['ved'])
print("set with added five name is:", eset)

if "nek" in eset:
    eset.remove("nek")
    eset.add("harshiv")
print(eset)

eset.remove("yash")
eset.remove("ved")
print(eset)

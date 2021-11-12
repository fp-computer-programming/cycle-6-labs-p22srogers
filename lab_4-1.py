# Author: SMR(AMDG) 11/12/21
colors=["red","blue","yellow","green"]
print(colors)
colors.extend(["purple","pink","black"])
print(colors.count("yellow"))

colors.insert(3,"turqoise")
print(colors)

colors.clear()
print(colors)

print(colors.count("red"))

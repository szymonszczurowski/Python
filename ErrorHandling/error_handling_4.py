try:
    x = 1 / 0
except:
    print("this is except")
    x = 1 / 0

print("this is after except")

 ################################################################

try:
    x = 1 / 0
except:
    print("this is except")
    x = 1 / 0
finally:
    print("this is after except")
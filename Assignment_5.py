## QUESTION 1
"""
def excption():
    return a/2

try:
    excption()
except ZeroDivisionError as ze:
    print("Divided by zero is not allowed")

except Exception as e:
    print("Any other idea please")

"""

## QUESTION 2

subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

for x in subjects:
    for y in verbs:
        for z in objects:
            print(x, y, z+'.')
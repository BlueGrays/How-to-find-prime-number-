control=True
number= int(input("Number Enter:"))
for i in range(2,number):
    if number%i ==0 :
        control= False
if control:
        print(True)
else:
        print(False)

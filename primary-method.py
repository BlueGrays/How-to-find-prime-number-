number = int(input("Number :"))
def control(number):
    i = 2 
    while i*i<=number: 
        if number%i==0 : 
            return False
        i +=1 
    else:
        return True
print(control(number))

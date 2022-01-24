def LCM(num1,num2):
    maximum=max(num1,num2)
    lcm=0
    while True:
         
        if  maximum%num1==0 and maximum%num2==0:
            break
        maximum=maximum+1
    return maximum   

def HCF(num1,num2):
    hcf=0
    minimum=min(num1,num2)
    for i in range(1,minimum+1):
        if num1%i==0 and num2%i==0:
               hcf=i
        
    return hcf    
         
if __name__ == '__main__':
    print("Here U can find LCM and HCF of two Numbers\n")
    inputno1=int(input("Enter 1st Number\n"))
    inputno2=int(input("Enter 2nd Number\n"))
    
    print(f"LCM of {inputno1} and {inputno2} is = ",LCM(inputno1,inputno2))
    print(f"HCF of {inputno1} and {inputno2} is = ",HCF(inputno1,inputno2))
    
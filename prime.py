import math
def prime(ascii_code_list):
    def isPrime(num):
        if(num==2 or num==3 or num==5 or num==7):	
            prime=True
        elif(num%2==0 or num%3==0 or num%5==0 or num%7==0):
            prime=False	
        elif(math.ceil(math.sqrt(num))-math.floor(math.sqrt(num))==0):
            prime=False
        else:	
            prime=True
        return(prime)
    

    prime_ascii_code = []
    for n in ascii_code_list:
        for i in range(n-1,1,-1):
            if(isPrime(i)):
                pnear=i 
                break
        snear=pnear+1 
        for i in range(n,n+pnear):
            if(isPrime(i)):
                snear=i
                break
        if((n-pnear)>(snear-n)):
            prime_ascii_code.append(snear)
        else:
            prime_ascii_code.append(pnear)
    return(prime_ascii_code)

string = input("Enter the string:-")
length_of_string = len(string)
create_list = []
ascii_code_list = []
count = 0
for c in string:
    create_list.append(c)
    ascii_code_list.append(ord(c))
print("Please enter the string = ")
print(create_list)
print("ASCII value  = ")
print(ascii_code_list)
prime_ascii_codes = prime(ascii_code_list)
print("Prime ASCII values = ")
print(prime_ascii_codes)
charcter_for_prime_ascii = []
for a in prime_ascii_codes:
    charcter_for_prime_ascii.append(chr(a))
print("")
print(charcter_for_prime_ascii)

import random
import string
print("WELCOME!To Password Generator\n\n")
length = int(input("Enter the length of the PASSWORD you want: "))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
number=string.digits
symbols=string.punctuation
all=lower+upper+number+symbols
temp=random.sample(all,length)
password="".join(temp)
print(password)


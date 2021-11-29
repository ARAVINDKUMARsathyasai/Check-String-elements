str = []
n = int(input("Enter the size of the string  "))
elemnt= input("Enter the character to searched  ")
count = 0
for x in range(n):
    str.append(input(""))
for x in str:
   if x.startswith(elemnt.upper()) or x.startswith(elemnt.lower()):
       count +=1
        
print(count)
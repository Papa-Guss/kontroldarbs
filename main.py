# a=[9,3,5,6]
# summa=sum(a)
# import numpy as np
# l = [1,2,3,4,5]
# print("Summa:",summa)
# print("Reizinājums:",np.prod(l))
# Vārds = 'Maksimka'[::-1]
# print(Vārds)
patskani=['ā','a','ū','u','ī','i','ē','e','o']
teikums=input("patskanis: ")
count = 0
for letter in teikums:
  if letter in patskani:
    count+= 1
print(count)
# 2. Write a program to greet all the person names stored in a list 'l' and which starts with S.
                #         L= ["Harry", "Soham", "Sachin", "Rahul"]
                # 3. Attempt problem 1 using while loop.
L= ["Harry", "Soham", "Sachin", "Rahul"]
i = 0
name = L[i]
while i < len(L):
    name = L[i]
    if name.startswith("S"):
        print(name)
    i = i + 1

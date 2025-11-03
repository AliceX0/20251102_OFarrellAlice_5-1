p = 2
q = 4

while p < q:
    print("Adios")
    r = 1
    while r < q:
        print("Adios")
        r = r + 1
    p = p + 1

#Outer loop prints Adios, resets the inner loop, and iterates p by 1
#Inner loop prints Adios 3 times for r = 1, 2, 3
#Outer loop runs 2 times for p = 2, 3
#Adios is printed a total of 8 times.
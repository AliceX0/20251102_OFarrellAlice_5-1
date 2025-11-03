j = 2
k = 5
n = 9

while j < k:
    m = 6
    while m < n:
        print ("Goodbye")
        m = m + 1
    j = j + 1

#Outer loop runs 3 times for j = 2, 3, 4
#Inner loop runs 3 times for m = 6, 7, 8
#At the end of the inner loop m is reset to 6 for the next iteration of the outer loop
#Goodbye is spammed 9 times.

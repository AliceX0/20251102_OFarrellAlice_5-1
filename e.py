j = 2
k = 5
m = 6
n = 9

while j < k:
    while m < n:
        print ("Hello")
        m = m + 1
    j = j + 1

#Inner loop runs 3 times while the conditions for both loops are true.
#Each time the inner loop runs Hello is printed.
#Once the condition of the inner loop is false, the outer loop increments j by 1.
#The outer loop has no output of its own.
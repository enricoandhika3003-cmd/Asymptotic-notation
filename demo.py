# O(1)
a = 2*3
print(a)


# O(n)
n = 4

for i in range(n+1):
    print(i+1)

# O(n^2)
for i in range(n+1):
    for j in range(n+1):
        print(i+1, j+1)

x = int(input("Enter value of X: "))
print(f"The value of X is {x}")

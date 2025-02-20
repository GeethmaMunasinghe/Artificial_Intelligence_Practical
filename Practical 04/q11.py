# Upper part of the pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Lower part of the pattern
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

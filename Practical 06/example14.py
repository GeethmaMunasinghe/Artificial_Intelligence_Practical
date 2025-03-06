def conjunction(p, q):
    return  p and q

def implication(p,q):
    return not p or q

# Print header
print("p     q     r    a")
print("-----------------")

# Iterate through truth values
for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            a = implication(conjunction(p,q) , r)  # Corrected function call
            print(f"{p}  {q}  {r}  {a}")  # Properly formatted output

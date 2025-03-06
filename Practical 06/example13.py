def conjunction(p, q):
    return  p and q

def disjunction(p,q):
    return p or q

# Print header
print("p     q     a")
print("-----------------")

# Iterate through truth values
for p in [True, False]:
    for q in [True, False]:
        a = disjunction(conjunction(p,q) , not q)  # Corrected function call
        print(f"{p}  {q}  {a}")  # Properly formatted output

def implication(p, q):
    return  (not p)or q # Returns True if both p and q are True

# Print header
print("p     q     a")
print("-----------------")

# Iterate through truth values
for p in [True, False]:
    for q in [True, False]:
        a = implication(p, q)  # Corrected function call
        print(f"{p}  {q}  {a}")  # Properly formatted output

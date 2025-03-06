def exclusive_disjunction(p, q):
    return (p and not q)or (not p and q)  # Returns True if both p and q are True

# Print header
print("p     q     a")
print("-----------------")

# Iterate through truth values
for p in [True, False]:
    for q in [True, False]:
        a = exclusive_disjunction(p, q)  # Corrected function call
        print(f"{p}  {q}  {a}")  # Properly formatted output

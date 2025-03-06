def bi_implication(p, q):
    return p==q

# Print header
print("p     q     a")
print("-----------------")

# Iterate through truth values
for p in [True, False]:
    for q in [True, False]:
        a = bi_implication(p, q)  # Corrected function call
        print(f"{p}  {q}  {a}")  # Properly formatted output

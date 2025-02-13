
rainbow=('violet','indigo','blue','green','yellow','orange','red')
other_colors=('white','black','pink')

nested_set=set((frozenset(rainbow),frozenset(other_colors)))

for sample_set in nested_set:
    print(sample_set)
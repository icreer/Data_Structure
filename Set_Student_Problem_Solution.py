'''
You need need to remove the intersection between two sets with out using the python .difference_update()
'''

def difference_update(s1,s2):
    # Solution
    save = set()
    for s in s1:
        if s not in s2:
            save.add(s)
    return save



s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

print(difference_update(s1,s2))
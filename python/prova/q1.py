def reps(lst):
    return filter(lambda x: lst.count(x) > 1, set(lst))

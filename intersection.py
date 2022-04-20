
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}


def same_elements():
    intersection = first_set.intersection(second_set)
    for x in intersection:
        first_set.remove(x)
        second_set.remove(x)

    print("First list Intersection ", first_set)
    print("Second list Intersection ", second_set)


same_elements()

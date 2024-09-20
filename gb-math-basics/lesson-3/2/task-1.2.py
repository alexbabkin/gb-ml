import math
def calc_vector_len(vect):
    len2 = 0
    for e in vect:
        len2 += e ** 2
    return math.sqrt(len2)

print(calc_vector_len((1, 2, 3)))
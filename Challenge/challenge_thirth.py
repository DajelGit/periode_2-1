import itertools

NO = 9
YES = 6

# VVD
# Dzz
# CDA
#  CU
# REG

# RUNS in about 17 ms on my machine
def test(output = False):
    arrays = itertools.permutations([1,2,3,4], 3)

    # print(list(arrays))

    for array in arrays:
        V, D, C = array

        interesting_R = V + D + C + 1
        interesting_E = (interesting_R + 6 + 1) % 10

        if interesting_R >= NO:
            continue

        arrays2 = itertools.permutations(list(set([1,2,3,4,5,6,7,8,9]) -set([interesting_R, interesting_E, NO]) - set(array)))
        for array2 in arrays2:
            
            R = interesting_R
            E = interesting_E
            A, U, G = array2     

            VVD = int("{}{}{}".format(V,V,D))
            D66 = int("{}{}{}".format(D,6,6))
            CDA = int("{}{}{}".format(C,D,A))
            CU = int("{}{}".format(C,U))
            REG = int("{}{}{}".format(R,E,G))

            if (VVD + D66 + CDA + CU == REG):
                if (output):
                    print("\n".join([str(VVD), str(D66), str(CDA), str(CU), str(REG)]), end="\n\n\n")


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=1) * 1000, "ms")


"""

carry 1
 carry 2
114
466
246
 27
----- +
853



carry 1
 carry 2
114
466
247
 26
----- +
853



carry 1
 carry 2
224
466
146
 17
----- +
853



carry 1
 carry 2
224
466
147
 16
----- +
853

"""







"""

112
266
328
 39
745


112
266
329
 38
745


113
366
432
 47
958


113
366
437
 42
958


221
166
417
 49
853


221
166
419
 47
853


331
166
412
 48
957


331
166
418
 42
957


332
266
128
 19
745


332
266
129
 18
745


441
166
217
 29
853


441
166
219
 27
853


441
166
312
 38
957


441
166
318
 32
957


443
366
132
 17
958


443
366
137
 12
958

"""
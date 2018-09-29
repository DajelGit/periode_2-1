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

        interesting = V + D + C + 1

        if interesting >= NO:
            continue

        arrays2 = itertools.permutations(list(set([1,2,3,4,5,6,7,8,9]) -set([interesting, NO]) - set(array)))
        for array2 in arrays2:
            
            R = interesting
            A, U, E, G = array2     

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
    print(timeit.timeit("test(True)", setup="from __main__ import test", number=1) * 1000, "ms")


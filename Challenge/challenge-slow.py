import itertools

# VVD
# Dzz
# CDA
#  CU
# REG

# RUNS in about 17 ms on my machine
def test():
    arrays = itertools.permutations([1,2,3,4,5,6,7,8])

    for array in arrays:
        V, D, C, A, U, R, E, G = array
                            
        VVD = int("{}{}{}".format(V,V,D))
        D66 = int("{}{}{}".format(D,6,6))
        CDA = int("{}{}{}".format(C,D,A))
        CU = int("{}{}".format(C,U))
        REG = int("{}{}{}".format(R,E,G))

        if (VVD + D66 + CDA + CU == REG):
            return True
            print("\n".join([str(VVD), str(D66), str(CDA), str(CU), str(REG)]), end="\n\n\n")


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=1))
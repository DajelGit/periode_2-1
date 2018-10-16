import itertools

NO = 6

# VVD
# Dzz
# CDA
#  CU
# REG

def test():
    arrays = itertools.permutations([1,2,3,4], 3)
    checks = 0

    # print(list(arrays))

    for array in arrays:
        V, D, C = array

        interesting_R = V + D + C + 1
        if interesting_R == NO or interesting_R > 9:
            continue

        interesting_E = (interesting_R + 6 + 1) % 10
        if interesting_E == NO :
            continue

        arrays2 = itertools.permutations(list(set([1,2,3,4,5,6,7,8,9]) -set([interesting_R, interesting_E, NO]) - set(array)))
        for array2 in arrays2:
            
            R = interesting_R
            E = interesting_E
            # print(array2, R, E, array)
            A, U, G = array2     

            VVD = V*100 + V*10 + D
            D66 = D*100 + 6*10 + 6
            CDA = C*100 + D*10 + A
            CU = C*10 + U
            REG = R*100 + E*10 + G

            if (VVD + D66 + CDA + CU == REG):
                # print("\n".join([str(VVD), str(D66), str(CDA), str(CU), str(REG)]), end="\n\n\n")
                checks += 1
    
    print(checks)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=1) * 1000, "ms")

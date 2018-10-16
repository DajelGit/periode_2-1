import itertools

NO = 6

def test(output = False):
    arrays = itertools.permutations([1,2,3,4], 3)
    checks_total = 0
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
            v = D + 6 + A + U

            checks_total += 1
            if (v % 10 == G and v > 20 ):
                checks += 1
                if output:
                    print(str([V, D, C, R, E, A, U, G]))
    
    print("checks done: ",checks_total, checks)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=1) * 1000, "ms")



"""

[1, 2, 3, 7, 4, 8, 9, 5] _
[1, 2, 3, 7, 4, 9, 8, 5] __
[1, 3, 4, 9, 5, 2, 7, 8]
[1, 3, 4, 9, 5, 7, 2, 8]
[2, 1, 4, 8, 5, 7, 9, 3] ____
[2, 1, 4, 8, 5, 9, 7, 3] ___
[3, 1, 4, 9, 5, 2, 8, 7]
[3, 1, 4, 9, 5, 8, 2, 7]
[3, 2, 1, 7, 4, 8, 9, 5] _____
[3, 2, 1, 7, 4, 9, 8, 5] ______
[4, 1, 2, 8, 5, 7, 9, 3] ________
[4, 1, 2, 8, 5, 9, 7, 3] _______
[4, 1, 3, 9, 5, 2, 8, 7]
[4, 1, 3, 9, 5, 8, 2, 7]
[4, 3, 1, 9, 5, 2, 7, 8]
[4, 3, 1, 9, 5, 7, 2, 8]

[1, 2, 3, 7, 4, 8, 9, 5] _
[1, 2, 3, 7, 4, 9, 8, 5] __
[2, 1, 4, 8, 5, 9, 7, 3] ___
[2, 1, 4, 8, 5, 7, 9, 3] ____
[3, 2, 1, 7, 4, 8, 9, 5] _____
[3, 2, 1, 7, 4, 9, 8, 5] ______
[4, 1, 2, 8, 5, 9, 7, 3] _______
[4, 1, 2, 8, 5, 7, 9, 3] ________

"""
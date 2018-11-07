#include <stdio.h>
#define IGNORE  9


int main() {
    int count = 0;

    for(int V=1; V <= 9 && V != IGNORE; V++) { // LOOP Unique V
        for(int D=1; D <= 9 && D != IGNORE; D++) { // LOOP Unique D
            if (V == D) continue;
            for(int C=1; C <= 9 && C != IGNORE; C++) { // LOOP Unique C
                if (V == C) continue;
                if (D == C) continue;

                if (V + D + C + 1 > 9) continue;

                int R = V + D + C + 1; // CALC R
                for(int E=(V + 6 + D + C +1) % 10; E <= (V + 6 + D + C +2) % 10; E++) { // LOOP Unique E
                    for(int A=1; A <= 9 && A != IGNORE; A++) { // LOOP Unique A
                        if (V == A) continue;
                        if (C == A) continue;
                        if (R == A) continue;
                        if (D == A) continue;

                        for(int U=1; U <= 9 && U != IGNORE; U++) { // LOOP Unique U
                            if (V == U) continue;
                            if (C == U) continue;
                            if (R == U) continue;
                            if (D == U) continue;
                            if (A == U) continue;

                            for(int G=1; G <= 9 && G != IGNORE; G++) { // LOOP Unique G
                                if (V == G) continue;
                                if (C == G) continue;
                                if (R == G) continue;
                                if (D == G) continue;
                                if (A == G) continue;
                                if (U == G) continue;

                                int value = (D + 6 + A + U);
                                if (value % 10 == G) {
                                    if ((V + 6 + D + C + (value / 10)) % 10 == E) {
                                        count++;
                                        // printf("%d%d%d + %d66 + %d%d%d + %d%d == %d%d%d \t", V,V,D, D, C,D,A, C,U, R,E,G);
                                        // printf("%d,%d,%d,%d,%d,%d,%d,%d\n", V,D,C,R,E,A,U,G);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    printf("%d", count);
}
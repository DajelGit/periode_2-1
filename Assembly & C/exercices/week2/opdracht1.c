#include <stdio.h>

int main() {

    int a = 3;
    int b = 7;
    int c;

    do {
        a = a-1;
        b = b-1;
        c = a;
        if (b == 6) {
            b = b-a;
        } else {
            if (b == 3) {
                a = a-1;
            }
        }
    } while (a > 0);

    printf("%d", a);
    printf("%d", b);
    printf("%d", c);
}
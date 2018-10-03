# week 1

1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111

## Opdracht 1
1. AB base16 = 10*16+11 = 171 base10
2. 7ED base16 = 7*16^2 + 14*16 + 13 = 2029  
3. 101010111 base2 = 256+64+16+4+2+1 = 343
4. 777 base8 = 7*8^2+7*8+7 = 511

## Opdracht 2
1. FE7 base16 = 1111 1110 0111
2. 5347 base8 = 101 011 100 111 
3. 99 base10 = 0110 0011

## Opdracht 3
1. 1110 1011 1001 base2 = EB9 base16
2. 7777 base8 = FF
3. 95 base10 = 0101 1111 base2 = 5F base16
4. 1024 base10 = 0100 0000 0000 base2 = 400 base16

## Opdracht 4
TODO

## Opdracht 5
1. 01110000 base2 + 10000001 base2 = 11110001 base2
2. 00110011 base2 + 10000001 base2 = 10110100 base2
3. 52F0 base16 + 4AA3 base16 = 9D93 base16
4. D38A base16 + 11D3 base16 = E55D base16
5. 10000001 base2 + 01110000 base2 = 11110001 base2
6. DAF5 base16 + 0342 base16 = DE37 base16
7. 417 base8 + 154 base8 = 573 base8
8. CD97 base16 + A1D3 base16 = 16F6A base16

## Opdracht 6
10110 * 1011 
22 * 11 = 242
242 base10 = 11110011 base2

0   1   1  1  1  0 0 1 1  
256 128 64 32 16 8 4 2 1

## Opdracht 7
1. 5 bit betekent 2^5 = 32 verschillende binaire waardes
2. 9 bit betekent 2^9 = 512 verschillende binaire waardes
3. 5 bits omdat het in 4 bits net niet past
4. 4 bits 

## opdracht 8
0000    0       0       0
0001    1       1       1
0010    2       2       2
0011    3       3       3
0100    4       4       4
0101    5       5       5
0110    6       6       6
0111    7       7       7
1000    8      -7      -8
1001    9      -6      -7
1010    10     -5      -6
1011    11     -4      -5
1100    12     -3      -4
1101    13     -2      -3
1110    14     -1      -2
1111    15     -0      -1

## opdracht 9
-3 + 4 = 1

-3 = 1101
4 =  0100 +
1 =  0001


2 - 5 = -3

2 =  0010
-5 = 1011 +
-3 = 1101


-5 - 2 = -7

-5 = 1011 
-2 = 1110 +
-7 = 1001


-6 - 3 = (-9)  7

-6 = 1010
-3 = 1101 +
7  = 0111


## opdracht 10
25 - 26 = -1

25 =  0001 1001
-26 = 1110 0110 +
-1 =  1111 1111


33 - 111 = 78

33 =   0000 0000
-111 = 0000 0000
78 =   


-64 -64 = -128

-64 =   1100 0000
-64 =   1100 0000 +
-128 =  1000 0000


-64 -65 = (-129)  127

-64 =  1100 0000
-65 =  1011 1111
127 =  0111 1111



## opdracht 11
1. 0111 = 7 en 1111 = -8
2. Java kent alleen maar signed two's compplement integers. In C kan je aangeven wat voor soort integer je wil hebben.
3. Nee Java kent geen unsigned integer.
4. 0111 1111 1111 1111 1111 1111 1111 = 2147483647    en 1111 1111 1111 1111 1111 1111 1111 = -2147483648
5. int i = 0xfe000000;   // -33554432



## opdracht 12
1. Dat je vanaf daar de getallen een lagere waarde hebben dan 1
2. Het heeft in het binaire stelsel de zelfde betekennis als in het 10-tallig stelsel.
3. 0,1111 base 2 = 15/16 base 10 = 0,9375 base 10
4. 101,101 base 2 = 5 5/8 base 10 = 5,625 base 10



## opdracht 13
1 bit sign 
8 bits Exponent
23 bits Mantisse
--------- +
32 bits IEEE float point formaat

0x42E48000

0100 0010 1110 0100 1000 0000 0000 0000
||        |                           |
S   Exp.            Mantisse

1000 0101 base 2  =>   -5 base 10
110 0100 1000 0000 0000 0000 base 2 = 6586368 base 10

0,6586368 * 10^-5 = 0,000006586368

TODO

## opdracht 14
TODO
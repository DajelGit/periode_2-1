Opdracht 1

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



A

A: 0; B: 3; C: 1

(Tussenstappen:
A: 3; B: 7; C: 0
If
A: 2; B: 4; C: 2

A: 2; B: 4; C: 2
Elif
A: 0; B: 3; C: 1
)

B

.def a=r16
.def b=r17
.def c=r18

start:                  ; Initialize de variabelen
    ldi a, 0x03
    ldi b, 0x07
    ldi c, 0x00

loop:                   ; De main loop
    dec a
    dec b
    mov c, a
    cpi b, 6
    breq ifbeq6
    cpi b, 3
    breq ifbeq3

ifbeq6:                 ; De eerste IF
    sub b, a
    rjmp loopend

ifbeq3:                 ; De tweede IF
    dec a
    rjmp loopend

loopend:                ; Het einde van de loop
    cpi a, 0
    breq end
    rjmp loop

end:                   ; Infinite loop
    rjmp end




Opdracht 3

.def a=r16
.def temp=r17

ldi a, 0x01
ldi xl, low(0x100)
ldi xh, high(0x100)
st x+, a

loop:
    ldi temp, 0x03
    mul a, temp
    mov temp, r1
    mov a, r0
    cpi temp, 0x01
    brpl end
    st x+, a
    dec a
    st x+, a
    rjmp loop

end:
    rjmp end




Opdracht 5

A

.include "m328Pdef.inc"

.ORG 0x0000    ; the next instruction has to be written to

start:
    ldi r16, low(RAMEND)
    out SPL, r16
    ldi r16, high(RAMEND)
    out SPH, r16


    ldi r16, 0xFF           ; Pins B to output
    out DDRB, r16

    ldi r16, 0x00           ; Pins D to input
    out DDRD, r16

loop:
    in r16, PinD
    out PortB, r16

    rjmp loop               ; jump to loop

B

.include "m328Pdef.inc"

.def temp=r16
.def state=r17

start:
    ldi temp, low(RAMEND)
    out SPL, temp
    ldi temp, high(RAMEND)
    out SPH, temp

    ; Pins B to output
    ldi temp, 0xFF
    out DDRB, temp

    ; Pins D to input
    ldi temp, 0x00
    out DDRD, temp

    ldi state, 0xFF

disable:
    ldi temp, 0x00
    out PortB, temp

loopoff:
    sbic PinD, 2
    rjmp enable
    rjmp loopoff

enable:
    ldi temp, 0xFF
    out PortB, temp

loopon:
    sbic PinD, 3
    rjmp disable
    rjmp loopon








OCR1A = 0b0000111110100000      ; De Maximale waarde van de timer
TCCR1B = 0b00001010             ; Prescaler van 8   CTC Timer modus wat betekent Clear Timer on Compare math
TIMSK1= 0b00000010              ; Compare A Math Interrupt Enable
;
; AssemblerApplication.asm
;
; Created: 18/09/2018 11:09:45
; Gemaakt door : Timo Strating 368678
;				 Remi Reuvenkamp


; Opdarcht 1
;;; A
SET Rd		; Set bits in Register
CBR Rd, K	; Clear Bit Register

;;; B
NEG Rd		; Vervangt de waarde in Rd met de two’s complements versie ervan.

;;; C
BR__		; Alle Branch commando's beginnen met BR
			; bij conditionele sprongen staat bij de Operation “if...” in pseudo C-achtige code.

;;; D
IN p 
OUT p		; Deze instructies dienen voor het instellen van een poort als input of output 

;;; E
; we kunnen tegelijkertijd fetchen, decoden en uitvoeren dus het neemt maar 4 cycles in beslag.

;;; F
RJMP		; is relatief vanaf het huidige address waardoor het lukt binnen 16 bits maar waardoor je niet door het volledige geheugen kan springen
JMP			; is relatief vanaf het begin van het geheugen hiervoor is wel een volledig 16 bits addres nodig waardoor die commando 32 bits nodig heeft

;;; G
ADC			; Add is met carry flag
ADD			; Add

;;; H
; ja met 2 getallen die binair alleen maar bestaat uit 1-nen kan ja als je ze plus elkaar doet niet meer getallen nodig hebben dan je kwijt kan met 1 extra carry



; Opdarcht 2
; Logical Shift left
LSL R..			; 0000 11dd dddd dddd  
ADD R.. R..		; 0000 11rd dddd rrrr
; Logical Shift left is een add met zich zelf



; Opdarcht 3
;;; A
In de huidige working directory

;;; B 
PORTB: 0x05
DDRB: 0x04
PINB: 0x03

;;; C
XH: de eerste register van het X (X bestaat uit 2 registers). Hierin staan de meest significante bit.
XL: het tweede register van X. Hierin staan de minst significante bits.

;;; D
Startadres: 0x0100
Grootte: 2048


; Opdarcht 4
;;; A
ldi r16,~0xf0		; r16 = 0b 00001111

;;; B
.equ a = 5			; a = 0b 0000 0101
.equ b = 0xff16		; b = 0b 1111 1111 0001 0110
ldi r18,low(a|b)	; r18 = 0001 0111

;;; C
.equ a = 5			; a = 0b 0000 0101
.equ b = 0xff		; b = 0b 1111 1111
ldi r18, a^b		; r18 = 0b 1111 1010

;;; D
ldi r16, (1<<5)|(1<<7)	; r16 = 1010 0000
out PORTB, r16			; PORTB = r16
						; PORTB wordt: 1010 0000

;;; E
ldi r16, ~(1<<PB3)		; r16 = 1111 0111

;;; F
ldi r16,low(RAMEND)		; r16 = low( 0x08ff ) = 1111 1111
out SPL,r16				; SPL   0x3d = r16
ldi r16,high(RAMEND)	; r16 = high( 0x08ff ) = 0000 1000
out SPH,r16				; SPH   0x3e = r16

RAMEND: 0x08ff: 2303

0000 1000 1111 1111
Naar SPL wordt 0000 1000 geschreven
Naar SPH wordt 1111 1111 geschreven



; Opdarcht 5
ldi r16, 0xAA			; r16 = 0b 10101010
ldi r17, 0x12			; r17 = 0b 00010010

;;; A
neg r16			; Change to two's complement   r16 = 0b 01010110
swap r17		; Swap Nibbels  r17 = 0b 0010 0001 = 0x21
sbr r16, 3		; Set Bits in Register r16 = 0b 10101011
dec r17			; Decrement  r17 -= 1    r17 = 0b 00010001
ori r16, 0xF0	; Logical Or with immediate  wat betekent OR with constante in het register r16

;;; B
mul r16, r17	; Multiply heeft mogelijk meerdere carry's nodig dus daarom wordt het resultaat in registers r0 en r1 geplaatsts



; Opdarcht 9
.org 0																								; Het zegd tegen de assembler dat wat hierna komt bij adress 0 begind
	ldi zh, high(ASCII_TABLE << 1) ;define Z-pointer		; REGISTER			; Inmediate			; Laad het getal 0x00 in Register R31
	ldi zl, low(ASCII_TABLE << 1)							; REGISTER			; Inmediate			; Laad het getal 0x28 in Register R30
	ldi r16, 0x0											; REGISTER			; Inmediate			; Laad het getal 0x0 in Register R16. We moeten dit doen omdat we een register alleen maar kunnen gbruiken om een port te zetten
	out DDRC, r16 ;PORTC input								; I/O				; Direct			; Zet alle pins van PORTC als output
	ldi r16, 0xff											; REGISTER			; Inmediate			; Laad het getal 0x0 in Register R16. Zie 2 naar boven.
	out DDRD, r16 ;PORTD output								; I/O				; Direct			; Zet alle pins van PORTD als output
BEGIN:																								; Dit is een Label
	in r16, PINC											; I/O				; Direct			; Zet alle de waarde van de pins van PinC naar register R16
	andi r16, 0b00000111 ;mask upper 5 bits					; REGISTER			; Inmediate			; Doe een AND op binair niveau met het getal 5. Wat als gevolg heeft dat 0111 als een masker werkt en alleen de laatste 3 eenen over neemt van R16
	add zl, r16												; REGISTER			; Direct			; Voeg R16 toe aan R30
	lpm r17, z												; SRAM				; Indirect			; Het laad R31 in R17 als de waarde van R30 deelbaar is door 2 zonder rest anders laad het R30 in R17
	out PORTD, r17											; I/O				; Direct			; Het resultaat wordt daarna naar de output geschreven
	rjmp BEGIN												; SRAM									; Spring weer terug naar het label BEGIN:
 
.org 20														; SRAM									; Het zegd tegen de assembler dat wat hierna komt bij adress 20 begind
ASCII_TABLE: .DB '0','1','2','3','4','5','6','7'			; SRAM									; De ASCII tekens 0 1 2 3 4 5 6 7 worden in het code segment geladen

;;; A
;LPM R.., Z; Load Program Memory. Het laad 

;;; B 
; Zie code

;;; C
; Zie code
; Het convert een binair getal van PORTC naar Ascii en zet dat op PORTD




; Opdarcht 10
.dseg
	.org SRAM_START 

dest: 
	.byte 20						; Reserveer 20 bytes voor Hello world
 
.cseg
	rjmp start                      ; De eerste instructie is om naar het label start te springen
 
src: 
	.db "hello world !"             ; De string die we gaan kopieren van het code segment naar het data segment
	.equ length=13                  ; De lengte van de sting "hello world !" 
	.def temp = r0                  ; Dit is het tijdelijke register waar de data komt te staan tijdens het kopieren
	.def counter = r17              ; De teller die bij houd hoeveel tekens wij van de string al hebben gekopieerd 
 
start: 
	ldi zh,high(2*src)              ; Z-pointer wijst naar de source maar gaat x2 of to wel << 1 omdat lpm naar de aller eerste bit kijkt om te behalen of hij het hoge of het lage gedeelte van de Z pointer moet hebben
	ldi zl,low(2*src)               ; ...
	ldi xh,high(dest)               ; X-pointer wijst naar de desination
	ldi xl,low(dest)                ; ...
	clr counter                     ; 

loop:      
	lpm      						; Laad waar de X pointer naar point
	inc zl      					; Verhoog de Z pointer met 1
	st x+,temp            			; Sla de Z pointer op
	inc counter            			; Verhoog De counter met 1 om aan het volgende char te beginnen
	cpi counter, length            	; Vergelijk of we al op het eind van de sting zijn
	brlt loop       				; Zolang als er nog meer chars zijn die we kunnnen kopieren dan beginnen we weer opnieuw met het kopieren van een char

end:
	rjmp end						; infinite loop




;;; B	
; Het geen wat in het code segment staat wordt naar het datasegment overgezet. 
; In dit geval wordt "Hello World" vanuit het data segment overgezet naar het code segment.

;;; C
; LMP pakt de Z pointer en plaatst het in ....  <<< TODO >>>
; De Z pointer is alleen al 2 registers lang dus 16 bits wat LMP daarom doet is dat het kijkt naar de minst significante bit. 
; Deze bit bepaald of het naar Zl (het rigister van Z waar de minst waardevolle bits in staan) of Zh (het andere register van Z) gaan kijken.

;;; D
https://imgur.com/oXkW8yZ

;;; E
.dseg 
.db "hello world !" 

; Bovenstaande regel zou niet werken omdat de datasegment tijdens het resetten leeggehaald zou worden. 
; De assembler zou dus de string opslplitsen in de verschillende geheugencellen maar tijdens de reset wordt daarna alles weer overschreven

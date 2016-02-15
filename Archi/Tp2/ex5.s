.global _start
_start: ldrb  r0, a
  ldrb r1, b
  ldrb r2, c
  cmp r0,r1 @compare a et b
  bge cmp2
  mov  r0, r1 @si a < b

cmp2:cmp r0,r2 @compare max(a,b) et c
  bge fin
  mov r0,r2

fin: str  r0, max


exit:	b exit
a : .byte 5
b : .byte 3
c : .byte 4
max : .int -1

.global _start
_start:
  adr r0, tab @adresse du tableau
  add  r1, r0, #40 @fin tableau
  mov r2,#1 @nb occurences
  mov r3,#0 @nb occurences max
  ldr  r4, [r0],#4 @ contient la derniere valeur analysee

boucle: cmp r0,r1 @arret
  bge fin
  ldr r5,[r0],#4 @nouvelle valeur
  cmp r4, r5
  mov r4,r5
  bne notequal
  add  r2, r2, #1
  b boucle

notequal:cmp r2, r3
  ble init
  mov r3,r2
init:mov r2,#1
  b boucle

fin:cmp r2,r3
  ble exit
  mov r3,r2

exit: b exit
tab: .int 1,9,5,5,5,5,5,5,3,3

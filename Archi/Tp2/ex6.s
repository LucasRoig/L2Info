.global _start
_start:adr r0,tab @pointeur tableau
  add  r1, r0, #400 @pointeur fin tableau
  mov r2,#0 @premier terme
  str  r2, [r0],#4 @store premier terme

boucle : add  r3,r2,#1 @dernier terme + 1
  add  r2, r2, r3 @ terme suivant
  str r2,[r0],#4 @store terme suivant
  cmp r0, r1
  ble boucle
exit: b exit
tab: .fill 100,4

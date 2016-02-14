.global _start
_start:adr r1,tab
	adr r2,tab
	add r2,r2,#40
	mov r3,#0
	b sommer

sommer: ldr r4,[r1],#4
	add r3,r3,r4
	cmp r1,r2
	blt sommer
	b fin
fin :	adr r1,somme
	str r3,[r1]

tab : .int 1,1,1,1,1,1,1,1,1,1,1
somme : .int -1

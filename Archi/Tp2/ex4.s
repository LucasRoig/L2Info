.global _start
_start:	adr r0,tab 	@Pointeur tableau
	mov r1,r0
	add r1,r1,#80 	@Pointeur fin
	mov r2,#7	@Premier terme
	str r2,[r0],#4

comp:	cmp r0,r1	@Fin du tableau?
	bgt exit
	mov r3,r2,lsl #31
	cmp r3,#0	@Est Pair ?
	beq pair
	b impair

pair:	mov r2,r2,lsr #1
	str r2,[r0],#4
	b comp

impair: mov r3, #3
	mul r2,r3,r2
	add r2,r2,#1
	str r2,[r0],#4
	b comp

exit:	b exit

tab: .fill 20,4

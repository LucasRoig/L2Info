.global _start
_start:	adr r0,tab
comp:	ldrb r1,[r0]
	cmp r1,#0
	beq exit
	b tolow	

tolow:	add r1,r1,#0x20
	strb r1,[r0],#1
	b comp	

exit:	b	exit
	

tab: .asciz "ARM"



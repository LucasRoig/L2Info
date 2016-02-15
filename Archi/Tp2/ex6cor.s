@ TP2 : exercice6 : nombres triangulaires
.global _start
_start:
	mov 	r1,#1 @ r1 contient n
	mov 	r2,#0 @ r2 contient Tn
	adr	 r3,tab
debut:	cmp	r1,#100
	beq 	exit
	add	r2,r2,r1
	str	r2,[r3],#4
	add	r1,r1,#1
	b	debut

exit:	b exit

tab:	.fill	100,4,0

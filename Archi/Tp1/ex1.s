.global	_start
_start:	sub	r2,r1,r0
	add	r2,r1,r0,LSL #5
	add	r0,r0,#130
	mov	r0,#3	@ r0=3
	mov 	r1,#1	@ r1=1
	add	r0,r0,#3	@r0 <- r0 +3
	sub	r2,r1,r0	@r0 <- r0 - r0
	adr	r3,tab1	@r3 <- tab3
exit: 	b	exit	@ boucle infinie

tab1:	.int 2,3,-1
tab2:	.fill 4,2,12
chaine:	.asciz	"bonjour"
tab3:	.byte 13,-3,'A'

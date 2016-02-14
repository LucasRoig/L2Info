.global _start
_start:	adr r0,tab 	@Pointeur tableau
	mov r1,r0	@Fin du tableau
	add r1,r1,#40
	ldr r2,[r0],#4	@Minimum
	
boucle: ldr r3,[r0],#4	@Terme suivant
	cmp r3,r2
	blt echange
	cmp r0,r1
	ble boucle
	b exit	

echange: mov r2,r3
	cmp r0,r1
	ble boucle


exit:	b exit

tab: .int 10,5,1,2,3,-1,-5,4,-9,-3

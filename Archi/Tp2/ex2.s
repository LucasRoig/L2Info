.global _start
_start:	adr r0,tab 	@pointeur sur le tableau
	adr r1,tab
	add r1,r1,#400 	@pointeur fin du tableau
	mov r2,#2	@premier terme
	str r2,[r0],#4

boucle: add r2,r2,r2	
	sub r2,r2,#1
	str r2,[r0],#4	@Nouveau Terme
	cmp r0,r1
	ble boucle
	
	
exit:	b exit

tab: .fill 100,4



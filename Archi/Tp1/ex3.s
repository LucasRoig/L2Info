.global _start
_start: adr r0,var1
	ldr r1,[r0]
	adr r0,var2
	ldr r2,[r0]
	add r1,r1,r2
	adr r0,res
	str r1,[r0]
exit:	b	exit

var1:	.int	9
var2:	.int	18
res:	.int	-1

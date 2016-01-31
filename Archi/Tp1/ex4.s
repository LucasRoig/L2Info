.global _start
_start: adr	r0,tab
	ldr	r1,[r0,#4]
	str	r1,[r0,#8]
	ldr	r1,[r0]
	str	r1,[r0,#4]
	mov	r1,#0
	str	r1,[r0]	

exit:	b	exit

tab: .int 1,2,3



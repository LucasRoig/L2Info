.global _start
_start:	adr r0, tab
	ldrb r1,[r0]
	ldrb r2,[r0,#3]
	strb r1,[r0,#3]
	strb r2,[r0]	
exit:	b	exit

tab: .byte 0xA0,0xD0,0x74,0x24



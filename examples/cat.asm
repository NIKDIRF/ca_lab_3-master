.data:
    num tmp 0
.text:

loop: in tmp
    out_char tmp
	jmp loop
end: hlt
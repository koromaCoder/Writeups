from pwn import *
gdbcmd = "b *0x0806cc02"
target = gdb.debug("./feedme", gdbscript = gdbcmd)

target.sendline(b"A"*50)

target.interactive()
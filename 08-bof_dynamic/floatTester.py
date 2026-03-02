def float_to_ieee(value):
	mant = 0x007fffff & value
	exp = (0x7f800000 & value) >> 23
	sign1 = 0x80000000 & value >> 31
	expon = 2 ** (exp - 127)
	dec = 0.0
	for i in range(23):
		x = 0x400000 & mant
		mant = mant << 1
		thing = x >> (22 - i) 
		if( thing != 0):
			cloat = 2.0 ** -float(i)
		else:
			continue
		print('{0:.20}'.format(cloat))
		dec += cloat
		
	dec *=  expon
	return '{0:.20}'.format(dec)

puts_plt = 0x00000000004008d0
puts_got = 0x0000000000602018
where_long = 0x00400ad4
pop_rdi = 0x0000000000400a83

print(float_to_ieee(puts_plt))
#float_to_ieee(puts_got)
#float_to_ieee(pop_rdi)
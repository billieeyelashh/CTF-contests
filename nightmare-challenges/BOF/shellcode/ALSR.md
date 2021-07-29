Aslr stands for Adress space randomization

Basically it keeps us from knowing what  the memory addresses are for certain regions of memory

The bypass is we leak an address from a memory region that we want to know what it's address space is. For this it might help to take a look at the memory mappings of a process with gef>vmmap:


Thing is while the addresses in a memory space will change, the offset between the addresses themselves will not change. So if we leak a single address from a memory region that we know what is, we can just add the offset to whatever address we want to know. We can find this offset in gdb, since the offsets between two different memory addresses in the same memory region don't change.

PIE
Position Independent Executable (pie) is another binary mitigation extremely similar to aslr. It is basically aslr but for the actual binary's code / memory regions.

With pie, everything in the "binary's" memory regions is compiled to have an offset versus a fixed address. Each time the binary is run, the binary generates a random number known as a base. Then the address of everything becomes the base plus the offset. For this to make more since let's first look at the memory mapping:


With the cool features of gef we can still set a break  boin for that with gef> pie b *0x116f
									   gef> pie run

With this we an set an breakpoint for an offset BOOOM.


AGAIN HERE THE IMPORTANT COMMANDS:

pie b *0x000
pie run
vmmapp // for showing the offsets 


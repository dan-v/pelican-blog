Mystery In Latest Foscam Firmware
##########################################

:date: 2013-08-20 23:00
:tags: firmware,foscam,reverse engineering
:category: Project
:author: Dan

While attempting to build my own custom core firmware for my Foscam 8910W, I ran into a mysterious checksum of some sort that gets appended to the end of the firmware file. I see this only in the latest firmware lr_cmos_11_37_2_51.bin and not in the previous version lr_cmos_11_37_2_49.bin.

The foscam_pkmgr shell script_ is able to unpack and repackage the system firmware file. The first step is to grab the latest Foscam core firmware and then use foscam_pkgmr to unpack it.

.. _script: https://github.com/moldov/webui/blob/master/foscam_pkmgr

.. code-block:: text

	dan@ubuntu:~$./foscam_pkmgr --firm lr_cmos_11_37_2_51.bin
	Unpacking firmware lr_cmos_11_37_2_51.bin
	>Extracting linux.bin (764064)
	>Extracting rootfs.img (1054720)
	Done extracting firmware

When unpacked, the system firmware consists of two files:

- linux.bin - This is a compressed Linux kernel image. As you can see below it is running kernel version 2.4.20 with a patch from uClinux.

.. code-block:: text

	dan@ubuntu:~/lr_cmos_11_37_2_51.bin_extracted$ binwalk linux.bin 
	DECIMAL   	HEX       	DESCRIPTION
	-------------------------------------------------------------------------------------------------------------------
	0         	0x0       	Zip archive data, at least v2.0 to extract, compressed size: 763912,  uncompressed size: 1539496, name: "linux.bin"  
	764042    	0xBA88A   	End of Zip archive

	dan@ubuntu:~/lr_cmos_11_37_2_51.bin_extracted$ unzip -d /tmp linux.bin
	Archive:  linux.bin
	  inflating: /tmp/linux.bin           

	dan@ubuntu:~/lr_cmos_11_37_2_51.bin_extracted$ strings /tmp/linux.bin | grep 'Linux version'
	Linux version 2.4.20-uc0 (root@maverick-linux) (gcc version 3.0) #1924 
	

- rootfs - This is a romfs filesystem image that contains all of the binaries. It was easy enough to mount and browse, but I was surprised to not find the core CGI scripts anywhere in here.

.. code-block:: text

	dan@ubuntu:~/$ sudo mount -o loop lr_cmos_11_37_2_51.bin_extracted/rootfs.img /mnt
	mount: warning: /mnt seems to be mounted read-only.

	dan@ubuntu:~/$ ls -l /mnt/
	total 0
	drwxr-xr-x 1 root root 32 Dec 31  1969 bin
	drwxr-xr-x 1 root root 32 Dec 31  1969 dev
	drwxr-xr-x 1 root root 32 Dec 31  1969 etc
	drwxr-xr-x 1 root root 32 Dec 31  1969 flash
	drwxr-xr-x 1 root root 32 Dec 31  1969 home
	drwxr-xr-x 1 root root 32 Dec 31  1969 proc
	drwxr-xr-x 1 root root 32 Dec 31  1969 swap
	drwxr-xr-x 1 root root 32 Dec 31  1969 tmp
	drwxr-xr-x 1 root root 32 Dec 31  1969 usr
	drwxr-xr-x 1 root root 32 Dec 31  1969 var

	dan@ubuntu:~/$ ls -l /mnt/bin
	total 0
	-rwxr-xr-x 1 root root 591628 Dec 31  1969 camera
	-rwxr-xr-x 1 root root  44792 Dec 31  1969 dhcpcd
	-rwxr-xr-x 1 root root    929 Dec 31  1969 fcc_ce.wlan
	-rwxr-xr-x 1 root root  21610 Dec 31  1969 ifconfig
	-rwxr-xr-x 1 root root    234 Dec 31  1969 init
	-rwxr-xr-x 1 root root  38300 Dec 31  1969 iwconfig
	-rwxr-xr-x 1 root root  33640 Dec 31  1969 iwpriv
	drwxr-xr-x 1 root root     32 Dec 31  1969 mypppd
	-rwxr-xr-x 1 root root  28824 Dec 31  1969 route
	-rwxr-xr-x 1 root root  36894 Dec 31  1969 sh
	-rwxr-xr-x 1 root root  48520 Dec 31  1969 wetctl
	-rwxr-xr-x 1 root root  96327 Dec 31  1969 wpa_supplicant

The core CGI scripts ended up being located in the camera blob which needs to be decompressed. uClinux uses a Binary Flat format known as BFLT. To decompress this I used a tool called flthdr. I was able to use strings on the decompressed file to search through the camera binary. The CGI files were found, but I had no way of seeing the actual contents or modifying them without some form of decompiler.

I really just wanted to see if I could inject my own CGI script into the firmware. My next idea was to inject it somewhere in the init script in the rootfs image.

Before doing this, I wanted to verify that I could unpack and repack a system firmware file and end up with a file that matched the original. I quickly learned that this was not the case. For some reason the repacked firmware was smaller by 8 bytes.

.. code-block:: text

	dan@ubuntu:~/$ ls -l lr_cmos_11_37_2_51.bin*
	-rw-rw-r-- 1 dan dan 1818812 Aug 18 19:04 lr_cmos_11_37_2_51.bin
	-rw-rw-r-- 1 dan dan 1818804 Aug 20 00:23 lr_cmos_11_37_2_51.bin_custom

I ended up dumping both of these firmware files to hex for easier comparison and did a diff. The files matched except at the very end.

.. code-block:: text

	dan@ubuntu:~/$ xxd lr_cmos_11_37_2_51.bin > original.hex
	dan@ubuntu:~/$ xxd lr_cmos_11_37_2_51.bin_custom > new.hex
	dan@ubuntu:~/$ diff original.hex new.hex 
	113676c113676
	< 01bc0b0: 0000 0000 9fc0 1b0b 60aa ba34            ........`..4
	---
	> 01bc0b0: 0000 0000                                ....

Printing out the hex value in plaintext revealed what looked to be a checksum. I verified that if I appended the hex (converted back to binary) to my repacked firmware that I ended up with the same file as the original. 

.. code-block:: text

	dan@ubuntu:~/$ echo -n 9fc01b0b60aaba34 | xxd -p
	39666330316230623630616162613334

	dan@ubuntu:~/$ echo -n 9fc01b0b60aaba34 | xxd -r -p >> lr_cmos_11_37_2_51.bin_custom

	dan@ubuntu:~/$ md5sum lr_cmos_11_37_2_51.bin lr_cmos_11_37_2_51.bin_custom
	242e2788aa32aefb3b68b9988cc97159  lr_cmos_11_37_2_51.bin
	242e2788aa32aefb3b68b9988cc97159  lr_cmos_11_37_2_51.bin_custom

The remaining mystery is this checksum? I originally tried to md5sum everything but then learned md5sum is a 16 byte value. I then moved onto CRC checks. So far no luck. Without being able to generate this checksum at the end of the firmware file it isn't possible to make a custom core firmware image that will be accepted by the camera.

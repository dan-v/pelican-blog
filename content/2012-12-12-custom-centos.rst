Custom CentOS Live CD
################################

:date: 2012-12-12 22:00
:tags: centos,linux,livecd
:category: Tutorial
:author: Dan

This is a quick tutorial on creating a custom CentOS Live CD. This was done with CentOS 6.2. 

* First step is to download the CentOS Live CD ISO.

.. code-block:: text

        mkdir /iso
        cd /iso
        wget <url for centos live ISO>

* Mount CentOS ISO and copy the contents to temporary location.

.. code-block:: bash

        mount CentOS-6.2-x86_64-LiveCD.iso mnt -o loop
        mkdir CentOS-6.2-x86_64-LiveCD
        cp -arp mnt/* CentOS-6.2-x86_64-LiveCD/
        umount mnt

* Create a custom isolinux.cfg file. This menu will be displayed when booting the custom CentOS Live CD. 

.. code-block:: bash

	##########
	UI vesamenu.c32
	MENU TITLE Custom CentOS
	TIMEOUT 50
	
	DEFAULT centos
	LABEL centos
	KERNEL vmlinuz0
	APPEND initrd=initrd0.img root=live:CDLABEL=CentOS-6.2-x86_64-LiveCD rootfstype=auto ro liveimg 3 quiet nodiskmount nolvmmount  rhgb vga=791 rd.luks=0 rd.md=0 rd.dm=0 selinux=0
	##########

* Overwrite isolinux.cfg file in temporary location.

.. code-block:: bash

        cp isolinux.cfg CentOS-6.2-x86_64-LiveCD/isolinux/

* Mount squashfs and copy off all contents to temporary location. Mount ext3fs filesystem.

.. code-block:: bash

        mount CentOS-6.2-x86_64-LiveCD/LiveOS/squashfs.img mnt -o loop -t squashfs
        mkdir squashfs
        cp -a mnt/* squashfs
        umount mnt
        mkdir ext3fs
        mount squashfs/LiveOS/ext3fs.img ext3fs -o loop

* Edit file ext3fs/etc/rc.local to change boot settings for custom ISO. In this case configuring networking, creating a ramdisk, and presenting it over NFS.

.. code-block:: bash

	##########
	touch /var/lock/subsys/local
	/sbin/ifconfig eth0 0.0.0.0
	/sbin/ifconfig eth0 up
	/sbin/ifconfig eth1 0.0.0.0
	/sbin/ifconfig eth1 up
	/sbin/vconfig add eth0 101
	/sbin/vconfig add eth1 101
	/sbin/ifconfig eth0.101 192.168.101.103 netmask 255.255.255.0
	/sbin/ifconfig eth1.101 192.168.101.104 netmask 255.255.255.0
	/sbin/ifconfig eth2 192.168.100.103 netmask 255.255.255.0 up
	/sbin/ifconfig eth3 192.168.100.104 netmask 255.255.255.0 up
	/bin/mkdir /ramdisk
	/bin/mount -o size=10G -t tmpfs tmpfs /ramdisk
	/bin/echo '/ramdisk *(rw,sync,insecure,fsid=1,all_squash,sync,no_wdelay)'>/etc/exports
	/sbin/service nfs restart
	##########

* Chroot into mounted ext3fs filesystem and make any required modifications. In this case, updating root password, disabling firewall, and enabling sshd.

.. code-block:: bash

        chroot /iso/ext3fs/
        passwd root passwd
        chkconfig NetworkManager off
        chkconfig iptables off
        chkconfig ip6tables off
        chkconfig sshd on
        exit

* Regenerate squashfs and create new ISO (Custom-CentOS.iso).

.. code-block:: bash

        rm /iso/CentOS-6.2-x86_64-LiveCD/LiveOS/squashfs.img
        mksquashfs /iso/squashfs /iso/CentOS-6.2-x86_64-LiveCD/LiveOS/squashfs.img
        mkisofs -o Custom-CentOS.iso \
              -J -r -hide-rr-moved -hide-joliet-trans-tbl -V CentOS-6.2-x86_64-LiveCD \
              -b isolinux/isolinux.bin -c isolinux/boot.cat \
              -no-emul-boot -boot-load-size 4 -boot-info-table \
              /iso/CentOS-6.2-x86_64-LiveCD



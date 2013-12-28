Lenovo USB BIOS Update
#######################

:date: 2013-12-27 20:00
:tags: lenovo,bios,usb,linux
:category: Tips
:author: Dan

It took me way too long to update the BIOS on my Lenovo T420s laptop (running Linux) with a USB stick, so I figured I'd document the process.

* Download_ the latest BIOS Update Bootable CD from Lenovo. The latest at this time for my model was 1.38 and the filename was 8cuj18us.iso.
 
.. _Download: http://support.lenovo.com/en_US/downloads/default.page?selector=expand

* Download geteltorito script (extracts boot image from ISO) and execute it against ISO to create IMG file.

.. code-block:: text
        
	wget http://userpages.uni-koblenz.de/~krienke/ftp/noarch/geteltorito/geteltorito.pl
        perl geteltorito.pl 8cuj18us.iso > bios.img

* Copy IMG file to USB disk (where sdX is actual USB disk device).

.. code-block:: text
	
	dd if=bios.img of=/dev/sdX bs=512K

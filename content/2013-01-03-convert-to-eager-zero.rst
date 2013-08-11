Convert VMDK from Thin to Eager Zero
####################################

:date: 2013-01-03 20:00
:tags: vmware,windows,convert,vmdk
:category: Tips
:author: Dan

This is one way to convert a thin provisioned VMDK into a thick provisioned eager zeroed VMDK. I was unable to mount a thin provisioned VMDK in read/write mode using vmware-mount.exe, so this is how I worked around it. You will need the VMware Virtual Disk Development Kit (VDDK_) to do this.

.. _VDDK: https://communities.vmware.com/community/vmtn/developer/forums/vddk

* After installing VDDK, open cmd.exe and use vmware-vdiskmanager to convert the VMDK.

.. code-block:: text
	
	cd c:\Program Files (x86)\VMware\VMware Virtual Disk Development Kit\bin
	vmware-vdiskmanager -r c:\thin_provisioned.vmdk -t 2 c:\thick_eager_zero.vmdk


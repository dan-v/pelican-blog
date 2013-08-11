Injecting Drivers into Windows ISO
##################################

:date: 2012-12-03 22:00
:tags: windows,drivers,vmware
:category: Tutorial
:author: Dan

Here are some notes on injecting drivers into a Windows ISO. There are two images boot.wim (WindowsPE) and install.wim (actual Windows setup files) that need to be updated. In this case I am using a Windows 2008 R2 ISO. Note that Windows 2012 has PowerShell Cmdlets for DISM commands (see here_).

.. _here: http://technet.microsoft.com/en-us/library/hh852126.aspx 

* First make some working directories.

.. code-block:: text

        mkdir c:\drivers
	mkdir c:\mount
	mkdir c:\iso

* Copy all of the drivers you want to add into the c:\\drivers directory.

* Insert Windows 2008 CDROM/ISO and manually copy all files into c:\\iso directory.

* List wim file indexes and figure out correct one to edit.

.. code-block:: text

	dism /get-wiminfo /wimfile:c:\boot.wim
	dism /get-wiminfo /wimfile:c:\install.wim

* Edit boot.wim and add drivers. In this case, adding VMware drivers (Paravirtual SCSI driver and VMXNET3 network driver).

.. code-block:: text

	dism /Mount-Wim /WimFile:C:\boot.wim /Index:2 /MountDir:c:\mount
	dism /image:c:\mount /Add-Driver /driver:c:\drivers\pvscsi.inf
	dism /image:c:\mount /Add-Driver /driver:c:\drivers\vmxnet3ndis6.inf
	dism /unmount-wim /mountdir:c:\mount /commit

* Edit install.wim and add drivers. In this case, it's only being added to index 5 which is Datacenter Full edition (since this is the only one I needed at the time). 

.. code-block:: text

	dism /Mount-Wim /WimFile:C:\install.wim /Index:5 /MountDir:c:\mount
	dism /image:c:\mount /Add-Driver /driver:c:\drivers\pvscsi.inf
	dism /image:c:\mount /Add-Driver /driver:c:\drivers\vmxnet3ndis6.inf
	dism /unmount-wim /mountdir:c:\mount /commit	

* Copy the updated wim files and overwrite the ones in c:\\iso directory.

.. code-block:: text

	copy c:\boot.wim c:\iso\sources\boot.wim
	copy c:\install.wim c:\iso\sources\install.wim

* Create a new ISO

.. code-block:: text

	oscdimg.exe -lGRMSXVOL_EN_DVD -m -u2 -bC:\iso\boot\etfsboot.com C:\iso C:\Windows_2008_R2_With_Injected_VMware_Drivers.ISO


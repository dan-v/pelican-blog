Custom Foscam Web UI
#########################################

:date: 2013-08-17 12:00
:tags: hardware,hacking,foscam
:category: Project
:author: Dan

I have had a Foscam 8910W network camera setup in my home for quite some time. The core firmware and web inteface on these devices have never really been a strong point. I started this project wanting to get a root shell on the device, but ended up moving away from that after almost bricking the camera.

There was some work that had already been done on disassembling the Foscam firmware. There are two firmware files, a core firmware file and Web UI firmware file. Both of these firmware blobs are really just a header of some length followed by the files. A shell script exists_ called foscam_pkmgr that can unpack and pack both of these firmware files.

.. _exists: https://github.com/moldov/webui/blob/master/foscam_pkmgr

I took the functions from foscam_pkmgr and created a script to modify the Web UI. My new script foscam_customweb_ does the following:

.. _foscam_customweb: https://github.com/dan-v/foscam-customweb/

- Unpacks Web UI firmware
- Adds user customizations
- Repacks Web UI firmware
- Uploads it to camera

For Web UI customizations, I replaced the main page with a very simple Twitter Bootstrap site. I added keybindings to the arrow keys using jQuery to control the camera instead of having to click on arrows to move it around.

Below is the script in action and here is the final result_.

.. _result: images/foscam-custom-webui.png

.. code-block:: text

	dan@ubuntu:~/foscam-customweb$ ./foscam_customweb -w 2.4.10.5.bin -s 192.168.1.100 -u admin
	Enter password for admin: xxxxxxxx

	Found Web UI Version  : 2.4.10.5
	Unpacking Files...
	Extracting Web UI to 2.4.10.5.bin_extracted

	Copying custom Web UI from custom_web to 2.4.10.5.bin_extracted

	Repackaging the Web UI
	Checking Integrity of repacked Web UI:
		->Version : 2.4.10.5
		->Checksum verified (070c21cc)

	Firmware successfully packed to custom_2.4.10.5.bin

	Uploading Web UI firmware custom_2.4.10.5.bin to http://192.168.1.100/upgrade_htmls.cgi
	ok.

	Completed.
	Now just wait for camera to reboot.


It seems pretty hard to brick your device when only updating the Web UI firmware because it does not contain the core CGI scripts, so it is always possible to revert the changes.

.. code-block:: text

	curl -u admin:password -F file=@2.4.10.5.bin http://192.168.1.100/upgrade_htmls.cgi


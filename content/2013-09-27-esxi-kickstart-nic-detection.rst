ESXi Kickstart NIC Detection
#############################

:date: 2013-09-27 12:00
:tags: esxi,kickstart
:category: Tip
:author: Dan

A recent problem I ran into was NIC enumeration when using a kickstart file for ESXi installation. I had a two port 1Gb NIC and a two port 10Gb NIC and on any given install they would come up as different numbered vmnics. In the kickstart file I was building out the virtual switches with specific VLANs, so the correct NICs needed to be identified.

This is what I ended up with after the firstboot section of the kickstart script:

.. code-block:: text

	one_gig_nic_type="Broadcom"
	ten_gig_nic_type="Emulex"
	first_nic_type=$(esxcli network nic list | grep 'vmnic0' | awk '{print $9}')
	one_gig_1=$(esxcli network nic list | grep -i "$one_gig_nic_type" | grep '\.0' | cut -f1 -d " ")
	one_gig_2=$(esxcli network nic list | grep -i "$one_gig_nic_type" | grep '\.1' | cut -f1 -d " ")
	ten_gig_1=$(esxcli network nic list | grep -i "$ten_gig_nic_type" | grep '\.0' | cut -f1 -d " ")
	ten_gig_2=$(esxcli network nic list | grep -i "$ten_gig_nic_type" | grep '\.1' | cut -f1 -d " ")

Then just use these variables throughout the rest of the kickstart script to configure virtual switches.

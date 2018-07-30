# OpenstackSDK
Create Network topology using OpenStackSDK

--------------------------------------------------------------------------------------

Configuration of Virtual Machine on Virtual Box for Openstack:

Operating System on Virtual Box:
Type: Linux
Version: RedHat (64 bit)
OS Version: CentOS7 v7.5.1804 (64-bit)

Recommended OS:
Ubuntu 16.04 as it has a native support.

Memory Size:
If you have 8+ GB use 4 GB.
If you have only 4 GB use 2.5 GB.

Processors:
2 or more Core Processors

Hard Disk:
Keep it 20+GB, VDI type, dynamically allocated.

Network:
We can do Bridge Connection or NAT connection for using browser and Putty/Superputty.
Set NAT connection with Port forwarding rules on Virtual Box.

Name  Protocol  Host-IP  HOST-Port  Guest-IP  Guest-Port
SSH   TCP       -        22         -         22
TCP   TCP       -        80         -         80
VNC   TCP       -        6080       -         6080

Port 22 - SSH
Port 80 - HTTP
Port 6080 - Console into instance.

--------------------------------------------------------------------------------------

Installation of Devstack on Virtual Machine:

Openstack
Openstack version: 3.15.0
Devstack version: rocky

After fresh installing the CentOS7 on VM, run the following commands:
Ping to check after network configuration on CentOS.
$ ping -c3 www.google.com

If the ping doesn’t work, check the internet connection by restarting the network as it is required to download the files from the github.
$ service network restart
If still it fails, try using the Network manager TUI.
$ nmtui

Set the connection mentioned above and restart the service.
$ service network restart
After the internet connection is working.
$ sudo yum update
$ sudo yum upgrade
$ sudo yum install net-tools
$ sudo yum install vim
$ sudo yum install git
$ git clone https://git.openstack.org/openstack-dev/devstack
$ cd devstack
Create the local.conf file inside the devstack folder and add the following lines.
HOST_IP is not necessary but while installation if you get an error stating that there is no HOST_IP in local.conf file, just add the host ip to the local.conf file and restart the installation.

Start the installation by running the following command.
$ ./stack.sh

It takes about 60 minutes depending on the speed of internet, the system configuration on virtual box to complete.
This will be the final message after the installation of devstack on your virtual machine.
It will mention the host IP address, users, password, dashboard IP address, installed devstack version and OS version.

--------------------------------------------------------------------------------------

Troubleshooting:

In case if you cannot connect to the Openstack website or SSH after installing the devstack, then the traffic on those ports or IP’s might be blocked by the firewall.
Flush the iptables (Not recommended on the production) or add the iptables rules to accept the traffic from different ports and IP’s.
$ sudo ipables -F
$ sudo iptables -L

While shutting down the Virtual Machine always close the machine in save state or else you will need to install the devstack again since its main use case is not running a cloud so it will fail after a reboot.

If any time you get an error saying, “Missing value auth-url required for auth plugin password”
Source openrc so that it exports the variables.
devstack$ source openrc
WARNING: setting legacy OS_TENANT_NAME to support cli tools.
devstack$ export | grep OS_

Always close the machine in save state. If you shut down the virtual machine, the Openstack will not work. We need to do the following to start the Openstack again.
$ ./unstack.sh
$ ./clean.sh
$ ./stack.sh

This will take around 1-1.5 hrs to make the Openstack again working. Everything configured inside the Openstack will be deleted as this will be new installation.
After installation, put the machine in saved state and clone the machine in virtual box.

--------------------------------------------------------------------------------------
 

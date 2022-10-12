# ASRock - 2x NVIDIA GeForce 3080 Crypto Miner

## General Information

ASRock Mining rack with 4 GB of RAM running Windows 10 from a USB stick located on the motherboard itself. The Nvidia GPU's need to be terminated with an HDMI terminator, and otherwise the mining software isn't able to bypass the Hash rate limited from Nvidia.

### Side notes

* Windows Nvidia Beta driver is the only one getting the maximum Hash Rate from the GPU's! If you decide to rebuild with a Linux-based Mining OS, you will lose around 33% of the mining Hash Rate.

## Hardware

* Motherboard – ASRock Z87 Extreme
* SanDisk USB Thumb drive – Windows System Disk
* 2x GPU – Nvidia GeForce 3080
* 2x HDMI Terminator

## Software

* MSI Afterbunner - Overclocking software
* Nvidia Driver – GPU Driver
* Gminer – ETH Crypto Miner
* T-Rex - ETH Crypto Miner

## Setting up the miner for the first time

### Windows credentials

Logging into the Windows directly on the console should be automatically on boot of the computer. The following credentials are being used for that.

* Windows user: **miner**
* User password: **12CryptoKoning!**

### Connect the miner to the network

When you start the miner for the first time, it will not have an Internet connection, which is required to be able to get the miner to work and send the calculated hashes to the internet. The best way to do this is by plugging the miner into the network with a LAN cable. Wi-Fi is **NOT** recommended and by default disabled on Windows.

### TeamViewer

After the miner is plugged in to the network, you should be able to connect to it via TeamViewer with the following credentials:

* Computer ID: **107 888 452**
* TeamViewer password: **12CryptoKoning21!**

### Set up your wallet

There are multiple pieces of software available to mine crypto. The best results we've got with **Gminer** and on the second place **T-rex**.

#### Mining software:

* [Gminer](https://gminer.info/) - [Direct Download - v3.05\_windows64](https://github.com/develsoftware/GMinerRelease/releases/download/3.05/gminer_3_05_windows64.zip)
* [T-Rex](https://trex-miner.com/) - [Direct Download - v0.26.5-win](https://trex-miner.com/download/t-rex-0.26.5-win.zip)

### Manual for setting up the Mining rig

* [Manual (German)](https://www.hardwareluxx.de/index.php/news/hardware/grafikkarten/55694-ethereum-mining-bremse-der-geforce-rtx-3060-umgangen-4-update.html)

### Nvidia driver download

To get the maximum possible mining hash with the GeForce RTX3060 you need to use a leaked old Beta driver for the **Nvidia GPU GTX3060**

* [Nvidia BETA driver](https://bittention.com/software/beta-driver-470-05-download-for-rtx-3060/)

## Start miner is rebooted

 1. Open Windows Explorer by pressing **Win button + E**
 2. Navigate to Mining software (at moment of writing in **C:\\Users\\miner\\Downloads\\gminer\_2\_54\_windows64**)
 3. Select **.bat** file you use for starting the miner with **single** click on **Left** button
 4. **Right click** to open sub-menu and select **Copy to -> Desktop (create shortcut)**
 5. Close the Windows Explorer window
 6. Press **Win button + R** to open the **Run command** window
 7. Enter `shellcommon startup` followed by **ENTER**
 8. Drag the created shortcut to the window that opened
 9. Close the Windows Explorer window
10. Restart to see if the miner starts automatically

## Questions and Answers

* Q: The miner stopped working and can't connect with TeamViewer
  * A: Windows updates are forced to install by Microsoft, sometimes after a major update you need to answer some questions before the miner continues to boot and start the miner software. To validate this, connect a mouse, keyboard, and monitor to see what is going on.
* Q: I can't find the hard drive
  * A: The miner runs from a **SanDisk USB Thumb drive** which is installed on the motherboard.
* Q: System is slow or unresponsive
  * A: The miner runs from a **USB Drive,** which is fine for a miner, but can be slow or feels unresponsive. This should not interrupt the mining process. A weekly reboot of the miner is a good thing to do so the miner will perform the best way possible.
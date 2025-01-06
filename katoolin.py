# pylint: disable=anomalous-backslash-in-string
#!/usr/bin/python

import os
import sys
import traceback

os.system("clear")

if os.getuid() != 0:
    print("Sorry. This script requires sudo privledges")
    sys.exit()


def main():
    try:
        print(
            """
			$$\   $$\             $$\                         $$\ $$\           
			$$ | $$  |            $$ |                        $$ |\__|          
			$$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
			$$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
			$$  $$<    $$$$$$$ |  \033[1;35mKali linux tools installer\033[1;m |$$ |$$ |$$ |  $$ |
			\033[1;35m$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
			$$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
			\__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| V7.0 \033[1;m
			\033[1;37m+ -- -- +=[ Author: Easton Seidel(easton57)\033[1;m
			\033[1;37m+ -- -- +=[ Github: https://github.com/easton57/katoolin7\033[1;m
			\033[1;37m+ -- -- +=[ 331 Tools \033[1;m\n
			"""
        )

        def init1():
            while True:
                print(
                    """
					1) Add Kali repositories & Update 
					2) View Categories
					3) Install classicmenu indicator
					4) Install Kali menu
					5) Help
					"""
                )

                option0 = input("\033[1;35mkat > \033[1;m")

                while option0 == "1":
                    print(
                        """
						1) Add kali linux repositories
						2) Update
						3) Remove all kali linux repositories
						4) View the contents of sources.list file
						"""
                    )

                    repo = input("\033[1;35mWhat do you want to do ?> \033[1;m")

                    if repo == "1":
                        os.system(
                            "apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys ED444FF07D8D0BF6"
                        )
                        os.system(
                            "echo '# Kali linux repositories | Added by Katoolin\ndeb \
                            https://kali.mirror.garr.it/mirrors/kali kali-rolling main non-free contrib' >> \
                                /etc/apt/sources.list"
                        )
                    elif repo == "2":
                        os.system("apt update -m")
                    elif repo == "3":
                        infile = "/etc/apt/sources.list"
                        outfile = "/etc/apt/sources.list"

                        delete_list = [
                            "# Kali linux repositories | Added by Katoolin\n",
                            "deb https://kali.mirror.garr.it/mirrors/kali kali-rolling main non-free contrib\n",
                        ]
                        fin = open(infile)
                        os.remove("/etc/apt/sources.list")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, "")
                            fout.write(line)

                        fin.close()
                        fout.close()
                        print(
                            "\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m"
                        )
                    elif repo == "back":
                        init1()
                    elif repo == "gohome":
                        init1()
                    elif repo == "4":
                        file = open("/etc/apt/sources.list", "r")

                        print(file.read())

                    else:
                        print("\033[1;31mSorry, that was an invalid command!\033[1;m")

                if option0 == "3":
                    print(
                        """
						ClassicMenu Indicator is a notification area applet (application indicator) for the top panel \
                            of Ubuntu's Unity desktop environment.
						It provides a simple way to get a classic GNOME-style application menu for those who prefer \
                            this over the Unity dash menu.
						Like the classic GNOME menu, it includes Wine games and applications if you have those \
                            installed.
						For more information , please visit : \
                            http://www.florian-diesch.de/software/classicmenu-indicator/
						"""
                    )
                    repo = input(
                        "\033[1;35mDo you want to install classicmenu indicator ? [y/n]> \033[1;m"
                    )
                    if repo == "y":
                        os.system("add-apt-repository ppa:diesch/testing && apt update")
                        os.system("sudo apt install classicmenu-indicator")

                elif option0 == "4":
                    repo = input(
                        "\033[1;35mDo you want to install Kali menu ? [y/n]> \033[1;m"
                    )
                    if repo == "y":
                        os.system("apt install kali-menu")

                elif option0 == "5":
                    print(
                        """
						****************** +Commands+ ******************
						\033[1;35mback\033[1;m 	\033[1;35mGo back\033[1;m
						\033[1;35mgohome\033[1;m	\033[1;35mGo to the main menu\033[1;m
						"""
                    )

                def init():
                    while option0 == "2":
                        print(
                            """
							\033[1;35m**************************** All Categories *****************************\033[1;m
							1) Information Gathering			8) Exploitation Tools
							2) Vulnerability Analysis			9) Forensics Tools
							3) Wireless Attacks				10) Stress Testing
							4) Web Applications				11) Password Attacks
							5) Sniffing & Spoofing				12) Reverse Engineering
							6) Maintaining Access				13) Hardware Hacking
							7) Reporting Tools 				14) Extra
																
							0) All
							"""
                        )
                        print(
                            "\033[1;35mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m"
                        )

                        option1 = input("\033[1;35mkat > \033[1;m")
                        if option1 == "back":
                            init1()
                        elif option1 == "gohome":
                            init1()
                        elif option1 == "0":
                            install_packages()

                        while option1 == "1":
                            packages = read_packages("information_gathering.txt")

                            print(
                                """
								\033[1;35m=+[ Information Gathering\033[1;m
								"""
                            )
                            for i in range(0, len(packages), 2):
                                print(
                                    f"""
                                    \033[1;m {i + 1}) {packages[i]}\t\t{i + 2}) {packages[i + 1]}""")
                            print(
                                """
                                \033[1;m0) Install all Information Gathering tools\n
								"""
                            )

                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")

                            if option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            elif option2 == "0":
                                install_packages(packages)
                            else:
                                install_packages(packages[int(option2) - 1])

                            # Wait for a second goodness
                            input("Review installation above then press enter...")

                        while option1 == "2":
                            print(
                                """
								\033[1;35m=+[ Vulnerability Analysis\033[1;m
								1) BBQSQL				18) Nmap
								2) BED					19) ohrwurm
								3) cisco-auditing-tool			20) openvas-administrator
								4) cisco-global-exploiter		21) 
								5) cisco-ocs				22) gvmd
								6) cisco-torch				23) openvas-scanner
								7) copy-router-config			24) Oscanner
								8) commix				25) Powerfuzzer
								9) DBPwAudit				26) sfuzz
								10) DoonaDot				27) SidGuesser
								11) DotPwn				28) SIPArmyKnife
								12) Greenbone Security Assistant 	29) sqlmap
								13) GSD					30) Sqlninja
								14) HexorBase				31) sqlsus
								15) Inguma				32) THC-IPV6
								16) jSQL				33) tnscmd10g
								17) Lynis				34) unix-privesc-check
													35) Yersinia
								0) Install all Vulnerability Analysis tools\n
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "2":
                                os.system("apt install bed")
                            elif option2 == "3":
                                os.system("apt install cisco-auditing-tool")
                            elif option2 == "4":
                                os.system("apt install cisco-global-exploiter")
                            elif option2 == "5":
                                os.system("apt install cisco-ocs")
                            elif option2 == "6":
                                os.system("apt install cisco-torch")
                            elif option2 == "7":
                                os.system("apt install copy-router-config")
                            elif option2 == "8":
                                os.system(
                                    "apt install git && git clone https://github.com/stasinopoulos/commix.git commix \
										&& cd commix && python ./commix.py --install"
                                )
                            elif option2 == "9":
                                os.system(
                                    "echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'"
                                )
                            elif option2 == "10":
                                os.system("apt install doona")
                            elif option2 == "11":
                                os.system("apt install dotdotpwn")
                            elif option2 == "12":
                                os.system("apt install greenbone-security-assistant")
                            elif option2 == "13":
                                os.system(
                                    "apt install git && git clone git://git.kali.org/packages/gsd.git"
                                )
                            elif option2 == "15":
                                print(
                                    "Please download inguma from : http://inguma.sourceforge.net"
                                )
                            elif option2 == "16":
                                os.system("apt install jsql")
                            elif option2 == "17":
                                os.system("apt install lynis")
                            elif option2 == "18":
                                os.system("apt install nmap")
                            elif option2 == "19":
                                os.system("apt install ohrwurm")
                            elif option2 == "20":
                                os.system("apt install openvas-administrator")
                            elif option2 == "21":
                                os.system("apt install ")
                            elif option2 == "22":
                                os.system("apt install gvmd")
                            elif option2 == "23":
                                os.system("apt install openvas-scanner")
                            elif option2 == "24":
                                os.system("apt install oscanner")
                            elif option2 == "25":
                                os.system("apt install ")
                            elif option2 == "26":
                                os.system("apt install sfuzz")
                            elif option2 == "27":
                                os.system("apt install sidguesser")
                            elif option2 == "28":
                                os.system("apt install siparmyknife")
                            elif option2 == "29":
                                os.system("apt install sqlmap")
                            elif option2 == "30":
                                os.system("apt install sqlninja")
                            elif option2 == "31":
                                os.system("apt install sqlsus")
                            elif option2 == "32":
                                os.system("apt install thc-ipv6")
                            elif option2 == "33":
                                os.system("apt install tnscmd10g")
                            elif option2 == "34":
                                os.system("apt install unix-privesc-check")
                            elif option2 == "35":
                                os.system("apt install yersinia")
                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            elif option2 == "0":
                                os.system(
                                    "apt install -y bed cisco-auditing-tool cisco-global-exploiter cisco-ocs \
									cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant \
									jsql lynis nmap ohrwurm gvmd openvas-scanner oscanner sfuzz sidguesser \
									siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia"
                                )
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m"
                                )

                        while option1 == "3":
                            print(
                                """
								\033[1;35m=+[ Wireless Attacks\033[1;m
								1) Aircrack-ng				17) kalibrate-rtl
								2) Asleap				18) KillerBee
								3) Bluelog				19) Kismet
								4) BlueMaho				20) mdk3
								5) Bluepot				21) mfcuk
								6) BlueRanger				22) mfoc
								7) Bluesnarfer				23) mfterm
								8) Bully				24) Multimon-NG
								9) coWPAtty				25) PixieWPS
								10) crackle				26) Reaver
								11) eapmd5pass				27) redfang
								12) Fern Wifi Cracker			28) RTLSDR Scanner
								13) Ghost Phisher			29) Spooftooph
								14) GISKismet				30) Wifi Honey 
								15) mdk4                                31) Wifitap
								16) gr-scan				32) Wifite 
								0) Install all Wireless Attacks tools\n
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "1":
                                os.system("apt install aircrack-ng")
                            elif option2 == "2":
                                os.system("apt install asleap")
                            elif option2 == "3":
                                os.system("apt install bluelog")
                            elif option2 == "4":
                                os.system(
                                    "apt install git && git clone git://git.kali.org/packages/bluemaho.git"
                                )
                            elif option2 == "5":
                                os.system(
                                    "apt install git && git clone git://git.kali.org/packages/bluepot.git"
                                )
                            elif option2 == "6":
                                os.system("apt install blueranger")
                            elif option2 == "7":
                                os.system("apt install bluesnarfer")
                            elif option2 == "8":
                                os.system("apt install bully")
                            elif option2 == "9":
                                os.system("apt install cowpatty")
                            elif option2 == "10":
                                os.system("apt install crackle")
                            elif option2 == "11":
                                os.system("apt install eapmd5pass")
                            elif option2 == "12":
                                os.system("apt install fern-wifi-cracker")
                            elif option2 == "13":
                                os.system("apt install ")
                            elif option2 == "14":
                                os.system("apt install ")
                            elif option2 == "16":
                                os.system(
                                    "apt install git && git clone git://git.kali.org/packages/gr-scan.git"
                                )
                            elif option2 == "17":
                                os.system("apt install kalibrate-rtl")
                            elif option2 == "18":
                                os.system("apt install ")
                            elif option2 == "19":
                                os.system("apt install kismet")
                            elif option2 == "20":
                                os.system("apt install mdk3")
                            elif option2 == "21":
                                os.system("apt install mfcuk")
                            elif option2 == "22":
                                os.system("apt install mfoc")
                            elif option2 == "23":
                                os.system("apt install mfterm")
                            elif option2 == "24":
                                os.system("apt install multimon-ng")
                            elif option2 == "25":
                                os.system("apt install pixiewps")
                            elif option2 == "26":
                                os.system("apt install reaver")
                            elif option2 == "27":
                                os.system("apt install redfang")
                            elif option2 == "28":
                                os.system("apt install rtlsdr-scanner")
                            elif option2 == "29":
                                os.system("apt install spooftooph")
                            elif option2 == "30":
                                os.system("apt install wifi-honey")
                            elif option2 == "31":
                                os.system("apt install ")
                            elif option2 == "32":
                                os.system("apt install wifite")
                            elif option2 == "0":
                                os.system(
                                    "apt install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty \
									crackle eapmd5pass fern-wifi-cracker kalibrate-rtl kismet mdk3 mfcuk mfoc mfterm \
									multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifite"
                                )
                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m"
                                )

                        while option1 == "4":
                            print(
                                """
								\033[1;35m=+[ Web Applications\033[1;m
								1) apache-users			21) Parsero
								2) Arachni				22) 
								3) BBQSQL				23) Powerfuzzer
								4) BlindElephant			24) ProxyStrike
								5) Burp Suite				25) Recon-ng
								6) commix				26) Skipfish
								7) CutyCapt				27) sqlmap
								8) DAVTest				28) Sqlninja
								9) 				29) sqlsus
								10) DIRB				30) 
								11) DirBuster				31) Uniscan
								12) 				32) Vega
								13) FunkLoad				33) 
								14) Grabber				34) WebScarab
								15) jboss-autopwn			35) Webshag
								16) joomscan				36) WebSlayer
								17) jSQL				37) WebSploit
								18) Maltego Teeth			38) Wfuzz
								19) PadBuster				39) WPScan
								20) Paros				40) XSSer
													41) zaproxy
								0) Install all Web Applications tools\n
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )

                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "1":
                                os.system("apt install apache-users")
                            elif option2 == "2":
                                os.system("apt install ")
                            elif option2 == "3":
                                os.system("apt install ")
                            elif option2 == "5":
                                os.system("apt install burpsuite")
                            elif option2 == "6":
                                os.system("apt install cutycapt")
                            elif option2 == "7":
                                os.system(
                                    "apt install git && git clone https://github.com/stasinopoulos/commix.git commix \
										&& cd commix && python ./commix.py --install"
                                )
                            elif option2 == "8":
                                os.system("apt install davtest")
                            elif option2 == "9":
                                os.system("apt install ")
                            elif option2 == "10":
                                os.system("apt install dirb")
                            elif option2 == "11":
                                os.system("apt install dirbuster")
                            elif option2 == "12":
                                os.system("apt install ")
                            elif option2 == "13":
                                os.system("apt install ")
                            elif option2 == "14":
                                os.system("apt install ")
                            elif option2 == "15":
                                os.system("apt install jboss-autopwn")
                            elif option2 == "16":
                                os.system("apt install joomscan")
                            elif option2 == "17":
                                os.system("apt install jsql")
                            elif option2 == "18":
                                os.system("apt install maltego-teeth")
                            elif option2 == "19":
                                os.system("apt install padbuster")
                            elif option2 == "20":
                                os.system("apt install paros")
                            elif option2 == "21":
                                os.system("apt install parsero")
                            elif option2 == "22":
                                os.system("apt install ")
                            elif option2 == "24":
                                os.system("apt install ")
                            elif option2 == "25":
                                os.system("apt install recon-ng")
                            elif option2 == "26":
                                os.system("apt install skipfish")
                            elif option2 == "27":
                                os.system("apt install sqlmap")
                            elif option2 == "28":
                                os.system("apt install sqlninja")
                            elif option2 == "29":
                                os.system("apt install sqlsus")
                            elif option2 == "30":
                                os.system("apt install ")
                            elif option2 == "31":
                                os.system("apt install uniscan")
                            elif option2 == "32":
                                os.system("apt install ")
                            elif option2 == "33":
                                os.system("apt install ")
                            elif option2 == "34":
                                os.system("apt install webscarab")
                            elif option2 == "35":
                                print("Webshag is unavailable")
                            elif option2 == "36":
                                os.system(
                                    "apt install git && git clone git://git.kali.org/packages/webslayer.git"
                                )
                            elif option2 == "37":
                                os.system("apt install websploit")
                            elif option2 == "38":
                                os.system("apt install wfuzz")
                            elif option2 == "39":
                                os.system("apt install wpscan")
                            elif option2 == "40":
                                os.system("apt install xsser")
                            elif option2 == "41":
                                os.system("apt install zaproxy")
                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            elif option2 == "0":
                                os.system(
                                    "apt install -y apache-users burpsuite cutycapt davtest dirb dirbuster \
									jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero \
									recon-ng skipfish sqlmap sqlninja sqlsus uniscan webscarab websploit wfuzz wpscan \
									xsser zaproxy"
                                )
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m"
                                )

                        while option1 == "5":
                            print(
                                """
								\033[1;35m=+[ Sniffing & Spoofing\033[1;m
								1) Burp Suite				17) rtpmixsound
								2) DNSChef				18) sctpscan
								3) fiked				19) SIPArmyKnife
								4) hamster-sidejack			20) SIPp
								5) HexInject				21) SIPVicious
								6) iaxflood				22) SniffJoke
								7) inviteflood				23) SSLsplit
								8) iSMTP				24) sslstrip
								9) isr-evilgrade			25) THC-IPV6
								10) mitmproxy				26) VoIPHopper
								11) ohrwurm				27) WebScarab
								12) protos-sip				28) Wifi Honey
								13) rebind				29) Wireshark
								14) responder				30) xspy
								15) rtpbreak				31) Yersinia
								16) rtpinsertsound			32) zaproxy 
								0) Install all Sniffing & Spoofing tools\n
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "1":
                                os.system("apt install burpsuite")
                            elif option2 == "2":
                                os.system("apt install dnschef")
                            elif option2 == "3":
                                os.system("apt install fiked")
                            elif option2 == "4":
                                os.system("apt install hamster-sidejack")
                            elif option2 == "5":
                                os.system("apt install hexinject")
                            elif option2 == "6":
                                os.system("apt install iaxflood")
                            elif option2 == "7":
                                os.system("apt install inviteflood")
                            elif option2 == "8":
                                os.system("apt install ismtp")
                            elif option2 == "9":
                                os.system(
                                    "apt install git && git clone git://git.kali.org/packages/isr-evilgrade.git"
                                )
                            elif option2 == "10":
                                os.system("apt install mitmproxy")
                            elif option2 == "11":
                                os.system("apt install ohrwurm")
                            elif option2 == "12":
                                os.system("apt install protos-sip")
                            elif option2 == "13":
                                os.system("apt install rebind")
                            elif option2 == "14":
                                os.system("apt install responder")
                            elif option2 == "15":
                                os.system("apt install rtpbreak")
                            elif option2 == "16":
                                os.system("apt install rtpinsertsound")
                            elif option2 == "17":
                                os.system("apt install rtpmixsound")
                            elif option2 == "18":
                                os.system("apt install sctpscan")
                            elif option2 == "19":
                                os.system("apt install siparmyknife")
                            elif option2 == "20":
                                os.system("apt install sipp")
                            elif option2 == "21":
                                os.system("apt install sipvicious")
                            elif option2 == "22":
                                os.system("apt install sniffjoke")
                            elif option2 == "23":
                                os.system("apt install sslsplit")
                            elif option2 == "24":
                                os.system("apt install sslstrip")
                            elif option2 == "25":
                                os.system("apt install thc-ipv6")
                            elif option2 == "26":
                                os.system("apt install voiphopper")
                            elif option2 == "27":
                                os.system("apt install webscarab")
                            elif option2 == "28":
                                os.system("apt install wifi-honey")
                            elif option2 == "29":
                                os.system("apt install wireshark")
                            elif option2 == "30":
                                os.system("apt install xspy")
                            elif option2 == "31":
                                os.system("apt install yersinia")
                            elif option2 == "32":
                                os.system("apt install zaproxy")
                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            elif option2 == "0":
                                os.system(
                                    "apt install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood \
									inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak \
									rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke \
									sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy \
									yersinia zaproxy"
                                )
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m"
                                )

                        while option1 == "6":
                            print(
                                """
								\033[1;35m=+[ Maintaining Access\033[1;m
								1) CryptCat
								2) Cymothoa
								3) dbd
								4) dns2tcp
								5) 	
								6) HTTPTunnel
								7) Intersect
								8) Nishang
								9) polenum
								10) PowerSploit
								11) pwnat
								12) RidEnum
								13) sbd
								14) U3-Pwn
								15) Webshells
								16) Weevely
								0) Install all Maintaining Access tools
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "1":
                                os.system("apt install cryptcat")
                            elif option2 == "2":
                                os.system("apt install ")
                            elif option2 == "3":
                                os.system("apt install dbd")
                            elif option2 == "4":
                                os.system("apt install dns2tcp")
                            elif option2 == "5":
                                os.system("apt install ")
                            elif option2 == "6":
                                os.system("apt install httptunnel")
                            elif option2 == "7":
                                os.system("apt install ")
                            elif option2 == "8":
                                os.system("apt install nishang")
                            elif option2 == "9":
                                os.system("apt install polenum")
                            elif option2 == "10":
                                os.system("apt install powersploit")
                            elif option2 == "11":
                                os.system("apt install pwnat")
                            elif option2 == "12":
                                os.system("apt install ridenum")
                            elif option2 == "13":
                                os.system("apt install sbd")
                            elif option2 == "14":
                                os.system("apt install ")
                            elif option2 == "15":
                                os.system("apt install webshells")
                            elif option2 == "16":
                                os.system("apt install weevely")
                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            elif option2 == "0":
                                os.system(
                                    "apt install -y cryptcat dbd dns2tcp httptunnel nishang polenum powersploit pwnat \
									ridenum sbd webshells weevely"
                                )
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m"
                                )

                        while option1 == "7":
                            print(
                                """
								\033[1;35m=+[ Reporting Tools\033[1;m
								1) CaseFile
								2) CutyCapt
								3) dos2unix
								4) Dradis
								5) KeepNote	
								6) MagicTree
								7) Metagoofil
								8) Nipper-ng
								9) pipal
								0) Install all Reporting Tools\n
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "1":
                                os.system("apt install casefile")
                            elif option2 == "2":
                                os.system("apt install cutycapt")
                            elif option2 == "3":
                                os.system("apt install dos2unix")
                            elif option2 == "4":
                                os.system("apt install ")
                            elif option2 == "5":
                                os.system("apt install ")
                            elif option2 == "6":
                                os.system("apt install ")
                            elif option2 == "7":
                                os.system("apt install metagoofil")
                            elif option2 == "8":
                                os.system("apt install nipper-ng")
                            elif option2 == "9":
                                os.system("apt install pipal")
                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            elif option2 == "0":
                                os.system(
                                    "apt install -y casefile cutycapt dos2unix metagoofil nipper-ng pipal"
                                )
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m"
                                )

                        while option1 == "8":
                            print(
                                """
								\033[1;35m=+[ Exploitation Tools\033[1;m
								1) Armitage
								2) Backdoor Factory
								3) BeEF
								4) cisco-auditing-tool
								5) cisco-global-exploiter	
								6) cisco-ocs
								7) cisco-torch
								8) commix
								9) crackle
								10) jboss-autopwn
								11) Linux Exploit Suggester
								12) Maltego Teeth
								13) SET
								14) ShellNoob
								15) sqlmap
								16) THC-IPV6
								17) Yersinia
								0) Install all Exploitation Tools\n
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "1":
                                os.system("apt install armitage")
                            elif option2 == "2":
                                os.system("apt install backdoor-factory")
                            elif option2 == "3":
                                os.system("apt install beef-xss")
                            elif option2 == "4":
                                os.system("apt install cisco-auditing-tool")
                            elif option2 == "5":
                                os.system("apt install cisco-global-exploiter")
                            elif option2 == "6":
                                os.system("apt install cisco-ocs")
                            elif option2 == "7":
                                os.system("apt install cisco-torch")
                            elif option2 == "8":
                                os.system(
                                    "apt install git && git clone https://github.com/stasinopoulos/commix.git commix \
										&& cd commix && python ./commix.py --install"
                                )
                            elif option2 == "9":
                                os.system("apt install crackle")
                            elif option2 == "10":
                                os.system("apt install jboss-autopwn")
                            elif option2 == "11":
                                os.system("apt install linux-exploit-suggester")
                            elif option2 == "12":
                                os.system("apt install maltego-teeth")
                            elif option2 == "13":
                                os.system("apt install set")
                            elif option2 == "14":
                                os.system("apt install ")
                            elif option2 == "15":
                                os.system("apt install sqlmap")
                            elif option2 == "16":
                                os.system("apt install thc-ipv6")
                            elif option2 == "17":
                                os.system("apt install yersinia")
                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            elif option2 == "0":
                                os.system(
                                    "apt install -y armitage backdoor-factory cisco-auditing-tool \
									cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn \
									linux-exploit-suggester maltego-teeth set  sqlmap thc-ipv6 yersinia beef-xss"
                                )
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m"
                                )

                        while option1 == "9":
                            print(
                                """
								\033[1;35m=+[ Forensics Tools\033[1;m
								1) Binwalk				11) extundelete
								2) bulk-extractor			12) Foremost
								3) Capstone				13) Galleta
								4) chntpw				14) Guymager
								5) Cuckoo				15) iPhone Backup Analyzer
								6) dc3dd				16) p0f
								7) ddrescue				17) pdf-parser
								8) DFF					18) pdfid
								9) diStorm3				19) 
								10) Dumpzilla				20) 
													21) RegRipper
													22) Volatility
													23) Xplico
								0) Install all Forensics Tools\n
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "1":
                                os.system("apt install binwalk")
                            elif option2 == "2":
                                os.system("apt install bulk-extractor")
                            elif option2 == "3":
                                os.system(
                                    "apt install git && git clone git://git.kali.org/packages/capstone.git"
                                )
                            elif option2 == "4":
                                os.system("apt install chntpw")
                            elif option2 == "5":
                                os.system("apt install ")
                            elif option2 == "6":
                                os.system("apt install dc3dd")
                            elif option2 == "7":
                                os.system("apt install ddrescue")
                            elif option2 == "8":
                                print("dff is unavailable")
                            elif option2 == "9":
                                os.system(
                                    "apt install git && git clone git://git.kali.org/packages/distorm3.git"
                                )
                            elif option2 == "10":
                                os.system("apt install dumpzilla")
                            elif option2 == "11":
                                os.system("apt install extundelete")
                            elif option2 == "12":
                                os.system("apt install foremost")
                            elif option2 == "13":
                                os.system("apt install galleta")
                            elif option2 == "14":
                                os.system("apt install guymager")
                            elif option2 == "15":
                                os.system("apt install ")
                            elif option2 == "16":
                                os.system("apt install p0f")
                            elif option2 == "17":
                                os.system("apt install pdf-parser")
                            elif option2 == "18":
                                os.system("apt install pdfid")
                            elif option2 == "19":
                                os.system("apt install ")
                            elif option2 == "20":
                                os.system("apt install ")
                            elif option2 == "21":
                                print("Regripper is unavailable")
                            elif option2 == "22":
                                os.system("apt install ")
                            elif option2 == "23":
                                os.system("apt install ")
                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            elif option2 == "0":
                                os.system(
                                    "apt install -y binwalk bulk-extractor chntpw dc3dd ddrescue dumpzilla extundelete \
									foremost galleta guymager p0f pdf-parser pdfid"
                                )
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m"
                                )

                        while option1 == "10":
                            print(
                                """
								\033[1;35m=+[ Stress Testing\033[1;m
								1) DHCPig
								2) FunkLoad
								3) iaxflood
								4) Inundator
								5) inviteflood	
								6) ipv6-toolkit
								7) mdk3
								8) Reaver
								9) rtpflood
								10) SlowHTTPTest
								11) t50
								12) Termineter
								13) THC-IPV6
								14) THC-SSL-DOS 		
								0) Install all Stress Testing tools\n
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "1":
                                os.system("apt install dhcpig")
                            elif option2 == "2":
                                os.system("apt install ")
                            elif option2 == "3":
                                os.system("apt install iaxflood")
                            elif option2 == "4":
                                os.system(
                                    "apt install git && git clone git://git.kali.org/packages/inundator.git"
                                )
                            elif option2 == "5":
                                os.system("apt install inviteflood")
                            elif option2 == "6":
                                os.system("apt install ipv6-toolkit")
                            elif option2 == "7":
                                os.system("apt install mdk3")
                            elif option2 == "8":
                                os.system("apt install reaver")
                            elif option2 == "9":
                                os.system("apt install rtpflood")
                            elif option2 == "10":
                                os.system("apt install slowhttptest")
                            elif option2 == "11":
                                os.system("apt install t50")
                            elif option2 == "12":
                                os.system("apt install termineter")
                            elif option2 == "13":
                                os.system("apt install thc-ipv6")
                            elif option2 == "14":
                                os.system("apt install thc-ssl-dos ")
                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            elif option2 == "0":
                                os.system(
                                    "apt install -y dhcpig iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood \
									slowhttptest t50 termineter thc-ipv6 thc-ssl-dos"
                                )
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m"
                                )

                        while option1 == "11":
                            print(
                                """
								\033[1;35m=+[ Password Attacks\033[1;m
								1) 				19) Maskprocessor
								2) Burp Suite				20) 
								3) CeWL				21) Ncrack
								4) chntpw				22) 
								5) cisco-auditing-tool			23) PACK
								6) CmosPwd				24) patator
								7) 				25) phrasendrescher
								8) crunch				26) polenum
								9) DBPwAudit				27) RainbowCrack
								10) 				28) rcracki-mt
								11) gpp-decrypt				29) RSMangler
								12) hash-identifier			30) SQLdict
								13) HexorBase				31) Statsprocessor
								14) THC-Hydra				32) THC-pptp-bruter
								15) John the Ripper			33) TrueCrack
								16) Johnny				34) WebScarab 
								17) 				35) wordlists 
								18) Maltego Teeth			36) zaproxy 
								0) Install all Password Attacks tools\n
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "2":
                                os.system("apt install burpsuite")
                            elif option2 == "3":
                                os.system("apt install cewl")
                            elif option2 == "4":
                                os.system("apt install chntpw")
                            elif option2 == "5":
                                os.system("apt install cisco-auditing-tool")
                            elif option2 == "6":
                                os.system("apt install ")
                            elif option2 == "7":
                                os.system("apt install ")
                            elif option2 == "8":
                                os.system("apt install crunch")
                            elif option2 == "9":
                                os.system(
                                    "apt install git && git clone git://git.kali.org/packages/dbpwaudit.git"
                                )
                            elif option2 == "10":
                                os.system("apt install ")
                            elif option2 == "11":
                                os.system("apt install gpp-decrypt")
                            elif option2 == "12":
                                os.system("apt install hash-identifier")
                            elif option2 == "13":
                                os.system("apt install ")
                            elif option2 == "14":
                                os.system(
                                    "echo 'please visit : https://www.thc.org/thc-hydra/' "
                                )
                            elif option2 == "15":
                                os.system("apt install john")
                            elif option2 == "16":
                                os.system("apt install johnny")
                            elif option2 == "17":
                                os.system("apt install ")
                            elif option2 == "18":
                                os.system("apt install maltego-teeth")
                            elif option2 == "19":
                                os.system("apt install maskprocessor")
                            elif option2 == "20":
                                os.system("apt install ")
                            elif option2 == "21":
                                os.system("apt install ncrack")
                            elif option2 == "22":
                                os.system("apt install ")
                            elif option2 == "23":
                                os.system("apt install pack")
                            elif option2 == "24":
                                os.system("apt install patator")
                            elif option2 == "25":
                                os.system(
                                    "echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml'"
                                )
                            elif option2 == "26":
                                os.system("apt install polenum")
                            elif option2 == "27":
                                os.system("apt install ")
                            elif option2 == "28":
                                os.system("apt install rcracki-mt")
                            elif option2 == "29":
                                os.system("apt install rsmangler")
                            elif option2 == "30":
                                print("Sqldict is unavailable")
                            elif option2 == "31":
                                os.system("apt install statsprocessor")
                            elif option2 == "32":
                                os.system("apt install thc-pptp-bruter")
                            elif option2 == "33":
                                os.system("apt install truecrack")
                            elif option2 == "34":
                                os.system("apt install webscarab")
                            elif option2 == "35":
                                os.system("apt install wordlists")
                            elif option2 == "36":
                                os.system("apt install zaproxy")
                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            elif option2 == "0":
                                os.system(
                                    "apt install -y burpsuite cewl chntpw cisco-auditing-tool crunch gpp-decrypt \
									hash-identifier john johnny maltego-teeth maskprocessor ncrack pack patator \
									polenum rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab \
									wordlists zaproxy"
                                )
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m"
                                )

                        while option1 == "12":
                            print(
                                """
								\033[1;35m=+[ Reverse Engineering\033[1;m
								1) apktool
								2) dex2jar
								3) diStorm3
								4) 
								5) 	
								6) javasnoop
								7) jdim-GUI
								8) OllyDbg
								9) smali
								10) Valgrind
								11) YARA
								0) Install all Reverse Engineering tools\n
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "1":
                                os.system("apt install apktool")
                            elif option2 == "2":
                                os.system("apt install dex2jar")
                            elif option2 == "3":
                                os.system("apt install python-diStorm3")
                            elif option2 == "4":
                                os.system("apt install ")
                            elif option2 == "5":
                                os.system("apt install ")
                            elif option2 == "6":
                                os.system("apt install javasnoop")
                            elif option2 == "7":
                                os.system("apt install jdim")
                            elif option2 == "8":
                                os.system("apt install OllyDbg")
                            elif option2 == "9":
                                os.system("apt install smali")
                            elif option2 == "10":
                                os.system("apt install Valgrind")
                            elif option2 == "11":
                                os.system("apt install YARA")
                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            elif option2 == "0":
                                os.system(
                                    "apt install -y apktool dex2jar python-diStorm3 javasnoop jdim OllyDbg smali \
									Valgrind YARA"
                                )
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m"
                                )

                        while option1 == "13":
                            print(
                                """
								\033[1;35m=+[ Hardware Hacking\033[1;m
								1) android-sdk
								2) apktool
								3) Arduino
								4) dex2jar
								5) Sakis3G	
								6) smali
								0) Install all Hardware Hacking tools\n
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "1":
                                os.system("apt install android-sdk")
                            elif option2 == "2":
                                os.system("apt install apktool")
                            elif option2 == "3":
                                os.system("apt install ")
                            elif option2 == "4":
                                os.system("apt install dex2jar")
                            elif option2 == "5":
                                os.system("apt install sakis3g")
                            elif option2 == "6":
                                os.system("apt install smali")

                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()
                            elif option2 == "0":
                                os.system(
                                    "apt install -y android-sdk apktool  dex2jar sakis3g smali"
                                )
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m"
                                )

                        while option1 == "14":
                            print(
                                """
								\033[1;35m=+[ Extra\033[1;m
								1) Wifresti
								2) Squid3
								"""
                            )
                            print(
                                "\033[1;35mInsert the number of the tool to install it .\n\033[1;m"
                            )
                            option2 = input("\033[1;35mkat > \033[1;m")
                            if option2 == "1":
                                os.system(
                                    "git clone https://github.com/LionSec/wifresti.git && \
									cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti"
                                )
                                print(" ")
                            elif option2 == "2":
                                os.system("apt install squid3")
                                print(" ")
                            elif option2 == "back":
                                init()
                            elif option2 == "gohome":
                                init1()

                init()

        init1()
    except KeyboardInterrupt:
        print("Shutdown requested...Goodbye...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


def install_packages(packages="all"):
    # Exceptions
    if packages in ["all", "bing-ip2hosts"] or "bing-ip2hosts" in packages:
        os.system(
            "wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && \
            tar -xzvf bing-ip2hosts-0.4.tar.gz && \
            cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/"
        )

        packages[packages.index("bing-ip2hosts")]

    # System/repo packages
    prefix = "apt install -y"
    package_list = ""

    for i in packages:
        package_list += f"{i} "

    os.system(f"{prefix} {package_list}")

def read_packages(file_name):
    with open(f"package_lists/{file_name}", "r") as f:
        return f.read().splitlines()

if __name__ == "__main__":
    main()

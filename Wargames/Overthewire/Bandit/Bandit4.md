# [Bandit4](http://overthewire.org/wargames/bandit/bandit4.html)

Exit the previous ssh and enter in as bandit3 now, using the password we obtained from last level.

```
exit
ssh bandit3@bandit.labs.overthewire.org -p 2220
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

The password for the next level is stored in a hidden file in the directory 'inhere'. First cd into this directory. After this, trying a normal
ls lists nothing. This is a good time to consult the manual page of ls, by typing man ls. We see here that there is an option for showing
all entries, using -a. Now, let's use ls -a and see what we find.

```
cd inhere
ls
man ls
ls -a
```

We see from this that there is a file called .hidden. We are not sure what type of file it is, so let's use the file command to see what it is.

```
file .hidden
.hidden: ASCII text
```

This is just a text file, so let's print it out and see what we find.

```
cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

Voilah! There's the password for the next level.

*That's all for this level!*

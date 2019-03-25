# [Bandit3](http://overthewire.org/wargames/bandit/bandit3.html)

Exit the previous ssh and enter in as bandit3 now, using the password we obtained from last level.

```
exit
ssh bandit2@bandit.labs.overthewire.org -p 2220
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

The password for the next level is stored in a file named 'spaces in this filename'. In Linux commands, spaces are used as argument seperators.
As a result, we cannot do something like the below snippet.

```
cat spaces in this filename
```

The cat command will take the 'spaces' argument and the space indicates the end of the argument, so it doesn't know what to do with the commands after the space.
In order to combat this, linux allows us to escape characters using the '\'. Using '\' before a character tells the commandline to ignore the next
character. Thus, use the command:

```
cat spaces\ in\ this\ filename
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

## Quick Tip!
Using tab auto finishes the command for a filename, given no other similar path names. Thus, if we type in just 'cat spac' and then hit tab, 
the command will autofill the rest of the command to the one above. This is very useful for filenames that have spaces or are long!

*That's all for this level!*

# [Bandit2](http://overthewire.org/wargames/bandit/bandit2.html)

Exit the previous ssh and enter in as bandit1 now, using the password we obtained from last level.

```
exit
ssh bandit1@bandit.labs.overthewire.org -p 2220
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

The password for the next level is stored in a file named '-'. You may be tempted to use a command such as

```
cat -
```

However, this will not work as - is used for other functions, like stdin. In order to fool our cat command into looking at this file, we neeed
to give the cat command the file path to the file. A period followed by a backslash indicates current directory, so we can have a cat command using
the path that looks like this:

```
cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```
*That's all for this level!*

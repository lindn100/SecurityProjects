1
`cat readme`

2
`cat ./-`

3
`cat spaces\ in\ this\ filename` 

4
```cd inhere
ls -a
cat .hidden```

5
```file ./-file07
cat ./-file07```

6
```find . -type f -size 1033c -name "[[:print:]]*" ! -executable
cat ./maybehere07/.file2```

7
```find / -user bandit7 -group bandit6 -size 33c 2> /dev/null
cat /var/lib/dpkg/info/bandit7.password```

8
`cat data.txt | grep "millionth"`

9
`sort data.txt | uniq -u`

10
`strings data.txt | grep =`

11
`cat data.txt | base64 --decode`

12
`cat data.txt | tr a-zA-Z n-za-mN-ZA-M`

13
```xxd -r data.txt > newFile
file newFile
mv newFile newFile.gz
funzip newFile.gz
file newFile
mv newFile newFile.bz2
bzip2 -d newFile.bz2
file newFile
mv newFile newFile.gz
gunzip newFile.gz
file newFile
mv newFile newFile.tar
tar xvf newFile.tar
file data5.bin
mv data5.bin data5.tar
tar xvf data5.tar
mv data6.bin data6.tar
tar xvf data6.tar
mv data8.tar data8.gz
gunzip data8.gz
file data8
cat data8```

14


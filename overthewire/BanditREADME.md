# OverTheWire Bandit Walkthrough

*A personal walkthrough of the Bandit wargame from OverTheWire.*

Bandit is a cybersecurity wargame designed to teach Linux fundamentals,
networking, cryptography basics, and security concepts through hands‑on
challenges.

------------------------------------------------------------------------

# Skills Demonstrated

-   Linux command line usage
-   File permissions and hidden files
-   Text processing (`grep`, `sort`, `uniq`, `strings`)
-   File discovery (`find`, `stat`)
-   Encoding and decoding (Base64, ROT13)
-   Working with compressed archives (`gzip`, `bzip2`, `tar`)
-   Networking tools (`nc`, `openssl`, port scanning)
-   SSH authentication and key usage
-   Cron jobs and automation
-   Privilege escalation concepts
-   Git repository investigation

------------------------------------------------------------------------

# Bandit Levels Summary

## Bandit 0 → 1

**Concept:** Reading files in Linux

``` bash
cat readme
```

The password for the next level is stored inside a file called `readme`.

------------------------------------------------------------------------

## Bandit 1 → 2

**Concept:** Handling filenames beginning with `-`

``` bash
cat ./-
```

Using `./` prevents the shell from interpreting `-` as stdin.

------------------------------------------------------------------------

## Bandit 2 → 3

**Concept:** Filenames containing spaces

``` bash
cat "./--spaces in this filename--"
```

Quotes allow the shell to treat the entire string as one filename.

------------------------------------------------------------------------

## Bandit 3 → 4

**Concept:** Hidden files

``` bash
cd inhere
ls -a
cat "...Hiding-From-You"
```

Files starting with `.` are hidden unless `ls -a` is used.

------------------------------------------------------------------------

## Bandit 4 → 5

**Concept:** Identifying readable files

``` bash
cd inhere
cat ./-file07
```

Only one file contains readable ASCII text.

------------------------------------------------------------------------

## Bandit 5 → 6

**Concept:** Searching files using `find`

``` bash
find . -maxdepth 2 -type f ! -executable -exec stat -c "%s %n" {} + | sort -r
```

The password file has specific attributes like size and permissions.

------------------------------------------------------------------------

## Bandit 6 → 7

**Concept:** Searching the filesystem

``` bash
find / -user bandit7 -group bandit6 -size 33c
```

Filters allow searching by owner, group, and file size.

------------------------------------------------------------------------

## Bandit 7 → 8

**Concept:** Searching text using `grep`

``` bash
grep "millionth" data.txt
```

The password appears next to the keyword **millionth**.

------------------------------------------------------------------------

## Bandit 8 → 9

**Concept:** Sorting and removing duplicates

``` bash
sort data.txt | uniq -u
```

The password is the only unique line in the file.

------------------------------------------------------------------------

## Bandit 9 → 10

**Concept:** Extracting readable strings

``` bash
strings data.txt
```

Binary files can contain readable ASCII sequences.

------------------------------------------------------------------------

## Bandit 10 → 11

**Concept:** Base64 decoding

``` bash
base64 -d data.txt
```

The data is Base64 encoded.

------------------------------------------------------------------------

## Bandit 11 → 12

**Concept:** ROT-style substitution cipher

``` bash
cat data.txt | tr "T-ZA-St-za-s" "G-ZA-Fg-za-f"
```

Characters are rotated to reveal the plaintext.

------------------------------------------------------------------------

## Bandit 12 → 13

**Concept:** File identification and compression

Tools used: - `xxd` - `file` - `gunzip` - `bzip2` - `tar`

The file must be repeatedly identified and extracted.

------------------------------------------------------------------------

## Bandit 13 → 14

**Concept:** SSH private key authentication

``` bash
scp -P 2220 bandit13@bandit.labs.overthewire.org:/home/bandit13/sshkey.private .
ssh -i sshkey.private -p 2220 bandit14@bandit.labs.overthewire.org
```

Login using a private SSH key instead of a password.

------------------------------------------------------------------------

## Bandit 14 → 15

**Concept:** Netcat networking

``` bash
echo PASSWORD | nc localhost 30000
```

Netcat sends the password to a TCP service.

------------------------------------------------------------------------

## Bandit 15 → 16

**Concept:** TLS connections

``` bash
openssl s_client -connect localhost:30001
```

The service requires a secure TLS connection.

------------------------------------------------------------------------

## Bandit 16 → 17

**Concept:** Port scanning

Multiple ports must be scanned to locate the one returning an SSH key.

------------------------------------------------------------------------

## Bandit 17 → 18

**Concept:** File comparison

``` bash
diff passwords.new passwords.old
```

The new password is the difference between the files.

------------------------------------------------------------------------

## Bandit 18 → 19

**Concept:** Executing commands over SSH

``` bash
ssh bandit18@server "cat readme"
```

Commands must be executed directly because the shell exits immediately.

------------------------------------------------------------------------

## Bandit 19 → 20

**Concept:** Setuid binaries

A provided binary runs with elevated privileges and reveals the
password.

------------------------------------------------------------------------

## Bandit 20 → 21

**Concept:** Network listeners

``` bash
nc -l localhost 29999
```

A listener waits for the password to be sent.

------------------------------------------------------------------------

## Bandit 21 → 22

**Concept:** Cron jobs

Scheduled scripts store the password in `/tmp`.

------------------------------------------------------------------------

## Bandit 22 → 23

**Concept:** Hashing

``` bash
echo I am user bandit23 | md5sum
```

The script hashes the username to determine the password file location.

------------------------------------------------------------------------

## Bandit 23 → 24

**Concept:** Cron privilege escalation

A script placed in the cron directory runs automatically and writes the
password to a readable file.

------------------------------------------------------------------------

## Bandit 24 → 25

**Concept:** Brute forcing

A script tests all PIN combinations against a service.

------------------------------------------------------------------------

## Bandit 25 → 26

**Concept:** Escaping restricted shells

Using `vim` allows spawning a new shell and bypassing restrictions.

------------------------------------------------------------------------

## Bandit 26 → 27

**Concept:** Running privileged binaries

A provided binary executes commands as another user.

------------------------------------------------------------------------

## Bandit 27 → 28

**Concept:** Git repositories

``` bash
git clone <repo>
```

The password is hidden in a repository.

------------------------------------------------------------------------

## Bandit 28 → 29

**Concept:** Git commit history

``` bash
git log
git show <commit>
```

Passwords can still exist in previous commits.

------------------------------------------------------------------------

## Bandit 29 → 30

**Concept:** Git branches

``` bash
git branch -a
```

The password is stored in another branch.

------------------------------------------------------------------------

## Bandit 30 → 31

**Concept:** Git tags

``` bash
git tag
git show secret
```

Sensitive data may be hidden in tags.

------------------------------------------------------------------------

## Bandit 31 → 32

**Concept:** Bypassing `.gitignore`

``` bash
git add key.txt -f
```

`-f` forces Git to add ignored files.

------------------------------------------------------------------------

## Bandit 32 → 33

**Concept:** Escaping restricted environments

``` bash
$0
```

Starting a new shell bypasses restrictions.

------------------------------------------------------------------------

# Conclusion

The Bandit wargame is an excellent introduction to practical
cybersecurity concepts such as:

-   Linux system navigation
-   Networking tools
-   Encoding and encryption basics
-   Privilege escalation
-   Git forensic analysis

Completing these challenges builds a strong foundation for penetration
testing and security engineering.

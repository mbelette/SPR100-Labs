2.) (response to ls -la) 

 stat secret.txt
total 20
drwxrwxr-x 3 mbelette mbelette 4096 Mar 17 22:40 .
drwxrwxr-x 3 mbelette mbelette 4096 Mar 17 22:40 ..
-rw-rw-r-- 1 mbelette mbelette   11 Mar 17 22:40 notes.txt
drwxrwxr-x 3 mbelette mbelette 4096 Mar 17 22:40 projects
-rw-rw-r-- 1 mbelette mbelette   46 Mar 17 22:40 secret.txt
  File: secret.txt
  Size: 46        	Blocks: 8          IO Block: 4096   regular file
Device: 803h/2051d	Inode: 2886791     Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/mbelette)   Gid: ( 1000/mbelette)
Access: 2026-03-17 22:40:07.658807025 -0400
Modify: 2026-03-17 22:40:07.658807025 -0400
Change: 2026-03-17 22:40:07.658807025 -0400
 Birth: 2026-03-17 22:40:07.658807025 -0400
mbelette@mbelette-virtual-ma 







3.) total 20
drwxrwxr-x 3 mbelette mbelette 4096 Mar 17 22:40 .
drwxrwxr-x 3 mbelette mbelette 4096 Mar 17 22:40 ..
-rw-r--r-- 1 mbelette mbelette   11 Mar 17 22:40 notes.txt
drwxr-x--- 3 mbelette mbelette 4096 Mar 17 22:40 projects
-rw------- 1 mbelette mbelette   46 Mar 17 22:40 secret.txt

(response to: chmod 600 secret.txt # Only YOU can read/write chmod 644 notes.txt # You read/write; others only read chmod 750 projects # You have full access; group can enter chmod 750 projects/teamA # Locked down for traversal ls -la)


4.) (response to: Sudo -u fsuser bash -c ‘cat /home/mbelette/SPR100_Labs/Lab04/work/secret.txt || echo “denied”)  

Cat: /home/mbelette/SPR100_Labs/Lab04/work/secret.txt: Permission denied 
denied





5.) (response to: setfacl -m u:fsuser:r-- secret.txt) 

6.) (response to: getfacl secret.txt) 

# file: secret.txt
# owner: mbelette
# group: mbelette
User: : rw-
User: fsuser:r - -
Group:: - - -
Mask:: r - -
Other: : - - -





7.) (response to: sudo -u fsuser bash -c 'cat /home/mbelette/SPR100_Labs/Lab04/work/secret.txt && echo OK') 



Cat: /home/mbelette/SPR100_Labs/Lab04/work/secret.txt: Permission denied



8.) (response to: sudo -u fsuser bash -c 'echo "hacked" >> /home/mbelette/SPR100_Labs/Lab04/work/secret.txt || echo "write denied"') 

Bash: line 1: /home/mbelette/SPR100_Labs/Lab04/work/secret.txt: Permission denied write denied



9.) (response to: chmod 751 /home/mbelette/SPR100_Labs/Lab04/work
setfacl -m u:fsuser:x /home/mbelette)

10.) response to: sudo -u fsuser cat /home/mbelette/SPR100_Labs/Lab04/work/secret.txt && echo "SUCCESS": 


confidential : Tue 17 Mar 2026 10:40:07 PM EDT SUCCESS




11.) response to: zip -r secure_bundle.zip projects
openssl enc -aes-256-cbc -salt -in secure_bundle.zip -out secure_bundle.zip.enc

Opsnssl enc -aes-256-cbc -salt  -in secure_ 
Adding: projects/ (stored 0%)
Adding: projects/teamA/ (stored 0%)

Enter AES-256-CBC encryption password: (i proceeded to put in my password) 


12.) (response to:  shred -u secure_bundle.zip)



13.) response to: setfattr -n user.note -v "confidential" notes.txt
getfattr -d notes.txt

14.) response to (zip -r secure_bundle.zip projects): 

Adding: projects/ (stored 0%)
Adding: projects/teamA/ (stored 0%) 





15.) (response to openssl enc -aes-256-cbc -salt -in secure_bundle.zip -out secure_bundle.zip.enc) 

Enter AES-256-CBC encryption password: 
Verifying - enter AES-256-CBC encryption password: 

*** WARNING : deprecated key derivation used.

Using -iter or -pbkdf2 would be better.

16.) (response to: shred -u secure_bundle.zip
ls -l secure_bundle.zip.enc) 

-rw-rw-r - - 1 mbelette mbelette 352 Mar 17 23:08 secure_bundle.zip.enc


REFLECTION SECTION

1.) When are ACLs preferred over standard permissions?
When you need to give a specific user access to a file without creating a whole new system group or changing permissions for everyone else.


2.) How does the ACL mask affect effective permissions?
It acts like a ceiling. Even if you give a user full rwx access, if the mask is set to r--, the user will only actually have Read access.

3.) Why is the execute (x) bit required on directories?
In Linux the x bit on a folder doesn't mean run a program. Instead, it means traversal. You need it to pass through a folder to reach the files or subfolders inside.

4.) What are the risks of using ad-hoc encryption like OpenSSL?
Losing the password. Data isn't recoverable if it's lost. Also, ad-hoc encryption often strips away metadata from the original file.



# Hash Crack

**Identify and crack a given hash**

Python scripts to identify a given hash and crack it with your specified wordlist and hash type.

*Thanks to Blackploit for the hash identification algorithm:*

[Hash-id - Github](https://github.com/blackploit/hash-identifier)

## Usage:

python hashcracker.py [/wordlist/path] [password hash]

### Example:

The md5 value for "armenia" is "3744c623dc4219b00a900ee527c16387"

<pre>echo -n "armenia" | md5sum</pre>

To crack this hash:

<pre>python hashcracker.py wordlist.txt a00c273f0f497484093fa94865cf5ca5</pre>

![Start](https://imgur.com/VyHeQll.png)

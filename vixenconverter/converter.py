#!/usr/bin/env python3

from docopt import docopt
import json
import os
from vixenfiles import VixenSequence,VixenProfile

help_message = """Proton - Vixen Converter

Usage:
    converter.py import-sequence <proton-path> <admin-key> <seq-file> <audio-file> <layout-id>
    converter.py import-layout <proton-path> <pro-file>
    converter.py --version
    converter.py (-h | --help)

Options:
    --version   Show version
    -h --help   Show this message
"""


def add_seq_to_proton_cli(proton_path, seq, seq_file, key_file, audio_file, layout_id):
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


def add_layout_to_proton_cli(proton_path, layout_file):
    # new-layout <layout-file>
    os.execl(proton_path, 'proton', 'new-layout', layout_file)


def import_profile(proton_path, pro_file):
    # Get profile
    pro = VixenProfile.make_vixen_profile(pro_file)
    channels = pro.get_channels()
    # Write layout data as JSON to file
    layout = {
        'layoutName': pro.name,
        'channels': channels
    }
    layout_json = json.dumps(layout)
    layout_file_name = pro.name + "_layout.json"
    ofile = open(layout_file_name, mode='w')
    ofile.write(layout_json)
    # Add to proton-cli
    add_layout_to_proton_cli(proton_path, layout_file_name)


def import_sequence(proton_path, seq_file, key_file, audio_file, layout_id):
    # Get sequence
    seq = VixenSequence.make_vixen_sequence(seq_file)
    seq_metadata = seq.get_metadata()
    # Write sequence data as JSON to file
    seq_json = json.dumps(seq.events.tolist())
    ofile_name = seq_metadata['title'] + ".json"
    ofile = open(ofile_name, mode='w')
    ofile.write(seq_json)
    # Add to proton-cli
    add_seq_to_proton_cli(proton_path, seq, ofile_name, key_file, audio_file, layout_id)


def run():
    arguments = docopt(help_message, version='Vixen Converter 0.0.1')
    if arguments['import-sequence']:
        proton_path = arguments['<proton-path>']
        seq_file = arguments['<seq-file>']
        key_file = arguments['<admin-key>']
        audio_file = arguments['<audio-file>']
        layout_id = arguments['<layout-id>']
        import_sequence(proton_path, seq_file, key_file, audio_file, layout_id)
    else:
        proton_path = arguments['<proton-path>']
        pro_file = arguments['<pro-file>']
        import_profile(proton_path, pro_file)


if __name__ == '__main__':
    run()

#!/bin/sh

# import-sequences.py <proton-path> <admin-key> <layout-id>

set -o nounset
set -o errexit

dir="$HOME/Dropbox/Sequencing 2016/Sequencing/Sequence Data/Sequences"
seq_dir="$dir/Sequences"
audio_dir="$dir/Audio"

declare -a seqs audio

seqs=( \
  "(1) Jingle Breaks.vix" \
  "(2) Feel Good.vix" \
  "(3) Collide.vix" \
  "(4) Unicorn Adventure_Master.vix" \
  "(5) Glory to the Bells.vix" \
)

audio=( \
  "(1) Jingle Breaks.ogg" \
  "(2) Feel Good.ogg" \
  "(3) Collide.ogg" \
  "(4) Unicorn Adventure_Master.ogg" \
  "(5) Glory to the Bells.ogg" \
)

for i in {0..4}; do
  echo ./converter.py "$1" "$2" "$seq_dir/${seqs[$i]}" "$audio_dir/${audio[$i]}" "$3"
done

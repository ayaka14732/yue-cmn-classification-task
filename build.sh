#!/bin/sh
wget -nc -O cantonese.1.yaml https://raw.githubusercontent.com/ayaka14732/sentences/fix-1/legacy_dialogue/%E9%A6%99%E6%B8%AF/general.yaml
wget -nc https://raw.githubusercontent.com/CanCLID/sentences/main/qq_chat/henry.txt
rm -rf test.text.txt test.label.txt
python build_cantonese.py
wget -nc https://raw.githubusercontent.com/zake7749/Gossiping-Chinese-Corpus/master/data/Gossiping-QA-Dataset-2_0.csv
python build_mandarin.py

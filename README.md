# Cantonese/Mandarin Classification Task

The aim of this task is to classify texts into Cantonese and Mandarin. It is extremely useful for filtering Cantonese text from large-scale web crawling-based corpus.

## Test

```sh
python compute_accuracy.py output.txt
```

## Source

The Cantonese test data are extracted from [粵語對話語料](https://github.com/CanCLID/sentences).

The Mandarin test data are extracted from [PTT 八卦版問答中文語料](https://github.com/zake7749/Gossiping-Chinese-Corpus).

## Build

```sh
./build.sh
```

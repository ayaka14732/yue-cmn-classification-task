# Cantonese/Mandarin Classification Task

The aim of this task is to classify texts into Cantonese and Mandarin. It is extremely useful for filtering Cantonese text from large-scale web crawling-based corpus.

## Scores

| Model | Author | Accuracy |
| :- | :- | :- |
| [Cantonese text classifier](https://github.com/CanCLID/cantonese-classifier) | CanCLID | 82.49% |

Please update this list if you have built your own model.

## Test

```sh
python compute_accuracy.py output.txt
```

## Source

The Cantonese test data are extracted from [粵語對話語料](https://github.com/CanCLID/sentences).

The Mandarin test data are extracted from [PTT 八卦版問答中文語料](https://github.com/zake7749/Gossiping-Chinese-Corpus).

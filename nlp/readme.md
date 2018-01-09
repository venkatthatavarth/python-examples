# Example of Python with Natural-Language Processing

While getting started with Natural-Language Processing with Python, I found the `spacy` tool to be great. This is a set of simple examples that use `spacy` for simple NLP tasks.

## Prerequisites

* Python 2.7 and Pip.
* [`pipenv`](https://pypi.python.org/pypi/pipenv). Install it using `pip install pipenv`

## How to run

First download different English language models:

* `python -m spacy download en_core_web_sm`
* `python -m spacy download en_core_web_md`
* `python -m spacy download en_core_web_lg` (:exclamation: 1 GB in size!)

* Run using the `small` language model: `python 1.py sm`
* Run using `medium` language model: `python 1.py md`
* Run using `large` language model: `python 1.py lg`

(Language models are described below.)

## About different language models


### Model Size

* Different language models have different sizes, due to the number of datapoints loaded.
* Example sizes: `en_core_web_sm` is 37 MB, `en_core_web_md` model is 120 MB. `en_core_web_lg` is **1 GB+**.
* Larger models might also result in higher processing times (perhaps due to I/O).

### Model Accuracy

For two strings, `help me with devops` and `i need help with devops`, the accuracy using different models is shown below.

```
$ python 1.py sm
using model: sm
similarity: 0.7242523745572412

$ python 1.py md
using model: md
similarity: 0.9095811579120793

$ python 1.py lg
using model: lg
similarity: 0.9155825546433053
```

## References

1. https://spacy.io/usage/models
1. https://spacy.io/models/en#en_core_web_sm
1. https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv

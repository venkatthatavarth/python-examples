# Example of Python with Natural-Language Processing

While getting started with Natural-Language Processing with Python, I found the `spacy` tool to be great. This is a set of simple examples that use `spacy` for simple NLP tasks.

## Prerequisites

* Python 2.7 and Pip.
* [`pipenv`](https://pypi.python.org/pypi/pipenv). Install it using `pip install pipenv`

### Download `en` model for `Spacy`

Different language models have different levels of accuracy. The `lg` or large model is 1+ GB in size, but gives you good accuracy with your NLP work.

* `python -m spacy download en` will by-default download the `en_core_web_sm` model.
* `python -m spacy download en_core_web_lg` will download the `en_core_web_lg` model.

## References

1. https://spacy.io/usage/models
1. https://spacy.io/models/en#en_core_web_sm
1. https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv

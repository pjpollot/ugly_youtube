# Ugly Youtube

To cope with my addiction to Youtube, I coded a simple project in Python to fetch videos on Youtube. The aim is to reduce the influence of the suggestion algorithm so I can be more productive in my daily life rather than watching endlessly cat videos suggested for me by Youtube's algorithm. 

## Installation

The package uses Python 3.9 and can be installed with [Poetry](https://python-poetry.org/) package manager. To install it, run the following command on the root of the repository: 

```
$ poetry install
```

## Features

The package is still in WIP but the basic features are already implemented:
- From a search query, retrieve videos' data (links and titles).
- Print the results in HTML or Markdown.

Details about the use-case can be found in `main.py`. Besides, docstrings are also present to explain each component's functionality.

## Caution

Make sure to have an API key for Youtube API so you can run this project. If not, you can generate one from [here](https://console.cloud.google.com/).
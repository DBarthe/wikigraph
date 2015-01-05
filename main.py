#!/usr/bin/env python3

from sys import argv
from wikigraph.collector.fetcher import Fetcher, ArticleNotFound


article_name = argv[1] if len(argv) > 1 else "42"

fetcher = Fetcher()

try:
  print (fetcher.fetch(article_name))
except ArticleNotFound as err:
  print (err)
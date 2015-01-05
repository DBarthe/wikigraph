#!/usr/bin/env python3

from sys import argv
from wikigraph.collector.fetcher import Fetcher, ArticleNotFound
from wikigraph.collector.parser import LinkedArticleFinder

article_name = argv[1] if len(argv) > 1 else "42"

fetcher = Fetcher()

try:
  html = fetcher.fetch(article_name)
except ArticleNotFound as err:
  print (err)
  exit (1)

parser = LinkedArticleFinder()
parser.feed(html)
linked_article_table = parser.collect()

for article in linked_article_table:
  print (article)

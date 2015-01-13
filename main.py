#!/usr/bin/env python3

from sys import argv

from wikigraph.collector.fetcher import Fetcher, ArticleNotFound
from wikigraph.collector.parser import LinkedArticleFinder

from wikigraph.models.network import ArticleNetwork

start_article = argv[1] if len(argv) > 1 else "42"


network = ArticleNetwork()
fetcher = Fetcher()
parser = LinkedArticleFinder()
frange = set([start_article])
closed = set()

while len(frange) > 0:
  article = frange.pop()
  if article not in closed:
    print ("expanding", article)
    closed.add(article)
    network.add_article(article)
    try:
      html = fetcher.fetch(article)
      parser.cleanup()
      parser.feed(html)
      linked_articles = parser.collect()
      for link_dest in linked_articles:
        print ("\tadd link", link_dest)
        frange.add(link_dest)
        network.add_article(link_dest)
        network.add_link(article, link_dest)

    except ArticleNotFound as err:
      print (err)




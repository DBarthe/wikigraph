
from .graph import Graph

class ArticleNetwork:

  def __init__(self):
    self.graph = Graph()
    self.articles = {}

  def add_article(self, name):
    if name not in self.articles:
      key = self.graph.add_vertice()
      self.articles[name] = key

  def key_of(self, name):
    return self.articles[name]

  def name_of(self, key):
    for name, k in self.articles:
      if k == key:
        return name
    raise KeyError("ArticleNetwork")

  def add_link(self, src, dst):
    self.add_article(src), self.add_article(dst)
    key_src, key_dst = self.key_of(src), self.key_of(dst)
    try:
      self.graph.add_edge(key_src, key_dst)
    except ValueError:
      pass

  def get_links_generic(self, name, f):
    key = key_of(name)
    adjacents = f(key)
    return [name_of(k) for k in adjacents]

  def get_links_from(self, name):
    return get_links_generic(name, self.graph.get_adjacents_from)

  def get_links_to(self, name):
    return get_links_generic(name, self.graph.get_adjacents_to)

  def get_links(self, name):
    return get_links_generic(name, self.graph.get_adjacents)

  def exist(self, name):
    return name in self.articles
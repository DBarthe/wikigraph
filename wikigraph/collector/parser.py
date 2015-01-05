from html.parser import HTMLParser

class ParserBase(HTMLParser):

  def __init__(self, *arg, **kwarg):
    super().__init__(strict=False, *arg, **kwarg)


  def feed(self, html):
    super().feed(html)

  def collect(self):
    pass

  def cleanup(self):
    pass

class LinkFinder(ParserBase):

  def __init__(self, *arg, **kwarg):
    super().__init__(*arg, **kwarg)

    self.link_table = []

  def collect(self):
    return self.link_table

  def cleanup(self):
    self.link_table = []

  def handle_starttag(self, tag, attrs):
    if tag == 'a':
      self.link_table.append(attrs)


class LinkedArticleFinder(LinkFinder):

  """ Every links to article starts with this prefix. """
  article_url_prefix = "/wiki/"

  """ Skip articles which starts with one of the following. """
  boycotted_prefix_table = [
    "File:", "Special:", "Template:",
    "Template_talk:", "Category:", "Help:",
    "Wikipedia:"
  ]

  """ Stop looking for article links when this link is encountered. """
  terminating_link = "Help:Category"

  def __init__(self, *arg, **kwarg):
    super().__init__(*arg, **kwarg)


  def collect(self):

    link_table = super().collect()
    linked_article_table = []

    for link in link_table:
      """ Get the 'href' attribute. """
      url = next((value for name, value in link if name == "href"), None)

      """ Extract the article name. """
      if url is not None and url.startswith(self.article_url_prefix):
        (_, _, article_name) = url.partition(self.article_url_prefix)

        """ Decide what to do (terminate, append, or skip). """
        if article_name == self.terminating_link:
          break
        elif not any(map(
          lambda s: article_name.startswith(s), self.boycotted_prefix_table)):
            linked_article_table.append(article_name)

    return linked_article_table



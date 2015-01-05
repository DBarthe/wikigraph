from urllib.request import urlopen
from urllib.error import HTTPError


class FetchError(Exception):
  def __init__(self, *arg, **kwarg):
    super().__init__(*arg, **kwarg)

  def __str__(self):
    return 'Fetch error'

class ArticleNotFound(FetchError):

  def __init__(self, name, *arg, **kwarg):
    super().__init__(*arg, **kwarg)
    self.name = name

  def __str__(self):
    return "{0}: article '{1}' is not found.".format(super().__str__(), self.name)

class Fetcher:

  """
  Default values.
  There are easily modifiable for one particular instance.
  For example: instance.lang = "fr"
  """
  protocol = "http"
  host = "wikipedia.org"
  article_url_prefix = '/wiki/' 
  lang = "en"

  def fetch(self, article_name):
    url = self.protocol + "://" + self.lang + "." + self.host \
        + self.article_url_prefix + article_name

    try:
      response = urlopen(url)
    except HTTPError:
      raise ArticleNotFound(article_name)

    return str(response.read())


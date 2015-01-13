import itertools

class Graph:
  """ A basic graph class. """

  def __init__(self):
    """ A matrix vertice x edges. """    
    self.vertices = []

  """ Gets the number of vertices. """ 
  def order(self):
    return len(self.vertices)

  """ Gets the number of edges. """
  def size(self):
    return sum((len(edges) for edges in self.vertices))

  """ Gets the number of edges that connect a vertice.
  'Loop' edges are counted twice. """
  def degree(self, key):
    check_key(self.check_key)
    edges = self.vertices[key]
    from_nbr = len(edges)
    to_nbr = sum(len([k for k in edges if k == key]) for edges in self.vertices)
    return from_nbr + to_nbr

  """ Adds a vertice to the grah. Returns its key. """
  def add_vertice(self):
    index = len(self.vertices)
    self.vertices.append([])
    return index

  """ Adds all vertices contained in an iterable.
  Returns their keys in an array. """
  def add_vertices(self, iterable):
    return [ self.add_vertice() for value in iterable ]

  """ Private. Check the validity of the key
  Raise an exception if necessary. """
  def check_key(self, key):
    if key < 0 or key >= len(self.vertices):
      raise IndexError("Graph: invalid vertice key.")

  """ Add an edge in the graph. """
  def add_edge(self, key_from, key_to, allow_loop=False):
    self.check_key(key_from)
    self.check_key(key_to)

    edges = self.vertices[key_from]

    if key_to in edges:
      raise ValueError("Graph: edge already exists.")

    if not allow_loop and key_from in edges:
      raise ValueError("Graph: loop edge unallowed.")

    edges.append(key_to)
    
  """ Add several edges contained in an array of couple. """
  def add_edges(self, iterable, *args, **kwargs):
    for key_from, key_to in iterable:
      self.add_edge(key_from, key_to, *args, **kwargs)


  def get_adjacents_from(self, key):
    check_key(key)
    return [k for k in self.vertices[key] if k != key]

  def get_adjacents_to(self, key):
    check_key(key)
    results = []
    for k, edges in enumerate(self.vertices):
       if k != key and key in edges:
          result.append(k)
    return result

  def get_adjacents(self, key):
    return list( \
      itertools.chain(self.get_adjacents_to(),
      self.get_adjacents_from()))
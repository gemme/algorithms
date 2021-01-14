class QuickUnionUF:
  def __init__(self, N):
    self.id = [i for i in range(N)]

  def _root(self, i):
    while(i is not self.id[i]):
      i = self.id[i]
    return i

  def connected(self, p, q):
    return self._root(p) == self._root(q)

  def union(self, p, q):
    i = self._root(p)
    j = self._root(q)
    self.id[i] = j



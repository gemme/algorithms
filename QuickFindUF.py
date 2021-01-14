class QuickFindUF:

  def __init__(self, N):
    self.id = [i for i in range(N)]

  def connected(self, p, q):
    return self.id[p] == self.id[q]

  def union(self, p, q):
    pid = id[p]
    qid = id[q]

    for(i in range(len(id))):
      if(id[i] == pid):
        id[i] = qid

  def print_id(self):
    print(self.id)

qF = QuickFindUF(10)
qF.print_id()
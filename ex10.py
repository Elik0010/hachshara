import scipy as sc

def distances(mat):
  print(sc.spatial.distance.pdist(mat))  
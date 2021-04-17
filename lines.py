#import pandas as pd

#df = pd.read_csv('/home/lisi/Desktop/SeminarStuff/3Cluster/Hierarchical/log_c4_pca_hierarchical.csv')

point1 = (13.91353, -1.06956, 2.444708)
point2 = (5.268935, 1.645602, 1.690951)

def vectordiff(pa, pb):
	pa1, pa2, pa3 = pa
	pb1, pb2, pb3 = pb
	return (pa1-pb1, pa2-pb2, pa3-pb3)

def crossprod(pa, pb):
	pa1, pa2, pa3 = pa
	pb1, pb2, pb3 = pb
	return ((pa2 * pb3) - (pa3 * pb2),(-1) * ((pa1 * pb3) - (pa3 * pb1)), (pa1 * pb2) - (pa2 * pb1))

def norm(pa):
	pa1, pa2, pa3 = pa
	return (pa1**2 + pa2**2 + pa3**2)**0.5

def distance(pa, pb, q):
	return norm(crossprod(vectordiff(pb, pa), vectordiff(pa, q))) / norm(vectordiff(pb,pa)) 


import sklearn # conda install scikit-learn  // pip install -U scikit-learn
from sklearn.manifold import Isomap
from sklearn.decomposition import PCA
import json
from pathlib import Path
import fire  # pip install fire 
import numpy as np 


def vec_pca(vectors_dict):
	pca = PCA(n_components=2)
	keys = list(vectors_dict.keys())
	vec2d = dic2arr2d(vectors_dict)
	pca_xys = pca.fit_transform(vec2d)
	return arr2d2dic(pca_xys, keys)


def vec_isomap(vectors_dict):
	iso = Isomap(n_components=2, n_neighbors=5)
	keys = list(vectors_dict.keys())
	vec2d = dic2arr2d(vectors_dict)
	iso_xys = iso.fit_transform(vec2d)
	
	return arr2d2dic(iso_xys, keys)

def dic2arr2d(dat):
	arrs = [vec for vec in dat.values()]
	return np.stack(arrs)

def arr2d2dic(arr2d, keys):
	assert len(keys)==len(arr2d)
	resdict = {}
	for i, key in enumerate(keys):
		resdict[key] = arr2d[i].tolist()
	return resdict



def str2float(raw_dat):
	dat = dict.fromkeys(raw_dat.keys())
	for key in dat:
		val = [float(i) for i in raw_dat[key]]
		dat[key] = val 

	return dat 

def main(filepath= 'thumbnail_net/thumbnail_vector.json', 
		 algorithm= 'pca', newfilename= None ):
	'''
	kwargs: 
	--filepath [filepath]
	--algorithm [pca, isomap]
	--newfilename [type what you want: not necessary]
	'''
	write_name = f'{algorithm}.json' if newfilename is None else f'{algorithm}_{newfilename}.json'

	filepath = Path(filepath)
	write_name = Path(write_name)

	with filepath.open() as f:
		raw = json.load(f)
		dat = str2float(raw)
	reduction_alg = {'pca': vec_pca, 'isomap': vec_isomap}
	func= reduction_alg[algorithm]
	result2d_dict = func(dat)

	with write_name.open(mode='w') as f:
		json.dump(result2d_dict, f)

	print(f"\n\nDONE!\n{str(filepath)} is processed with {algorithm} and saved to {write_name}")



if __name__ == '__main__':
	usage = '''usage:\npython vec2pca_isomap \n[\n\t--filepath thumbnailjsonPATH.json \n\t--algorithm pca or isomap (default pca) \n\t--newfilename NAME_YOU_WANT(not necessary)\n]'''
	print(usage)	
	fire.Fire(main)








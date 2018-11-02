all: QualtricsData.ipynb
	jupyter nbconvert QualtricsData.ipynb --to html --template full > index.html

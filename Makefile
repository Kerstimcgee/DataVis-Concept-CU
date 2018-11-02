all: QualtricsData.ipynb
	jupyter nbconvert QualtricsData.ipynb --to html --template full > QualtricsData.html

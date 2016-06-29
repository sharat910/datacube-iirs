import os,glob

def get_archive_path(path):
	for i in range(1,len(path)):
		if path[-1*i] == "/":
			break
	new_path = path[:i*-1] + "/archive"
	return new_path	

def get_cache_path(filename):
	return filename[:filename.index("archive")] + "cache"

def move_into_archive(files,destination):
	for file in files:
		compfile = file+".bz2"
		os.system("mv " + compfile + " " + destination)
	return

def move_into_cache(filename,destination):
	decompfile = filename[:-4]
	os.system("mv " + decompfile + " " + destination)
	return

def compress(path):
	files = glob.glob(str(path)+"/*.nc")	
	for file in files:		
		os.system("pbzip2 -zqf5 " + file)		

	new_path = get_archive_path(path)
	move_into_archive(files,new_path)
	return

def decompress(filename):
	os.system("pbzip2 -dqfk " + filename)
	move_into_cache(filename,get_cache_path(filename))

def getmethefile(filename):
	if os.path.isfile(filename):
		return 
	else:
		filename = filename.replace("cache","archive")
		decompress(filename + ".bz2")
		return

#path = str(input("Enter Path"))

#compress("/home/sharat910/IIRS/datacube/data/Landsat/tiles/LS8_OLI_LEDAPS")

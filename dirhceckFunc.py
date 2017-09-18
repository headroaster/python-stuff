def dircheck():
	if os.path.isdir(os.path.expanduser("~/Documents/Platypusses")):
		print ("the dir IS")
	else:
		print ("the dir WAS not")
		try:
			os.mkdir(os.path.expanduser("~/Documents/Platypusses"))
		except Exception:
			pass


def txtExtend(folder):
	for filename in os.listdir(folder):
	    infilename = os.path.join(folder,filename)
	    if not os.path.isfile(infilename): continue
	    oldbase = os.path.splitext(filename)
	    newname = infilename.replace('', '.txt')
	    output = os.rename(infilename, newname)


os.path.expanduser("~/Documents/notes")



def txtExtnd(folder):
	import glob, os
	for filename in glob.iglob(os.path.join(folder, '*.grf')):
    os.rename(filename, filename[:-4] + '.las')


def fileEnder(folder):
	for filename in folder:
	  base_file, ext = os.path.splitext(filename)
	  if ext == "":
	    os.rename(filename, base_file + ".txt")

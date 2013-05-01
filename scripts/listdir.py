import os

def recurdir():
	cwd=os.getcwd();
	dirlist=os.listdir(cwd)
	for i in dirlist:
		if(os.path.isdir(i)):
			os.chdir(cwd+'/'+i);
			recurdir()
			os.chdir(cwd);
		else:
			print(cwd+'/'+i)
			
recurdir()		
import os.path

os.chdir('main')
for current_dir, dirs, files in os.walk("."):
	if list(filter(lambda x: x.endswith('.py'), files)):
		print(os.path.relpath(current_dir, start='/Users/Julia/Downloads/'))
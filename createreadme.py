#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

HEADER = '''# T I L
> Today-I-Learned Repository

This is my 'Today-I-Learned' repository which is used to keep a record of whatever I learn in daily basis. 

![GitHub last commit](https://img.shields.io/github/last-commit/Pranav-Khurana/TIL.svg?color=blue&label=Last%20TIL&style=popout)
![Total TIL's](https://img.shields.io/badge/dynamic/json.svg?color=informational&label=Total%20TIL%27s&query=total_til&url=https%3A%2F%2Fraw.githubusercontent.com%2FPranav-Khurana%2FTIL%2Fmaster%2Fbadges.json)
'''

FOOTER = '''## Details
Want to know more about TIL repositories, see [Details.md](https://github.com/Pranav-Khurana/TIL/blob/master/Details.md) 
'''


''' Walk the current directory and get a list of all subdirectories at that
level.  These are the "categories" in which there are TILs. '''
def get_category_list ():
	dirs = [x for x in os.listdir ('.') if os.path.isdir (x) and '.git' not in x]
	return dirs

''' Read the file until we hit the first line that starts with a #
indicating a title in markdown.  We'll use that as the title for this
entry. '''
def get_title (til_file):
	with open (til_file) as file:
		for line in file:
			line = line.strip ()
			if line.startswith ('#'):
				return line[1:].lstrip ()  # text after # and whitespace

''' For a given category, get the list of TIL titles. '''
def get_tils (category):
	til_files = [x for x in os.listdir (category)]
	titles = []
	for filename in til_files:
		fullname = os.path.join (category, filename)
		if (os.path.isfile (fullname)) and fullname.endswith ('.md'):
			title = get_title (fullname)
			# changing path separator for Windows paths
			# https://mail.python.org/pipermail/tutor/2011-July/084788.html
			titles.append ((title, fullname.replace (os.path.sep, '/')))
	return titles

def get_category_dict (category_names):
	categories = {}
	count = 0
	for category in category_names:
		titles = get_tils (category)
		categories[category] = titles
		count += len (titles)
	return (count, categories)

''' Now we have all the information, print it out in markdown format. '''
def print_file (category_names, categories):
	with open ('README.md', 'w') as file:
		file.write (HEADER)
		file.write ('''
    
---
## Categories

''')
		# print the list of categories with links
		for category in sorted (category_names):
			file.write ('* [{0}](#{1})\n'.format (category.capitalize (), category))

		if len (category_names) > 0:
			file.write ('''
      
---

''')

		# print the section for each category
		for category in sorted (category_names):
			file.write ('### {0}\n'.format (category.capitalize ()))
			file.write ('\n')
			tils = categories[category]
			for (title, filename) in sorted (tils):
				file.write ('- [{0}]({1})\n'.format (title, filename))
			file.write ('\n')

		if len (category_names) > 0:
			file.write ('''
      
---

''')
		file.write (FOOTER)


def print_BADGE (til):
	with open ('badges.json', 'w') as file:
		st = '{ "total_til" : ' + str(til) + '}'
		file.write('{0}'.format(st))

''' Create a TIL README.md file with a nice index for using it directly
		from GitHub. '''
def create_README ():
	category_names = get_category_list ()
	count, categories = get_category_dict (category_names)
	print_BADGE(count)
	print_file (category_names, categories)

if __name__ == '__main__':
	create_README ()
	os.system('git add README.md')
	os.system('git add badges.json')

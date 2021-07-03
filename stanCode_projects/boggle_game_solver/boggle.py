"""
File: boggle.py
Name: Ada Wang
----------------------------------------
This program help you search the letters of sequentially adjacent cubes.
And check if a word exists in the dictionary.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


dictionary = []
boggle = []
LEN_C = 4
LEN_R = 4


def main():
	"""
	This program help you search the letters of sequentially adjacent cubes.
	Check the word length, if the word starts with the alphabet in boggle, then append the word to the lst, new_dict.
	And use DFS method to search the valid word.
	"""
	global boggle
	####################
	boggle = import_letter()
	read_dictionary()
	new_dict = []
	# filter the word starts with the alphabets from boggle
	for i in range(len(dictionary)):
		if 4 <= len(dictionary[i]) <= 16:
			for j in range(LEN_R):
				for k in range(LEN_C):
					if dictionary[i].startswith(boggle[j][k]):
						new_dict.append(dictionary[i])
	start = time.time()
	dfs_search(new_dict)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def dfs_search(new_dict):
	"""
	This program help you search the letters of sequentially adjacent cubes.
	:param new_dict: list, filter the word starts with the alphabets from boggle
	:return end_list: list, the valid word searched by dfs method
	"""
	end_lst = []
	for r in range(LEN_R):
		for c in range(LEN_C):
			dfs_helper(r, c, [], '', end_lst, new_dict)
	print('There are ' + str(len(end_lst)) + ' words in total.')


def dfs_helper(r, c, visited, cur_word, end_lst, new_dict):
	"""
	:param r: row id, r = 0, 1, 2, 3
	:param c: column id, c = 0, 1, 2, 3
	:param visited: list, save the neighbors for a given co-ordinates that has been visited
	:param cur_word: str, the current word for searching
	:param end_lst: list, the valid word searched by dfs method
	:param new_dict: list, filter the word starts with the alphabets from boggle
	"""
	if (r, c) in visited:
		return
	letter = boggle[r][c]
	visited.append((r, c))
	cur_word += letter
	# the valid word found
	if has_prefix(cur_word, new_dict) == 'T' and len(cur_word) >= 4 and cur_word not in end_lst:
		print('Found: "' + cur_word + '"')
		end_lst.append(cur_word)
	if len(cur_word) > 2 and has_prefix(cur_word, new_dict) is None:  # check has_prefix
		pass
	else:
		neighbors = get_neighbors(r, c)
		for i in range(len(neighbors)):
			dfs_helper(neighbors[i][0], neighbors[i][1], visited[::], cur_word, end_lst, new_dict)


def get_neighbors(r, c):
	"""
	Fine the neighbors of the given word
	:param r: row id
	:param c: columns id
	:return n : return the neighbors for the co-ordinates (new_r,new_c)
	"""
	n = []
	for i in range(-1, 2, 1):  # neighbors
		for j in range(-1, 2, 1):  # neighbors
			new_r = r + i
			new_c = c + j
			if new_r == r and new_c == c:
				pass
			else:
				if 0 <= new_r < LEN_R:
					if 0 <= new_c < LEN_C:
						n.append((new_r, new_c))
	return n


def import_letter():
	"""
	Import 4 rows of letters, and check the format.
	This program is Case insensitive.
	:return boggle : list, the list put the letters
	"""
	for i in range(1, 5):
		row = check_format(input(str(i)+' row of letters:'))
		if row is True:  # illegal input case
			break
		else:
			boggle.append(row)
	return boggle


def check_format(s):
	"""
	:param s: import the row of letters
	:return a: if a is True, illegal input, else return list
	"""
	a = s.split()
	for i in range(len(a)):
		if len(a[i]) > 1 or len(a) != 4:
			print('Illegal input')
			return True
		elif len(a) == 4:
			return a


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for line in f:
			dictionary.append(line[:-1])


def has_prefix(sub_s, new_dict):
	"""
	:param sub_s:  str, confirm whether the English prefix is in the dictionary
	:param new_dict: list, filter the word starts with the alphabets from boggle
	:return a: str, if a = 'T', means the valid word, if a is None, means the sub_s is not in the dictionary
	"""
	a = 'F'
	for i in range(len(new_dict)):
		if new_dict[i].startswith(sub_s):
			if len(new_dict[i]) == len(sub_s):
				a = 'T'
			else:
				a = 'G'
			return a
		else:
			pass


if __name__ == '__main__':
	main()

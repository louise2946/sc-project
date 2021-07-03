"""
File: anagram.py
Name: Ada Wang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    print('Welcome to stanCode "Anagram Generator" (or '+str(EXIT)+' to quit)')
    read_dictionary()

    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        else:
            start = time.time()
            find_anagrams(s)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')
    # ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


dictionary = {}


def read_dictionary():
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            dictionary[line[:-1]] = line[:-1]


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    print('Searching...')
    end_lst = []
    new_dict = {}
    for key in dictionary:
        for i in range(len(s)):
            if key.startswith(s[i]) and len(s) == len(key):
                new_dict[key] = dictionary[key]
    find_anagrams_helper(new_dict, s, '', end_lst)  # []:save anagrams
    print(str(len(end_lst))+' anagrams for:', end_lst)


def find_anagrams_helper(new_dict, s, current_lst, end_lst):
    if len(s) == 0:
        if has_prefix(new_dict, current_lst) == 'T' and current_lst not in end_lst:
            print('Found:'+current_lst)
            print('Searching...')
            end_lst.append(current_lst)
    elif len(s) >= 2 and has_prefix(new_dict, current_lst) is None:  # check if has prefix
        # print(2,current_lst)
        pass
    else:
        # explore
        for i in range(len(s)):
            find_anagrams_helper(new_dict, s[:i]+s[i+1:], current_lst+s[i:i+1], end_lst)


def has_prefix(new_dict, sub_s):
    """
    :param sub_s:
    :return:
    """
    a = 'F'
    for key in new_dict:
        if key.startswith(sub_s) is True:
            a = 'T'
            # print(key,a,sub_s)
            return a
        else:
            pass
    #print(key, a, sub_s)


if __name__ == '__main__':
    main()

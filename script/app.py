from pathlib import Path
from sys import path as PATH
PATH.append(str(
	Path(__file__) \
	.resolve() \
	.parents[1]\
	/ Path('src')))

from random import choice
from encouragement.phrase import phrases

def main():
	print(choice(phrases()))
if __name__ == '__main__':
	main()

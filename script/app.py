from pathlib import Path
from sys import path as PATH
PATH.append(str(
	Path(__file__) \
	.resolve() \
	.parents[1]\
	/ Path('src')))

from encouragement.phrase import phrases

def main():
	for s in phrases():
		print(s)
if __name__ == '__main__':
	main()

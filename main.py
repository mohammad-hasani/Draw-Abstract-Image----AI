import ga
import algorithms
from tools import *

def main():
	tp =algorithms.MakeAbstract(points_n = 300)
	tp.start()
	show_lines(tp.lines)


if __name__ == '__main__':
	main()
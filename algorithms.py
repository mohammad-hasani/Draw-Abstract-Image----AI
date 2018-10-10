import numpy as np
from tools import *
from scipy.spatial import distance


class MakeAbstract(object):
	def __init__(self, page_size_x=1024, page_size_y=1024, points_n=20, border=True):
		self.page_size_x = page_size_x
		self.page_size_y = page_size_y
		self.points_n = points_n
		self.border = border
		self.points = []
		self.lines = []
		self.points_costs = []

	def start(self):
		self.create_points()
		self.sort_points()
		self.make_lines()

	def create_points(self):
		def make_point(range_start, range_end, d_x=False, d_y=False):
			for i in range(range_start, range_end):
				if d_x is not False:
					x = d_x
				else:
					x = np.random.randint(0, self.page_size_x)
				if d_y is not False:
					y = d_y
				else:
					y = np.random.randint(0, self.page_size_y)
				point = Point(x, y)
				self.points.append(point)
		make_point(0, self.points_n)
		if self.border:
			make_point(10, 20, d_y=0)
			make_point(10, 20, d_x=0)
			make_point(10, 20, d_y=self.page_size_y)
			make_point(10, 20, d_x=self.page_size_x)

	def make_lines(self):
		for i in range(0, len(self.points_costs)):
			intersect = False
			for j in range(0, len(self.lines)):
				ind_p1 = self.points_costs[i][0]
				ind_p2 = self.points_costs[i][1]

				p1 = self.points[ind_p1]
				p2 = self.points[ind_p2]

				q1 = self.lines[j].p1
				q2 = self.lines[j].p2

				if p1.x == q1.x and p1.y == q1.y:
					continue
				if p2.x == q2.x and p2.y == q2.y:
					continue
				
				intersect = doIntersect(p1, p2, q1, q2)
				if intersect:
					break
			if not intersect:
				ind_p1 = self.points_costs[i][0]
				ind_p2 = self.points_costs[i][1]

				p1 = self.points[ind_p1]
				p2 = self.points[ind_p2]
				line = Line(p1, p2)
				self.lines.append(line)

	def sort_points(self):
		costs = []
		for index in range(0, len(self.points) - 1):
			for index2 in range(index + 1, len(self.points)):
				value_x = self.points[index].x
				value_y = self.points[index].y
				value2_x = self.points[index2].x
				value2_y = self.points[index2].y
				euc_dis = distance.euclidean([value_x, value_y], [value2_x, value2_y])
				costs.append([index, index2, euc_dis])
		costs = sorted(costs, key=lambda x: x[2])
		self.points_costs = costs
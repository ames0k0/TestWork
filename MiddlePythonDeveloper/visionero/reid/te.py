# Group Adjacent Coordinates
# Using product() + groupby() + list comprehension
# from itertools import groupby, product
# 
# def Manhattan(tup1, tup2):
#   a = abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])
#   print(a)
#   return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])
# 
# # initializing list
# test_list = [(4, 4), (6, 4), (7, 8), (11, 11),
#                      (7, 7), (11, 12), (5, 4)]
# 
# # printing original list
# print("The original list is : " + str(test_list))
# 
# # Group Adjacent Coordinates
# # Using product() + groupby() + list comprehension
# man_tups = [sorted(sub) for sub in product(test_list, repeat = 2)
#                                          if Manhattan(*sub) == 1]
# 
# res_dict = {ele: {ele} for ele in test_list}
# for tup1, tup2 in man_tups:
#     res_dict[tup1] |= res_dict[tup2]
#     res_dict[tup2] = res_dict[tup1]
# 
# res = [[*next(val)] for key, val in groupby(
#         sorted(res_dict.values(), key = id), id)]
# 
# # printing result
# print("The grouped elements : " + str(res))


test_list = [
  (449, 289), (437, 277), (427, 257), (410, 250), (396, 220), (413, 197), (384, 188), (371, 183), (413, 182)
]

# 0[..], 1[..]
test_list.sort()

# from sklearn.cluster import MeanShift
# import numpy as np
# # X = np.array([[1, 1], [2, 1], [1, 0],
# #               [4, 7], [3, 5], [3, 6]])
# X = sorted(test_list)
# 
# clustering = MeanShift(bandwidth=3).fit(X)
# print('<<<<', clustering.labels_)
# 
# 
# from sklearn.cluster import KMeans
# kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
# print(kmeans.labels_)

from collections import defaultdict

max_dist = 100

new_list = defaultdict(list)

for i, (x, y) in enumerate(test_list):
  if not i:
    prev_x = x
    prev_y = y
    continue

  if (x - prev_x) < max_dist:
    if (y - prev_y) < max_dist//2:
      new_list[(prev_x, prev_y)].append((x, y))
      continue

  prev_x = x
  prev_y = y

print(new_list)

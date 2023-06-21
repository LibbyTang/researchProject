import pickle

pose_path = "../data/cam3_final.pkl"
data = pickle.load(open(pose_path, "rb"))
print(data)


# pose_path = "../data/unsuccessful_test_pkl/all_unsuccessful/2s/1_INTS_test.pkl"
#
# data = pickle.load(open(pose_path, "rb"))
# print(data)

# unsuccessful_annotations = [(2, 385570, 387670, 'INTS_start'), (2, 326840, 328570, 'INTS_continue'),
# (3, 139500, 141950, 'INTS_continue'), (3, 371950, 374520, 'INTS_continue'), (4, 127110, 129170, 'INTS_start'),
#                             (4, 44860, 47690, 'INTS_continue'), (4, 192490, 194400, 'INTS_start'),
#                             (4, 428950, 431620, 'INTS_start'), (4, 454360, 456800, 'INTS_start'),
#                             (4, 461680, 464710, 'INTS_start'), (4, 112740, 115090, 'INTS_start'),
#                             (4, 196910, 198870, 'INTS_start'), (4, 266310, 267900, 'INTS_continue'),
#                             (4, 284290, 286930, 'INTS_continue'), (4, 297150, 298820, 'INTS_start'),
#                             (4, 310960, 312890, 'INTS_continue'), (5, 397280, 400500, 'INTS_continue'),
#                             (5, 245770, 248370, 'INTS_start'), (5, 412940, 414980, 'INTS_start'),
#                             (7, 317660, 319900, 'INTS_continue'), (7, 570090, 574000, 'INTS_start'),
#                             (10, 265920, 267680, 'INTS_continue'), (10, 268070, 270040, 'INTS_continue'),
#                             (10, 299760, 301570, 'INTS_continue'), (10, 322010, 323890, 'INTS_start'),
#                             (10, 506090, 507620, 'INTS_continue'), (11, 35322, 36322, 'INTS_start'),
#                             (11, 569646, 572020, 'INTS_start'), (11, 50231, 51231, 'INTS_start'), (11, 52129, 53129, 'INTS_start'),
#                             (11, 284610, 285610, 'INTS_continue'), (11, 504946, 505946, 'INTS_start'),
#                             (17, 127110, 128590, 'INTS_continue'), (17, 234790, 236770, 'INTS_continue'),
#                             (17, 586720, 588630, 'INTS_start'), (22, 319730, 322010, 'INTS_start'),
#                             (22, 245900, 248380, 'INTS_start'), (22, 355920, 359270, 'INTS_start'),
#                             (23, 543100, 545700, 'INTS_continue'),
#                             (22, 531540, 536200, 'INTS_continue'), (22, 555410, 557510, 'INTS_start'),
#                             (27, 472000, 476363, 'INTS_start'), (27, 35363, 38454, 'INTS_continue'),
#                             (27, 44909, 48909, 'INTS_start'), (27, 86181, 88090, 'INTS_continue'),
#                             (34, 426545, 432090, 'INTS_start'), (34, 439545, 440727, 'INTS_start'),
#                             (34, 473363, 478545, 'INTS_start'), (34, 515636, 518636, 'INTS_start'),
#                             (35, 214080, 216580, 'INTS_start')]
#
# import numpy as np
#
# print(len(unsuccessful_annotations))
# s = []
# c = []
# for i in unsuccessful_annotations:
#     if i[3] == 'INTS_start':
#         s.append(i)
#     if i[3] == 'INTS_continue':
#         c.append(i)
# durations = [(i[2] - i[1]) / 1000 for i in unsuccessful_annotations]
# print(np.mean(durations))
# print(np.std(durations))
# print(len(s))
# print(len(c))

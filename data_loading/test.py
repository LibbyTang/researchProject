# # import pickle
#
# # pose_path = "../data/cam3_final.pkl"
# # # Open the PKL file in read-binary mode
# # with open(pose_path, "rb") as file:
# #     # Load the object from the PKL file
# #     obj = pickle.load(file)
# #
# # # Now you can inspect the object or print its contents
# # print(obj)
#
# # pose_path = "../data/unsuccessful_test_pkl/all_unsuccessful/2s/1_INTS_test.pkl"
# #
# # data = pickle.load(open(pose_path, "rb"))
# # print(data)
#
# # unsuccessful_annotations = [(2, 385570, 387670, 'INTS_start'), (2, 326840, 328570, 'INTS_continue'),
# # (3, 139500, 141950, 'INTS_continue'), (3, 371950, 374520, 'INTS_continue'), (4, 127110, 129170, 'INTS_start'),
# #                             (4, 44860, 47690, 'INTS_continue'), (4, 192490, 194400, 'INTS_start'),
# #                             (4, 428950, 431620, 'INTS_start'), (4, 454360, 456800, 'INTS_start'),
# #                             (4, 461680, 464710, 'INTS_start'), (4, 112740, 115090, 'INTS_start'),
# #                             (4, 196910, 198870, 'INTS_start'), (4, 266310, 267900, 'INTS_continue'),
# #                             (4, 284290, 286930, 'INTS_continue'), (4, 297150, 298820, 'INTS_start'),
# #                             (4, 310960, 312890, 'INTS_continue'), (5, 397280, 400500, 'INTS_continue'),
# #                             (5, 245770, 248370, 'INTS_start'), (5, 412940, 414980, 'INTS_start'),
# #                             (7, 317660, 319900, 'INTS_continue'), (7, 570090, 574000, 'INTS_start'),
# #                             (10, 265920, 267680, 'INTS_continue'), (10, 268070, 270040, 'INTS_continue'),
# #                             (10, 299760, 301570, 'INTS_continue'), (10, 322010, 323890, 'INTS_start'),
# #                             (10, 506090, 507620, 'INTS_continue'), (11, 35322, 36322, 'INTS_start'),
# #                             (11, 569646, 572020, 'INTS_start'), (11, 50231, 51231, 'INTS_start'), (11, 52129, 53129, 'INTS_start'),
# #                             (11, 284610, 285610, 'INTS_continue'), (11, 504946, 505946, 'INTS_start'),
# #                             (17, 127110, 128590, 'INTS_continue'), (17, 234790, 236770, 'INTS_continue'),
# #                             (17, 586720, 588630, 'INTS_start'), (22, 319730, 322010, 'INTS_start'),
# #                             (22, 245900, 248380, 'INTS_start'), (22, 355920, 359270, 'INTS_start'),
# #                             (23, 543100, 545700, 'INTS_continue'),
# #                             (22, 531540, 536200, 'INTS_continue'), (22, 555410, 557510, 'INTS_start'),
# #                             (27, 472000, 476363, 'INTS_start'), (27, 35363, 38454, 'INTS_continue'),
# #                             (27, 44909, 48909, 'INTS_start'), (27, 86181, 88090, 'INTS_continue'),
# #                             (34, 426545, 432090, 'INTS_start'), (34, 439545, 440727, 'INTS_start'),
# #                             (34, 473363, 478545, 'INTS_start'), (34, 515636, 518636, 'INTS_start'),
# #                             (35, 214080, 216580, 'INTS_start')]
# #
# # import numpy as np
# #
# # print(len(unsuccessful_annotations))
# # s = []
# # c = []
# # for i in unsuccessful_annotations:
# #     if i[3] == 'INTS_start':
# #         s.append(i)
# #     if i[3] == 'INTS_continue':
# #         c.append(i)
# # durations = [(i[2] - i[1]) / 1000 for i in unsuccessful_annotations]
# # print(np.mean(durations))
# # print(np.std(durations))
# # print(len(s))
# # print(len(c))
#
#
#
# # import matplotlib.pyplot as plt
# #
# # # Data from Batch 32, successful
# # batch32_successful = [0.5032777807922065, 0.4722838302108887, 0.5012397525568172, 0.5030641511553897]
# # batch32_successful_std = [0.0037439630875768758, 0.004373784945995365, 0.0034675065969396674, 0.0032199819804937017]
# #
# # # Data from Batch 131, successful
# # batch131_successful = [0.5686671640825077, 0.5354245412825476, 0.5138566630566624, 0.4904739748632875]
# # batch131_successful_std = [0.018386048943667115, 0.016004600369257785, 0.01639618811941954, 0.0182048264955257]
# #
# # # Labels for x-axis
# # labels = ['1 second', '2 seconds', '3 seconds', '4 seconds']
# #
# # # Create the plot
# # plt.plot(labels, batch32_successful, marker='o', label='Batch 32 - Successful')
# # plt.plot(labels, batch131_successful, marker='o', label='Batch 131 - Successful')
# # plt.errorbar(labels, batch32_successful, yerr=batch32_successful_std, fmt='none', color='black', capsize=5)
# # plt.errorbar(labels, batch131_successful, yerr=batch131_successful_std, fmt='none', color='black', capsize=5)
# # plt.xlabel('Time Window')
# # plt.ylabel('AUC Score')
# # plt.title('AUC Scores for Successful Intentions (Batch 32 vs Batch 131)')
# # plt.legend()
# # plt.show()
# #
# # import matplotlib.pyplot as plt
# #
# # # Data from Batch 32, unsuccessful
# # batch32_unsuccessful = [0.4909658429005486, 0.4888266900973212, 0.5531739915954325, 0.4922294477800341]
# # batch32_unsuccessful_std = [0.014576196182887814, 0.010374869263784746, 0.007741293930257289, 0.007589851431999372]
# #
# # # Data from Batch 131, unsuccessful
# # batch131_unsuccessful = [0.5298570124755776, 0.5364591447919281, 0.5063645151907274, 0.4740771100134611]
# # batch131_unsuccessful_std = [0.010443424314931971, 0.012572310072367511, 0.010097056482685149, 0.008866831506937524]
# #
# # # Labels for x-axis
# # labels = ['1 second', '2 seconds', '3 seconds', '4 seconds']
# #
# # # Create the plot
# # plt.plot(labels, batch32_unsuccessful, marker='o', label='Batch 32 - Unsuccessful')
# # plt.plot(labels, batch131_unsuccessful, marker='o', label='Batch 131 - Unsuccessful')
# # plt.errorbar(labels, batch32_unsuccessful, yerr=batch32_unsuccessful_std, fmt='none', color='black', capsize=5)
# # plt.errorbar(labels, batch131_unsuccessful, yerr=batch131_unsuccessful_std, fmt='none', color='black', capsize=5)
# # plt.axhline(y=0.5, color='red', linestyle='--', label='Random Guessing')
# # plt.xlabel('Time Window')
# # plt.ylabel('AUC Score')
# # plt.title('AUC Scores for Unsuccessful Batches (Batch 32 vs Batch 131)')
# # plt.legend()
# # plt.show()
#
#
# # import matplotlib.pyplot as plt
# #
# # # Data for 39 pose features
# # pose_39 = [0.5211441297898727, 0.5008176654970306, 0.4991345262832981, 0.4743695497991924]
# # pose_39_std = [0.011153215993617127, 0.010775114259353279, 0.008418179478320478, 0.008113704490517966]
# #
# # # Data for 26 pose features
# # pose_26 = [0.5348594386558148, 0.5134531543375472, 0.5157100930247878, 0.500439957717399]
# # pose_26_std = [0.010021248561349179, 0.012076554237377274, 0.01240646983075335, 0.012647028214798052]
# #
# # # Labels for x-axis
# # labels = ['1 second', '2 seconds', '3 seconds', '4 seconds']
# #
# # # Create the plot
# # plt.plot(labels, pose_39, marker='o', label='with confidence scores')
# # plt.plot(labels, pose_26, marker='o', label='without confidence scores')
# # plt.errorbar(labels, pose_39, yerr=pose_39_std, fmt='none', color='black', capsize=5)
# # plt.errorbar(labels, pose_26, yerr=pose_26_std, fmt='none', color='black', capsize=5)
# # plt.axhline(y=0.5, color='red', linestyle='--', label='Random Guessing')
# # plt.xlabel('Time Window')
# # plt.ylabel('AUC Score')
# # plt.title('AUC Scores with or without confidence scores')
# # plt.legend()
# # plt.show()
#
# # import matplotlib.pyplot as plt
# #
# # # Data for annotation from Li et al. (successful)
# # li_et_al_successful = [0.48592355080915195, 0.49021050931982285, 0.5124883749002946, 0.48700401058506065]
# # li_et_al_successful_std = [0.0032425204087103607, 0.00480704962604123, 0.0035380311152339444, 0.005608994982626379]
# #
# # # Data for annotation from the research group (successful)
# # research_group_successful = [0.5686671640825077, 0.5354245412825476, 0.5138566630566624, 0.4904739748632875]
# # research_group_successful_std = [0.018386048943667115, 0.016004600369257785, 0.01639618811941954, 0.0182048264955257]
# #
# # # Labels for x-axis
# # labels = ['1 second', '2 seconds', '3 seconds', '4 seconds']
# #
# # # Create the plot
# # plt.plot(labels, li_et_al_successful, marker='o', label='Annotation from Li et al.')
# # plt.plot(labels, research_group_successful, marker='o', label='Annotation from the research group')
# # plt.errorbar(labels, li_et_al_successful, yerr=li_et_al_successful_std, fmt='none', color='black', capsize=5)
# # plt.errorbar(labels, research_group_successful, yerr=research_group_successful_std, fmt='none', color='black', capsize=5)
# # plt.axhline(y=0.5, color='red', linestyle='--', label='Random Guessing')
# # plt.xlabel('Time Window')
# # plt.ylabel('AUC Score')
# # plt.title('AUC Scores for Successful Annotations (different annotations)')
# # plt.legend()
# # plt.show()
# #
# # import matplotlib.pyplot as plt
# #
# # # Data for annotation from Li et al. (unsuccessful)
# # li_et_al_unsuccessful = [0.5118223339722644, 0.5651158652341749, 0.48233877324762714, 0.4051259819746225]
# # li_et_al_unsuccessful_std = [0.00936357958308225, 0.012030785891578325, 0.010925106001579244, 0.009830702074491599]
# #
# # # Data for annotation from the research group (successful)
# # research_group_successful = [0.5298570124755776, 0.5364591447919281, 0.5063645151907274, 0.4740771100134611]
# # research_group_successful_std = [0.010443424314931971, 0.012572310072367511, 0.010097056482685149, 0.008866831506937524]
# #
# # # Labels for x-axis
# # labels = ['1 second', '2 seconds', '3 seconds', '4 seconds']
# #
# # # Create the plot
# # plt.plot(labels, li_et_al_unsuccessful, marker='o', label='Annotation from Li et al.')
# # plt.plot(labels, research_group_successful, marker='o', label='Annotation from the research group')
# # plt.errorbar(labels, li_et_al_unsuccessful, yerr=li_et_al_unsuccessful_std, fmt='none', color='black', capsize=5)
# # plt.errorbar(labels, research_group_successful, yerr=research_group_successful_std, fmt='none', color='black', capsize=5)
# # plt.axhline(y=0.5, color='red', linestyle='--', label='Random Guessing')
# # plt.xlabel('Time Window')
# # plt.ylabel('AUC Score')
# # plt.title('AUC Scores for Unsuccessful Annotations (different annotations)')
# # plt.legend()
# # plt.show()
#
# # import matplotlib.pyplot as plt
# #
# # # Data for annotation from Li et al. (unsuccessful start)
# # li_et_al_unsuccessful_start = [0.45932301496920774, 0.5347236987480614, 0.41374047513543344, 0.4104282651465875]
# # li_et_al_unsuccessful_start_std = [0.01165248066478698, 0.0116724342495783, 0.011261546524151555, 0.014076445728500498]
# #
# # # Data for annotation from the research group (unsuccessful start)
# # research_group_unsuccessful_start = [0.4722106145993736, 0.5267809905168597, 0.4956263726238806, 0.4129852247338301]
# # research_group_unsuccessful_start_std = [0.015670595197504123, 0.019324937738689842, 0.012693553507788054, 0.01468473549241993]
# #
# # # Labels for x-axis
# # labels = ['1 second', '2 seconds', '3 seconds', '4 seconds']
# #
# # # Create the plot
# # plt.plot(labels, li_et_al_unsuccessful_start, marker='o', label='Annotation from Li et al.')
# # plt.plot(labels, research_group_unsuccessful_start, marker='o', label='Annotation from the research group')
# # plt.errorbar(labels, li_et_al_unsuccessful_start, yerr=li_et_al_unsuccessful_start_std, fmt='none', color='black', capsize=5)
# # plt.errorbar(labels, research_group_unsuccessful_start, yerr=research_group_unsuccessful_start_std, fmt='none', color='black', capsize=5)
# # plt.axhline(y=0.5, color='red', linestyle='--', label='Random Guessing')
# # plt.xlabel('Time Window')
# # plt.ylabel('AUC Score')
# # plt.title('AUC Scores for Unsuccessful Start Annotations (different annotations)')
# # plt.legend()
# # plt.show()
# #
# # import matplotlib.pyplot as plt
# #
# # # Data for annotation from Li et al. (unsuccessful continuous)
# # li_et_al_unsuccessful_continuous = [0.6084049803241105, 0.6090123734318663, 0.627974770923894, 0.3878570673720376]
# # li_et_al_unsuccessful_continuous_std = [0.020088434340780753, 0.021223922814689055, 0.02015075834192195, 0.015325890842212071]
# #
# # # Data for annotation from the research group (unsuccessful continuous)
# # research_group_unsuccessful_continuous = [0.6122769422017478, 0.5533837293288543, 0.5321949395770724, 0.5293796736110932]
# # research_group_unsuccessful_continuous_std = [0.015516411565618634, 0.01616774887094847, 0.013398019770383105, 0.010968142972438432]
# #
# # # Labels for x-axis
# # labels = ['1 second', '2 seconds', '3 seconds', '4 seconds']
# #
# # # Create the plot
# # plt.plot(labels, li_et_al_unsuccessful_continuous, marker='o', label='Annotation from Li et al.')
# # plt.plot(labels, research_group_unsuccessful_continuous, marker='o', label='Annotation from the research group')
# # plt.errorbar(labels, li_et_al_unsuccessful_continuous, yerr=li_et_al_unsuccessful_continuous_std, fmt='none', color='black', capsize=5)
# # plt.errorbar(labels, research_group_unsuccessful_continuous, yerr=research_group_unsuccessful_continuous_std, fmt='none', color='black', capsize=5)
# # plt.axhline(y=0.5, color='red', linestyle='--', label='Random Guessing')
# # plt.xlabel('Time Window')
# # plt.ylabel('AUC Score')
# # plt.title('AUC Scores for Unsuccessful Continuous Annotations (different annotations)')
# # plt.legend()
# # plt.show()
#
#
# import numpy as np
# from scipy import stats
#
# # Define your sample data
# data = np.array([0.5198350603161459, 0.5204115261296113, 0.5208283980247881, 0.5195593684260854, 0.5210629211673541, 0.5187777170993257, 0.5191271538891404, 0.5140408147857763, 0.5145577320644013, 0.5194437546339118, 0.516757007741119, 0.5235354502393881, 0.518223152042652, 0.5316975275351352, 0.509970661780852, 0.5181697309390602, 0.5306766086118733, 0.5229345410180924, 0.5326289843354048, 0.5208585773459816, 0.5180941111433921, 0.5155573870327109, 0.5156368124319675, 0.5166580154724115, 0.5158000745160889, 0.5253189555327713, 0.520873887068426, 0.5195222065410994, 0.5176253049632257, 0.5230901888376593, 0.5236734190019441, 0.5225010888326911, 0.5287109519944341, 0.5182491281083403, 0.5186425242777034, 0.5288810376814344, 0.5252950091169366, 0.5159510603249462, 0.5193691710201045, 0.5236479895596136, 0.5162866292758945, 0.5277645121176844, 0.5325447800141799, 0.5171678320096594, 0.5278403008991186, 0.5222548979073881, 0.5203960603197632, 0.5340256317206692, 0.5270646267176733, 0.5125936327757957, 0.5238584867805524, 0.5116309751016991, 0.5159415950720978, 0.5282457953943683, 0.5296715682641634, 0.5200835078090049, 0.5147438211398372, 0.5209378690477766, 0.5212109770030044, 0.5274271445685087, 0.5240530479501146, 0.5115213661173008, 0.5194019643163352, 0.5213610082368394, 0.5251269492342215, 0.5205334821034854, 0.5257725927767872, 0.5233721304110518, 0.5272396667064257, 0.5217341926418889, 0.523411766329652, 0.5154959767409422, 0.5319227407852983, 0.5175369517427342, 0.5273231077219563, 0.5161667499829474, 0.518401134342776, 0.5150127012561344, 0.5240423807960348, 0.5260907702075515, 0.5110461226062559, 0.5125244344223948, 0.5296509903083914, 0.523850451966981, 0.5217719843373165, 0.5238774693341377, 0.5173614740888872, 0.5193772475693332, 0.5223631900828081, 0.5167515912518771, 0.5216387461247767, 0.5193445538284684, 0.5217691616664596, 0.5226792765850559, 0.5186264915690333, 0.5199596875709954, 0.5211582689478164, 0.5230027725381343, 0.5170831865110158, 0.5228507313236842]
# )
#
# mean1 = 0.5923
#
#
# std1 = 0.004
#
# # Define the null hypothesis mean
# null_hypothesis_mean = 0.5
#
# # Perform one-sample t-test
# t_statistic, p_value = stats.ttest_1samp(data, null_hypothesis_mean)
#
#
# # Calculate the one-tailed p-value
# if t_statistic > 0:
#     one_tailed_p_value = p_value
# else:
#     one_tailed_p_value = 1 - p_value
#
# print("One-sample t-test results:")
# print("t-statistic:", t_statistic)
# print("One-tailed p-value:", one_tailed_p_value)
#
#
#
#
# sample_size = 100  # Assuming both samples have the same size
#
# # Generate the raw data for the paired samples
# sample1 = data
# sample2 = np.random.normal(mean1, std1, sample_size)
#
# # Perform paired samples t-test
# t_statistic1, p_value1 = stats.ttest_rel(sample1, sample2)
#
# if t_statistic1 > 0:
#     one_tailed_p_value = p_value1
# else:
#     one_tailed_p_value = 1 - p_value1
#
# print("......")
# print("Paired Samples T-Test Results:")
# print("t-statistic:", t_statistic1)
# print("p-value:", one_tailed_p_value)
#

import matplotlib.pyplot as plt

# Data from the table
labels = ['1 second', '2 seconds', '3 seconds', '4 seconds']
unsuccessful_start = [0.64080929797075, 0.4373259155876879, 0.5760795497971501, 0.5498487318108508]
unsuccessful_continuous = [0.5058953838362605, 0.5292242267980579, 0.5113450814810201, 0.5618813248932564]

# Standard deviations (std) for error bars
unsuccessful_start_std = [0.014609976748069856, 0.012357121451373911, 0.012113601100848036, 0.013089641147407377]
unsuccessful_continuous_std = [0.01597239634140707, 0.013670837250198896, 0.013412016757608064, 0.01078153417831562]

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the data
ax.plot(labels, unsuccessful_start, marker='o', label='Unsuccessful (Start)')
ax.plot(labels, unsuccessful_continuous, marker='o', label='Unsuccessful (Continuous)')

# Add error bars
ax.errorbar(labels, unsuccessful_start, yerr=unsuccessful_start_std, fmt='none', color='black', capsize=5)
ax.errorbar(labels, unsuccessful_continuous, yerr=unsuccessful_continuous_std, fmt='none', color='black', capsize=5)

# Add horizontal line for Random Guessing
ax.axhline(y=0.5, color='red', linestyle='--', label='Random Guessing')

# Set labels and title
ax.set_xlabel('Time Window')
ax.set_ylabel('AUC Score')
ax.set_title('AUC Scores for Different Time Windows - Group 2')
ax.legend()

plt.tight_layout()  # Adjust spacing
plt.show()

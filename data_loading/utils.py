import csv
import os

import pickle


import numpy as np
import pandas as pd


# csv_path = "../preprocess/audio/vad/"

# csv file path for successful training dataset.
from scipy.interpolate import interp1d

csv_path = "../preprocess/audio/successful_train_samples/"

# csv file path for successful testing dataset.
test_csv_path_successful = "../preprocess/audio/successful_test_samples/"

# csv file of all_unsuccessful unsucessful testing samples including both start and continue category.
test_csv_path_unsuccessful = "../preprocess/audio/unsuccessful_intention_test_sample/"

# csv file of all_unsuccessful unsucessful testing samples including both start and continue category.
test_csv_path_all_sample = "../preprocess/audio/all_sample/"

# txt output file of customized check
txt_path = "../preprocess/audio/output_file/"

balloon_pop_1_video_frame = 23030  # to
balloon_pop_1_accel_frame = 45977 + 19 / 34

balloon_pop_2_video_frame = 74844
balloon_pop_2_accel_frame = 47706 + 23 / 28

balloon_pop_3_video_frame = 166836.5
balloon_pop_3_accel_frame = 50776 + 30.5 / 32


def reset_examples_ids(examples):
    for i, ex in enumerate(examples):
        ex['id'] = i


'''
Generate information for example.pkl file
'''


class Maker():
    def __init__(self, tracks_path2=None, tracks_path3=None, accel_path=None, vad_path=None, unsuccessful_vad_path=None,
                 all_sample_path=None):
        self.tracks_cam2 = pickle.load(open(tracks_path2, "rb"))
        self.tracks_cam3 = pickle.load(open(tracks_path3, "rb"))

        self.accel = {}
        if accel_path is not None:
            self.load_accel(accel_path)

        self.vad = {}
        if vad_path is not None:
            self.load_vad(vad_path)

        self.unsuccessful_vad = {}
        if unsuccessful_vad_path is not None:
            self.load_unsuccessful_vad(unsuccessful_vad_path)

        self.all_samples_vad = {}
        if all_sample_path is not None:

            self.load_all_vad(all_sample_path)

        self.examples = None
        self.test_examples = None
        self.unsuccessful_examples = None
        self.all_samples = None

    def load_accel(self, accel_path):
        self.accel = pickle.load(open('../data/subj_accel_interp.pkl', 'rb'))

    def load_vad(self, vad_path):

        # load csv directly
        self.vad = {}
        pid_list = [2, 3, 4, 5, 7, 10, 11, 17, 22, 23, 27, 34, 35]
        for i in pid_list:
            fpath = os.path.join(vad_path, f'{i}.csv')

            self.vad[i] = pd.read_csv(fpath, header=None).to_numpy()

        if len(self.vad) == 0:
            print('load_vad called but nothing loaded.')

    def load_unsuccessful_vad(self, unsuccessful_vad):
        start_pid = [2, 3, 4, 7, 10, 11, 17, 22, 23, 34]
        # start_pid = [2, 3, 4, 5, 7, 10, 11, 17, 22, 23, 27, 34, 35]
        for i in start_pid:
            fpath = os.path.join(unsuccessful_vad, f'{i}.csv')
            self.unsuccessful_vad[i] = pd.read_csv(fpath, header=None).to_numpy()

        if len(self.unsuccessful_vad) == 0:
            print('load_unsuccessful_vad called but nothing loaded.')

    def _interp_vad(self, vad, in_fs, out_fs):
        t = np.arange(0, len(vad) / in_fs, 1 / in_fs)
        f = interp1d(t, vad, kind='nearest')
        tnew = np.arange(0, len(vad) / in_fs, 1 / out_fs)
        return f(tnew)

    def load_all_vad(self, all_vad):
        pid_list = [2, 3, 4, 5, 7, 10, 11, 17, 22, 23, 27, 34, 35]
        continue_pid = []
        maybe_pid = []
        for i in pid_list:
            fpath = os.path.join(all_vad, f'{i}.csv')

            self.all_samples_vad[i] = pd.read_csv(fpath, header=None).to_numpy()


        if len(self.all_samples_vad) == 0:
            print('load_all_vad called but nothing loaded.')

    # set time window
    def _get_vad(self, pid, ini_time, end_time, fs):
        # note audio (vad) and video start at the same time
        if pid not in self.vad:
            return None

        return self.vad[pid][ini_time * fs: end_time * fs].flatten()

    def _get_unsuccessful_vad(self, pid, ini_time, end_time, fs):
        # note audio (vad) and video start at the same time
        if pid not in self.unsuccessful_vad:
            return None

        return self.unsuccessful_vad[pid][ini_time * fs: end_time * fs].flatten()

    def _get_all_vad(self, pid, ini_time, end_time, fs):
        # note audio (vad) and video start at the same time
        if pid not in self.all_samples_vad:
            return None

        return self.all_samples_vad[pid][ini_time * fs: end_time * fs].flatten()

    def make_train_examples(self, windowSize, feature_fs):

        examples = list()
        example_id = 0
        valid_list = [2, 3, 4, 5, 7, 10, 11, 17, 22, 23, 27, 34, 35]

        # loop over participants
        for i in valid_list:
            # generate example of successful intention case:
            examples_participant, example_id = self.make_examples(i, example_id,
                                                                  csv_path + str(windowSize) + "s/" + '_' + str(
                                                                      i) + ".csv", feature_fs,
                                                                  self._get_vad)

            examples.append(examples_participant)

        examples = [item for sublist in examples for item in sublist]
        self.examples = examples
        print("training: ", len(examples))

        return examples

    # General template for making examples for a participant
    # (i indicate the pid for the current participant)
    def make_examples(self, i, example_id, csv_file, feature_fs, vad_function):
        # print("=========== Person", i, " ============")
        examples = []
        time_window_list = []

        with open(csv_file) as infile:
            reader = csv.reader(infile)

            for line in reader:
                if line:
                    # Add the time segment (as second) sample of the participant
                    time_window_list.append(tuple([int(line[0]), int(line[1])]))

        # Tracks in camera 2
        track_list2 = []

        # Tracks in camera 3
        track_list3 = []

        # Iterate through the tracks in camera 2, find the track that belongs to the current participant
        for _, track in enumerate(self.tracks_cam2):
            if i == track['pid']:
                track_list2.append(track)

        # Iterate through the tracks in camera 3, find the track that belongs to the current participant
        for _, track in enumerate(self.tracks_cam3):
            if i == track['pid']:
                track_list3.append(track)


        # Iterate through all the time segment samples
        for j in range(0, len(time_window_list)):
            # The participant does not have a track neither camera
            if not track_list2 and not track_list3:
                break

            ini_time = time_window_list[j][0]
            end_time = time_window_list[j][1]

            vad = vad_function(i, ini_time, end_time, 100)
            interp_vad = self._interp_vad(vad, 100, feature_fs)

            int_frame = ini_time * feature_fs
            end_frame = end_time * feature_fs

            poses_segment_cam2 = []
            # Iterate through all the tracks of the participant in camera 2 to find the one with the correct time
            # period.
            for participant_track in track_list2:
                # Check if the time interval has poses, if one endpoint is out of bound, discard this sample.
                ini = participant_track['ini']
                poses = participant_track['poses']

                if (int_frame > ini) and (end_frame < ini + len(poses)):
                    # Extract the corresponding pose segements from the given time segment
                    poses_segment_cam2 = poses[ini_time * feature_fs - ini + 1: end_time * feature_fs - ini + 1, :]
            poses_segment_cam3 = []
            # Iterate through all the tracks of the participant in camera 3 to find the one with the correct time
            # period.
            for participant_track in track_list3:
                # Check if the time interval has poses, if one endpoint is out of bound, discard this sample.
                ini = participant_track['ini']
                poses = participant_track['poses']

                if (int_frame > ini) and (end_frame < ini + len(poses)):
                    # Extract the corresponding pose segments from the given time segment
                    poses_segment_cam3 = poses[ini_time * feature_fs - ini + 1: end_time * feature_fs - ini + 1, :]

            poses_segment = []
            if poses_segment_cam2 == [] and poses_segment_cam3 == []:
                # print("There are some tracks in cam2 or cam3 of this person but none of them are in the range of the "
                #       "current time segment sample")
                continue
            elif poses_segment_cam2 == []:
                # print("Tracks in camera 2 of this person are not in the range of the current time segment sample")
                poses_segment = poses_segment_cam3
            elif poses_segment_cam3 == []:
                # print("Tracks in camera 3 of this person are not in the range of the current time segment sample")
                poses_segment = poses_segment_cam2
            else:
                # print("Compare the confident values")
                confidents2 = np.array([[x for i, x in enumerate(sublist) if (i + 1) % 3 == 0] for sublist in poses_segment_cam2])
                confidents3 = np.array([[x for i, x in enumerate(sublist) if (i + 1) % 3 == 0] for sublist in poses_segment_cam3])

                mean2 = np.mean(confidents2)
                mean3 = np.mean(confidents3)
                std2 = np.std(confidents2)
                std3 = np.std(confidents3)

                # Define the weights for mean and standard deviation
                mean_weight = 0.6  # Adjust the weight as per your preference
                std_weight = 0.4  # Adjust the weight as per your preference

                # Calculate the composite score for each array
                composite_score2 = (mean_weight * mean2) - (std_weight * std2)
                composite_score3 = (mean_weight * mean3) - (std_weight * std3)

                # Compare the composite scores
                if composite_score2 < composite_score3:
                    # print("confidents3 has a higher composite score.")
                    # print("mean 2: ", mean2)
                    # print("mean 3: ", mean3)
                    # print("std 2: ", std2)
                    # print("std 3: ", std3)

                    poses_segment = poses_segment_cam3
                else:
                    # print("confidents2 has a higher composite score.")
                    # print("mean 2: ", mean2)
                    # print("mean 3: ", mean3)
                    # print("std 2: ", std2)
                    # print("std 3: ", std2)

                    poses_segment = poses_segment_cam2

            # Only get x and y of the poses
            poses_segment_26 = np.array([[x for i, x in enumerate(sublist) if (i + 1) % 3 != 0] for sublist in
                                         poses_segment])

            examples.append({
                'id': example_id,
                'pid': i,
                'ini_time': ini_time,
                'end_time': end_time,
                # data
                'poses': poses_segment_26.transpose().astype(np.float32),
                'vad': interp_vad
            })
            example_id += 1

        return examples, example_id

    def make_test_examples(self, index_s, windowSize, feature_fs):
        test_examples = list()
        test_example_id = 0

        valid_list = [2, 3, 4, 5, 7, 10, 11, 17, 22, 23, 27, 34, 35]

        # loop over participants
        for i in valid_list:
            # generate example of successful intention case:
            examples_participant, test_example_id = self.make_examples(i, test_example_id, test_csv_path_successful
                                                                       + str(windowSize) + "s/" + str(index_s)
                                                                       + '_' + str(i) + ".csv", feature_fs,
                                                                       self._get_vad)
            test_examples.append(examples_participant)

        test_examples = [item for sublist in test_examples for item in sublist]
        self.test_examples = test_examples
        print("successful intention test: ", len(test_examples))

        return test_examples

    def make_all_examples(self, index_s, windowSize, feature_fs):
        """
        :param unsuccessful_pid: pid number
        :param index_s: the number of experiment
        :return: all_unsuccessful testing dataset including both start and continue unsuccessful case.
        """
        examples = list()
        example_id = 0
        valid_list = [2, 3, 4, 5, 7, 10, 11, 17, 22, 23, 27, 34, 35]
        for i in valid_list:
            examples_participant, example_id = self.make_examples(i, example_id, test_csv_path_all_sample
                                                                  + str(windowSize) + "s/" + str(index_s) + '_' + str(i)
                                                                  + ".csv", feature_fs, self._get_all_vad)
            examples.append(examples_participant)

        examples = [item for sublist in examples for item in sublist]
        self.all_samples = examples
        print("all intention test: ", len(examples))

        return examples

    def make_unsuccessful_examples(self, unsuccessful_pid, index_s, windowSize, feature_fs, category: str):
        """
        :param unsuccessful_pid: pid number
        :param index_s: the number of experiment
        :return: all_unsuccessful testing dataset including both start and continue unsuccessful case.
        """
        examples = list()
        example_id = 0
        valid_list = [2, 3, 4, 5, 7, 10, 11, 17, 22, 23, 27, 34, 35]
        for i in valid_list:

            if not unsuccessful_pid.__contains__(i):
                continue

            examples_participant, example_id = self.make_examples(i, example_id, test_csv_path_unsuccessful + category
                                                                  + "/" + str(windowSize) + "s/"
                                                                  + str(index_s) + '_' + str(i) + ".csv", feature_fs,
                                                                  self._get_unsuccessful_vad)
            examples.append(examples_participant)

        examples = [item for sublist in examples for item in sublist]
        self.unsuccessful_examples = examples
        print("unsuccessful intention test: ", len(examples))

        return examples

    def filter_examples_by_movement_threshold(self, ts=20):
        new_examples = list()

        for ex in self.examples:
            track = ex['poses']
            std_x = np.std(track[:, 3])
            std_y = np.std(track[:, 4])

            if std_x > ts or std_y > ts:
                continue

            new_examples.append(ex)


video_seconds_to_accel_sample = interp1d(
    [
        balloon_pop_1_video_frame / 29.97,
        balloon_pop_3_video_frame / 29.97
    ], [
        balloon_pop_1_accel_frame,
        balloon_pop_3_accel_frame
    ], fill_value="extrapolate")

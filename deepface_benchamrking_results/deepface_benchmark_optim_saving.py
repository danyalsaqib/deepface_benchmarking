# Basic Libraries

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shutil

import tensorflow as tf
# Check version
print(tf.__version__)
device_name = tf.test.gpu_device_name()
#if device_name != '/device:GPU:0':
#  raise SystemError('GPU device not found')
#print('Found GPU at: {}'.format(device_name))

from deepface import DeepFace
from deepface.commons import distance as dst

# Creates one test directory, and copy 'num_files_test' number of files from each folder

rootdir = 'celeb_updated_ready_25_june'
n = 0
total_images = 0
num_files_test = 5
for subdir, dirs, files in os.walk(rootdir):
    if (str(subdir[28:32]) != "test") & (n > 0):
      dir_iter = "test"
      path_test = os.path.join(rootdir, dir_iter)
      path_from = os.path.join(rootdir, subdir[28:len(subdir)])
      print("From Path ", n, ": ", path_from)
      print("Test Path ", n, ": ", path_test)
      if(files):
        print("\nFiles exist in this directory - Printing first ", num_files_test, " images:\n")
        for i in range(num_files_test):
          print("Iteration: ", i, "\n")
          print(files[i])
          copy_from_file = os.path.join(path_from, files[i])
          print(copy_from_file)
          img_str = str(subdir[28:len(subdir)]) + "_img_" + str(i) + ".jpg" 
          copy_to_file = os.path.join(path_test, img_str)
          print(copy_to_file)
          total_images += 1
          shutil.copyfile(copy_from_file, copy_to_file)
      else:
        print("\nThis directory has no files!")
      print("\nDone for this directory - exiting\n\n")
      print("******************************************\n\n")
    # print(subdir[28:len(subdir)])
    n += 1

print("Total Iterations: ", n)
print("Total images saved in directory: ", total_images)


testdir = 'celeb_updated_ready_25_june/test/'
n = 0
dropped_count_test = 0
dropped_count_other = 0
#valid_dirs = 0
#out_df = pd.DataFrame(columns=['Test Image', 'Target Image', 'Distance', 'Verified?'])

for subdir, dirs, files in os.walk(testdir):
  for file in files:
    test_path = os.path.join(testdir, file)
    print("Starting Evaluation for Loop ", n, "\n")
    print("Test Image Path: ", test_path)
    tst_embedding = DeepFace.represent(img_path = test_path, model_name ='ArcFace', detector_backend = 'mtcnn', enforce_detection = False)
    if np.sum(tst_embedding) == -1:
      print("Skipping Test Image")
      dropped_count_test +=1
      print("Total Dropped Test Images: ", dropped_count_test)
    else:
      out_df = pd.DataFrame(columns=['Test Image', 'Target Image', 'Distance', 'Verified?'])
      name_save = "benchmarks_of_image_" + file[0:-4] + ".csv"
      print("Saving Initial File as: ", name_save)
      out_df.to_csv(name_save)
      valid_dirs = 0
      iter_df = pd.DataFrame(columns=['Test Image', 'Target Image', 'Distance', 'Verified?'])

      for r_subdir, r_dirs, r_files in os.walk(rootdir):
        if (str(r_subdir[28:32]) != "test"):
          if (r_files):
            path_from = os.path.join(rootdir, r_subdir[28:len(r_subdir)])
            total_files = len(r_files)
            print("Total Files in this directory: ", total_files)
            for i in range(40):
              single_file = os.path.join(path_from, r_files[i])
              print("Path for second image: ", single_file)
              #with tf.device('/device:GPU:0'):
              #df = DeepFace.verify(img1_path = test_path, img2_path = single_file, model_name ='ArcFace', distance_metric = 'cosine', detector_backend = 'mtcnn', enforce_detection = False)
              other_embedding = DeepFace.represent(img_path = single_file, model_name ='ArcFace', detector_backend = 'mtcnn', enforce_detection = False)
              if np.sum(other_embedding) == -1:
                distance = -1
                dropped_count_test +=1
                print("Total Dropped Sample Images: ", dropped_count_other)
              else:
                distance = dst.findCosineDistance(tst_embedding, other_embedding)
              yon = 0
              if(distance <= 0.5):
                yon = 1
              single_file_name = str(r_subdir[28:len(r_subdir)]) + "/" + r_files[i]
              val_out = [file, single_file_name, distance, yon]
              print(val_out)
              iter_df.loc[0] = val_out
              #print(iter_df)
              valid_dirs += 1
              iter_df.to_csv(name_save, mode='a', header=False)
              print("Written to File")
              #print(out_df)
              print("Progress: ", i + 1, " / ", total_files - 1)
              print("\n----------------\n\n")

    #print("Saving checkpoint as: ", name_save)
    #out_df.to_csv(name_save)
    print("Evaluation for Image ", n, " is done")
    n += 1
    print("\n\n***********************************************************************\n\n")
#out_df.to_csv('deepface_benchmarks.csv')

# Deepface Benchmarking
This repository contains all the files and folders along with instructions on running the benchmarking evaluation scripts on any dataset.

## Prerequisites
The major prerequisite that this repository requires is the deepface library. You could easily look up instructions for installing the standard deepface library. However, within this particular project, I would recommend installing a separate version of deepface, using the code below:

```
python3 -m pip install -e git+https://github.com/danyalsaqib/deepface#egg=deepface
```

This particular repository is a fork of the original repository, with two basic changes:
1. If a particular image is corrupt or unreadable for some reason, the image is skipped and the 'represent' fuction returns -1.
2. If an image containes multiple faces that are detected, instead of simply choosing one face to run the detection on, the 'represent' function once again simply returns -1. This is done because multiple faces significantly affect benchmarking criteria.

The installation of this particular repository should automatically initiate the process of installing all dependencies, such as NumPy and Pandas. Once this particular library has been installed, you are ready to go!

## Arrangement of dataset
The datatset that you want to perform the evaluation on should be kept in a quite particular manner. The format of the dataset should be something like this: You should have a folder for each unique person or celebrity, containing some photos of this person. The photos should be clear, and should ideally have only the concerned person's face visible. Hence, a complete dataset folder would have a few folders, each named after the unique person, and each containing a few photos of the unique person. Note that all of these folders should be placed in a single directory.

## Setting up the codebase
You should now place the 'deepface_benchmark_optim_saving.py' file in the same directory as the superfolder containing all unique folders. Hence, the directory should look something like this:

- directory_where_evaluation_sheets_will_be_produced
  - deepface_benchmark_optim_saving.py
  - folder_with_all_the_unique_face_folders
    - person_1
    - person_2
    - person_3

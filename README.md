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
  - superfolder_with_all_the_unique_face_folders
    - person_1
    - person_2
    - person_3

## Modifying Code File
You now have the option of opening up the 'deepface_benchmark_optim_saving.py' file, and making 5 potential changes:

1. On line 22 and line 56 in both the 'rootdir' and 'testdir' variables, change the words from 'celeb_updated_ready_25_june' to 'superfolder_with_all_the_unique_face_folders', whatever your superfolder may be named. This is to tell the 'deepface_benchmark_optim_saving.py' file to look in the appropriate place for the folders of various persons.
2. On line 25, you will see the line: `num_files_test = 5`. In this line, you can change how many images from each folder will be chosen as 'test images'. The recommended number is between 3 and 6, but any number of images may be chosen. You may also choose to leave this variable as it is.
3. On line 87, you will see the line: `for i in range(40):`. In this line, change the number from 40 to however many images there are in each folder. If the number of images in each folder is different than the other, then choose the lowest number. Basically, this number determines how many images from each folder will be tested against our test images.
4. On line 68 and line 92, you have the option of modifying the 'model_name' and 'detector_backend' used for the deepface function. All possible models are listed in the deepface repository.
5. On line 100, you can modify the threshold used to determine if the faces match or not. This threshold can vary between 0 and 1, and you can change it according to your needs, or leave it be. The default value is 0.5.

## Running the evaluation
Now that everything is set up, we can run the evaluation script. Note that the results of the evaluation will all be generated in the same folder as our 'deepface_benchmark_optim_saving.py' script. To run the script, open a terminal, change into our target directory (the directory where the script and the superfolder are present), and then simply run:

```
python3 deepface_benchmark_optim_saving.py
```

This will now begin the evaluation process. Firstly, a separate test folder will be created, where 'num_files' test images from each person will be chosen and copied. Then, for each test image, evaluation will run through the dataset. This may take quite some time.

## Results
After the evaluation script has run its course, we will have several csv files, each corresponding to a test image. Each test image will have been evaluated against several images of all other categories. You can open up each csv file and check its contents. Each csv file has 4 columns:
1. Test Image:    The image's own name, as saved in the test folder.
2. Target Image:  The image that was checked to determine similarities in the faces.
3. Distance:      Between 0 and 1, what the distance is between the two images. The greater the distance, the more dissimilar the faces.
4. Verified: If the distance is less than the defined threshold, then the faces are listed as belonging to the same person i.e 1. Dissimilar faces means a 0.

# Deepface Benchmarking
This repository contains all the files and folders along with instructions on running the benchmarking evaluation scripts on any dataset. The files have been primarily run and tested on an Ubuntu 20.04 machine.

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
1. Test Image: The image's own name, as saved in the test folder.
2. Target Image: The image that was checked to determine similarities in the faces.
3. Distance: Between 0 and 1, what the distance is between the two images. The greater the distance, the more dissimilar the faces.
4. Verified: If the distance is less than the defined threshold, then the faces are listed as belonging to the same person i.e 1. Dissimilar faces means a 0.

An example output csv file is shown below:

![Overall Same](https://github.com/danyalsaqib/deepface_benchmarking/blob/main/csv_example_image.png)

## Visualization and Overall Results
Now that we have all of our results, we will probably want to do two main things. Firstly, we want to visualize these results, and extract some meaningful information from them. Secondly, we will want to see not just the results for individual imeages, but overall results to better understand our model and our dataset. We can do both of these things using the Python Notebook 'face_benchmarking_visualization_2.ipynb'.

The notebook is originally meant to be used on Colab. However, it can just as easily be run on a Jupyter Notebook with slight modifications.

### For Colab
For using the Notebook on Colab, you first need to go to your Google Drive, and create a new Folder where the data will be stored. In our case, the folder was named 'face_benchmark_results_2'. After creating this folder in 'My Drive', go ahead and upload all of the generated csv files from the previous section into this folder. After all of the csv files have been uploaded, you need to create two additional folders within the same directory. The first folder will be named 'Results", and the second folder will be named 'Overall Statistics'. Leave these two folders empty for now. The directory shoud look something like this:

- face_benchmark_results_2
  - Results
  - Test
  - benchmarks_of_image_person_1_img_0.csv
  - benchmarks_of_image_person_1_img_1.csv
  - benchmarks_of_image_person_2_img_0.csv
  - benchmarks_of_image_person_2_img_1.csv

You can now open up Google Colab, and specify your folder name if it is different than 'face_benchmark_results_2'. You can do this by simply replacing 'face_benchmark_results_2' with your folder's name in the third cell in the line `%cd drive/My Drive/face_benchmark_results_2/`. You are now ready to run the entire notebook.

### For Jupyter
Create a new folder, where you can place the notebook file 'face_benchmarking_visualization_2.ipynb'. Now within this folder, create a new folder, and name it to your liking. In our case, the folder was named 'face_benchmark_results_2'. Within this folder, copy all of the csv files that were generated during the previous step. Now within this folder, you need to create two additional folders within the same directory. The first folder will be named 'Results", and the second folder will be named 'Overall Statistics'. Leave these two folders empty for now. The directory shoud look something like this:

- face_benchmarking_visualization_2.ipynb
- face_benchmark_results_2
  - Results
  - Test
  - benchmarks_of_image_person_1_img_0.csv
  - benchmarks_of_image_person_1_img_1.csv
  - benchmarks_of_image_person_2_img_0.csv
  - benchmarks_of_image_person_2_img_1.csv

You can now open up Jupyter, and firstly comment out the following lines in the first cell.

```
from google.colab import drive
drive.mount('/content/drive', force_remount=True)
```
Secondly, in the third cell, you will see the line `%cd drive/My Drive/face_benchmark_results_2/`. Remove the 'drive/My Drive/' portion of the line, to change the line to `%cd face_benchmark_results_2/`. You can also specify your folder name if it is different than 'face_benchmark_results_2'. You can do this by simply replacing 'face_benchmark_results_2' with your folder's name. After all of this is done, you are now ready to run the entire notebook.

## Interpreting the Output
After the notebook as been successfully set up as in the previous section, you should run all the cells in the notebook. After the execution has successfully completed, you will get histograms of each individual image's results saved in the 'Results' directory we created earlier. Additionally, you will also get 2 csv files in the 'Overall Statistics' directory we create earlier, that will have the final overall results in their complete, cleaned form. The most important visualization of the lot is not the visualization of the individual images, but the 2 histograms that display the overall statistics of the evaluation. The 2 histograms showcase two different aspects of the evaluation. The first histogram shows distances for images that belong to the same category i.e images of the same person. These distances should be ideally quite lower, as images of the same person should have greater similarity. The second histogram shows distances for images that belong to different categories i.e images of different people. These distances should be ideally higher, as images of different people should have greater dissimilarities.

Shown below are two example histograms of the overall results:
![Overall Same](https://github.com/danyalsaqib/deepface_benchmarking/blob/main/Overall%20Statistics%20-%20Distances%20for%20Same%20Catgeory%20of%20Images.png)
![Overall Different](https://github.com/danyalsaqib/deepface_benchmarking/blob/main/Overall%20Statistics%20-%20Distances%20for%20Different%20Catgeory%20of%20Images.png)

You will notice that within the notebook, along with these histograms, several statistical parameters related to the overall data will be displayed. These can give you an even better picture about the model's performance, and your dataset.

## Conclusion
If you follow all the instructions correctly, the repository provides a convenient way to benchmark various deepface models on large datasets. We hope the instructions are clear and easy-to-run for all. Any feedback or comments would be highly appreciated.

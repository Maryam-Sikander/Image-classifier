#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules

from os import listdir
# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
        # Create an empty dictionary to store the results
    results_dic = {}
    # Get the filenames from the image directory
    filename_list = listdir(image_dir)
    # Process each filename in the filename list
    for filename in filename_list:
        # Check if the filename starts with a "."
        if filename.startswith("."):
            continue
        # Split the filename into words
        word_list = filename.lower().split("_")
        # Create a temporary label variable
        pet_label = ""
        # Process each word in the word list
        for word in word_list:
            # Check if the word contains only alphabetical characters
            if word.isalpha():
                # Append the word to the pet label with a space
                pet_label += word + " "
        # Remove leading/trailing whitespaces from the pet label
        pet_label = pet_label.strip()
        # Add the pet label to the results dictionary
        results_dic[filename] = [pet_label]
    return results_dic
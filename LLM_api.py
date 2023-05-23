"""
This module contains functions for interacting with the LLM API.

The LLM API provides access to a range of natural language processing
capabilities, including text generation, question answering, and sentiment
analysis. This module provides a simple interface for making API requests
and processing the results.
"""

import poe
from Image_captioning import generate_caption
client = poe.Client("pqwbrzjCafmAXogA2g7luA%3D%3D")
has_image= True

def concatenate_strings(string_list):
    """
    Concatenates a list of strings into a single string.

    Args:
        string_list (list): A list of strings.

    Returns:
        str: A string containing all the input strings concatenated together.
    """
    concatenated_string = ''.join(string_list)
    return concatenated_string

def reply(message,has_image,sample_img):
    """
    Sends a message to the LLM API and returns the response as a concatenated string.

    If `has_image` is True, generates a caption for `sample_img` using the `generate_caption`
    function, and adds it to the beginning of the `message` before sending it to the API.

    Args:
        message (str): The message to send to the LLM API.
        has_image (bool): Whether or not `sample_img` is provided.
        sample_img (PIL.Image.Image): An image to generate a caption for, if `has_image` is True.

    Returns:
        str: The concatenated response from the LLM API, with any header information removed.
    """
    if has_image:
        caption = generate_caption(sample_img)
        message =  "assume that I showed you a photo that: " + caption \
                   + ". now, given the information about the \
                    photo, I'll tell you this: " + message
    outlist = []
    for chunk in client.send_message("nutria", message):
        outlist.append(chunk["text_new"])
    del outlist[0]
    stringlist = concatenate_strings(outlist)
    return stringlist
# capybara for sage

#not stable
def reply_with_photo(message,has_image,sample_img):
    """
    Sends a message to the LLM API and returns the response as a string.

    If `has_image` is True, generates a caption for `sample_img` using the `generate_caption`
    function, and adds it to the beginning of the `message` before sending it to the API.

    After sending the message to the API, extracts information from the response to determine
    whether or not the user requested an image. If an image is requested, calls a function to
    retrieve the image and returns it along with the text response.

    Args:
        message (str): The message to send to the LLM API.
        has_image (bool): Whether or not `sample_img` is provided.
        sample_img (PIL.Image.Image): An image to generate a caption for, if `has_image` is True.

    Returns:
        str: If no image is requested, returns the text response from the LLM API as a string.
        If an image is requested, returns a tuple containing the text response and the image.
    """
    if has_image:
        caption = generate_caption(sample_img)
        message =  "assume that I showed you a photo that: " + caption \
               + ". now, given the information about the photo, I'll \
                tell you this: " + message
    output_list = []
    result = []
    for chunk in client.send_message("nutria", message):
        output_list.append(chunk["text_new"])
    my_string = "".join(output_list)
    my_list = my_string.split("\n")

    # Calling google search api
    if my_list[1]=="Yes":
        # use my_list[3] as it contains the description of \
        # the photo required and you have to make a function\
        # that returns an image and put it in the return of the reply function.
        pass
    return my_list[5]

# reply("what is this kind of sport",0,"")

# reply("what is the man wearing?",1,"35506150_cbdb630f4f.jpg")

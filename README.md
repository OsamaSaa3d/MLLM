# MLLM: Multi-Modal Large Language Model
MLLM is a Multi-Modal Large Language Model that combines the power of GPT-3.5 with an image-to-text model. This repository contains the code and resources to build and run the MMLLM.

# Overview
The MMLLM is a language model that can understand both text and images. It uses GPT-3.5 as a base model for text processing and integrates an image-to-text model to process images. The image-to-text model is trained on a large dataset of images and their descriptions, which allows it to accurately describe the content of an image.

We used prompt engineering to integrate our own image-to-text model with the GPT-3.5 API. This allows the MMLLM to generate text that is conditioned on both the input text and the input image.

# Getting Started
To get started with the MLLM, you will need to have access to the GPT-3.5 API. You will also need to download the image-to-text model and its associated data.

Once you have the necessary resources, you can use the provided code to build and run the MLLM. The main script is main.py, which takes as input a text prompt and an image file, and generates a description of the image conditioned on the input text.

# Usage
Once you have your gpt-3.5-turbo API, you can use your token to access the LLM.

Then you need the pretrained weights of the image-to-text model or you can just uncomment everything in the train.py and run it so that it trains the model.

Once you've that you can just run the main.py file and off you go.

# Sample Outputs

![1-CisK0zJfr-transformed](https://github.com/OsamaSaa3d/MLLM/assets/32080534/48ef4b39-9e10-4f5b-bb1b-ae281f69fd16)

![2-_wWl1mshQ-transformed](https://github.com/OsamaSaa3d/MLLM/assets/32080534/9b0b0090-768e-4ab4-84be-8c40323cf5c0)

![3-8NPHL1eJY-transformed](https://github.com/OsamaSaa3d/MLLM/assets/32080534/020c3310-cdc5-4681-9468-3d0763846677)

# Resources
This GitHub repository contains the following resources:

main.py: the main script for running the MLLM.
image_captioning_model.py: the image-to-text model implementation.
image_captioning_model_weights.h5: the pre-trained weights for the image-to-text model.
train.py: this file is what you need if you want to retrain the image-to-text model.

# Acknowledgments
This project was inspired by the work of OpenAI and the GPT-3 language model. We would like to thank the developers and researchers who contributed to the development of these tools.

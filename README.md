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

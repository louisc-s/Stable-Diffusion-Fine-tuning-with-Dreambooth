# Stable-Diffusion-Fine-tuning-with-Dreambooth
Code for finetuing Stable Diffusion with custom image dataset

## Overview

This code is utilised alongside the Diffusers library to produce a finetuned stable diffusion model capable of producing life-like generative images based on the custom image dataset provided.

## Project Structure 

1. create_json.py - creates a metadata json file for custom hugging face dataset using a prexisting csv file 

2. text_to_image_script.sh - script to create text-to-image finetuned model (uses metadata)

3. dreambooth_model - jupyter notebook to create dreambooth finetuned model (does not use metadata, only images)

## Author 

Louis Chapo-Saunders

#!/usr/bin/env python
# coding=utf-8

import os
import requests
import gpt_2_simple as gpt2

model_name = "124M"
file_name = "./datasets/input.txt"

if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/


sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              file_name,
              model_name=model_name,
              steps=10)
              
gpt2.generate(sess)

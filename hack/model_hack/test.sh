#!/bin/bash

python -m trainer.task \
    --save_steps -1 \
    --num_train_epochs 1 \
    --per_device_train_batch_size 1 \
    --model_type gpt2-medium \
    --model_name_or_path gpt2-medium \
    --tokenizer_name gpt2 \
    --overwrite_output_dir True \
    --do_train \
    --cache_dir '../datasets/cache' \
    --output_dir '../datasets/output' \
    --train_file '../datasets/train.txt'
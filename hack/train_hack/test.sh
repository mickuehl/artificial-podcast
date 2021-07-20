#!/bin/bash

python -m trainer.run \
    --model_type gpt2 \
    --model_name_or_path gpt2-medium \
    --tokenizer_name gpt2 \
    --num_train_epochs 1 \
    --output_dir '../datasets/output' \
    --validation_file '../datasets/eval.txt' \
    --train_file '../datasets/train.txt'
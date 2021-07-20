#!/bin/bash

TRAIN_FILE=gs://art-podcast/datasets/input.txt

gcloud ai-platform local train \
    --package-path trainer \
    --module-name trainer.run \
    -- \
    --save_steps -1 \
    --num_train_epochs 1 \
    --per_device_train_batch_size 1 \
    --model_type gpt2-medium \
    --model_name_or_path gpt2-medium \
    --do_train \
    --output_dir './datasets/output' \
    --cache_dir './datasets/cache' \
    --train_file $TRAIN_FILE

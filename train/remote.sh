#!/bin/bash

# see https://cloud.google.com/ai-platform/training/docs/using-tpus

REGION=europe-west4

DATE=`date '+%Y%m%d_%H%M%S'`
JOB_NAME=temp_$DATE

TRAIN_FILE=gs://art-podcast/datasets/train.txt
JOB_DIR=gs://art-podcast/jobs/$JOB_NAME

# see https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training

gcloud ai-platform jobs submit training $JOB_NAME \
    --package-path trainer \
    --module-name trainer.run \
    --runtime-version 2.4 \
    --python-version 3.7 \
    --job-dir $JOB_DIR \
    --region $REGION \
    --config resources.yml \
    -- \
    --save_steps -1 \
    --num_train_epochs 1 \
    --per_device_train_batch_size 1 \
    --model_type gpt2-medium \
    --model_name_or_path gpt2-medium \
    --tokenizer_name gpt2 \
    --do_train \
    --output_dir './data/output' \
    --cache_dir './data/cache' \
    --train_file $TRAIN_FILE

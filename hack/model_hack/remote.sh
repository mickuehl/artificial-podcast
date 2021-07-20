#!/bin/bash

export REGION=europe-west4

DATE=`date '+%Y%m%d_%H%M%S'`
JOB_NAME=temp_$DATE

TRAIN_FILE=gs://art-podcast/datasets/input.txt
JOB_DIR=gs://art-podcast/jobs/$JOB_NAME

gcloud ai-platform jobs submit training $JOB_NAME \
    --runtime-version 2.4 \
    --python-version 3.7 \
    --job-dir $JOB_DIR \
    --package-path trainer \
    --module-name trainer.task \
    --region $REGION \
    -- \
    --save_steps -1 \
    --num_train_epochs 1 \
    --per_device_train_batch_size 1 \
    --model_type gpt2-medium \
    --model_name_or_path gpt2-medium \
    --do_train \
    --output_dir './data/output' \
    --cache_dir './data/cache' \
    --train_file $TRAIN_FILE

gcloud ml-engine local train \
    --module-name=trainer.task \
    --package-path=trainer/ \
    -- \
    --train-file=$TRAIN_FILE \
    --word-index-file=$WORD_INDEX_FILE \
    --job-dir=$JOB_DIR
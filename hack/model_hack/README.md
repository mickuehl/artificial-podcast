## README


```shell
python -m trainer.task \
    --save_steps -1 \
    --num_train_epochs 1 \
    --per_device_train_batch_size 1 \
    --model_type gpt2-medium \
    --model_name_or_path gpt2-medium \
    --do_train \
    --output_dir '../datasets/output' \
    --train_file '../datasets/mini.txt'
```


```shell

DATE=`date '+%Y%m%d_%H%M%S'`
export JOB_NAME=temp_$DATE
export TRAIN_FILE=gs://art-podcast/datasets/input.txt
export REGION=europe-west4
export JOB_DIR=gs://art-podcast/jobs/$JOB_NAME

gcloud ai-platform jobs submit training $JOB_NAME \
    --runtime-version 2.4 \
    --python-version 3.7 \
    --job-dir=$JOB_DIR \
    --package-path=trainer \
    --module-name trainer.task \
    --region $REGION \
    -- \
    --fp16 \
    --save_steps -1 \
    --num_train_epochs 1 \
    --per_device_train_batch_size 1 \
    --model_type gpt2-medium \
    --model_name_or_path gpt2-medium \
    --do_train \
    --output_dir './output' \
    --train_file $TRAIN_FILE

```

## artificial podcast

### Development

pip install -U pip pip install --user --upgrade virtualenv

virtualenv venv 
source venv/bin/activate

pip install -r requirements.txt


### Training

python train.py \
    --save_steps -1 \
    --num_train_epochs 1 \
    --per_device_train_batch_size 1 \
    --model_type gpt2-medium \
    --model_name_or_path gpt2-medium \
    --do_train \
    --do_eval \
    --output_dir "./datasets/output" \
    --train_file "./datasets/train.txt" \
    --validation_file "./datasets/eval.txt"


python train.py \
    --save_steps -1 \
    --num_train_epochs 1 \
    --per_device_train_batch_size 1 \
    --model_type gpt2-medium \
    --model_name_or_path gpt2-medium \
    --do_train \
    --output_dir "./datasets/output" \
    --train_file "./datasets/input.txt"


for CUDA devices
--fp16 \


### Cleanup

rm -rf /Users/turing/.cache/huggingface/transformers
rm -rf /Users/turing/.cache/huggingface/datasets


### Reference

https://cloud.google.com/ai-platform/docs/getting-started-keras

https://cloud.google.com/sdk/gcloud/reference/ml-engine

https://cloud.google.com/ai-platform/training/docs/versioning

https://github.com/GoogleCloudPlatform/cloudml-samples/tree/master/tensorflow

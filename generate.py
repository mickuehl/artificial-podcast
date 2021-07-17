#!/usr/bin/env python
# coding=utf-8

#from transformers import GPT2Tokenizer, TFGPT2Model, GPT2LMHeadModel, TFGPT2LMHeadModel
#from transformers import set_seed, pipeline


# setup imports to use the model
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

def generate():
 
    prompt = 'well fuck off then'
    
    model = TFGPT2LMHeadModel.from_pretrained("./datasets/output", from_pt=True)
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    input_word_vect = tokenizer.encode(prompt, return_tensors='tf')

    generated_text = model.generate(
        input_word_vect, 
        max_length=150,  
        num_return_sequences=5,
        no_repeat_ngram_size=2,
        repetition_penalty=1.5,
        top_p=0.92,
        temperature=.85,
        do_sample=True,
        top_k=125,
        early_stopping=True
    )

    for i, vect in enumerate(generated_text):
        print("{}: {}".format(i,tokenizer.decode(vect, skip_special_tokens=True)))
        print()
    
    
if __name__ == "__main__":
    generate()
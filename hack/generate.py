#!/usr/bin/env python
# coding=utf-8

# see https://www.tensorflow.org/api_docs/python/tf/Tensor#__len__
# see https://gist.github.com/mickuehl/56e6b83b2f14408a1c1e386c55069bfb

# setup imports to use the model
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
from tensorflow import concat

model_dir = "../datasets/output"

model = TFGPT2LMHeadModel.from_pretrained(model_dir, from_pt=True)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")


def generate(prompt, max_words):
    txt = model.generate(
        prompt, 
        max_length=max_words,  
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        repetition_penalty=1.5,
        top_p=0.92,
        temperature=.85,
        do_sample=True,
        top_k=125,
        early_stopping=True
    )
    return txt


def generate_text(prompt, min_words, prompt_words, gen_batch):
    i = 1

    print("\nIteration {}\n".format(i))
    
    prompt_tokens = tokenizer.encode(prompt, return_tensors='tf')
    txt_generated = generate(prompt_tokens, gen_batch)
    txt = txt_generated[0]

    while len(txt) < min_words:
        i += 1

        n = len(txt_generated[0]) - prompt_words
        tokens = txt_generated[0][n:]
        gen_prompt = tokenizer.decode(tokens, skip_special_tokens=True)
        prompt_tokens = tokenizer.encode(gen_prompt, return_tensors='tf')

        print("\nIteration {}\n".format(i))
        
        txt_generated = generate(prompt_tokens, gen_batch)
        txt2 = txt_generated[0][prompt_words:]

        txt = concat([txt, txt2],0)

    gen_text = tokenizer.decode(txt, skip_special_tokens=True)
    print("\n{}".format(gen_text))


if __name__ == "__main__":
    prompt = 'Awareness came to him slowly, the events of the day slowly fighting their way'

    generate_text(prompt, 1000, 8, 300)
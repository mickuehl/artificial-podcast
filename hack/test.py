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

def hack():
 
    prompt = '"You know I wouldn? You should see what these Slytherins have done here! Just look!" Hermione said,'
    
    input_word_vect = tokenizer.encode(prompt, return_tensors='tf')
    
    print(input_word_vect)
    print(input_word_vect.shape)

    vect = concat([input_word_vect, input_word_vect],1)

    #txt1 = tokenizer.decode(vect[0], skip_special_tokens=True)
    
    print("")
    print(input_word_vect)

    print("")
    print(vect)

    vect2 = concat([vect, input_word_vect],1)

    print("")
    print(vect2)

    

def generate2():
 
    model = TFGPT2LMHeadModel.from_pretrained("../datasets/output", from_pt=True)
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    prompt1 = '"You know I wouldn? You should see what these Slytherins have done here! Just look!" Hermione said,'

    print("")
    print(prompt1)
    print("---")

    prompt_vect1 = tokenizer.encode(prompt1, return_tensors='tf')

    generated_text1 = model.generate(
        prompt_vect1, 
        max_length=300,  
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        repetition_penalty=1.5,
        top_p=0.92,
        temperature=.85,
        do_sample=True,
        top_k=125,
        early_stopping=True
    )

    txt1 = tokenizer.decode(generated_text1[0], skip_special_tokens=True)
    print("")
    print("{}".format(txt1))

    words = 8

    n = len(generated_text1[0]) - words
    prompt2 = tokenizer.decode(generated_text1[0][n:], skip_special_tokens=True)

    print("---")
    print("{}".format(prompt2))
    print("")

    prompt_vect2 = tokenizer.encode(prompt2, return_tensors='tf')
    
    generated_text2 = model.generate(
        prompt_vect2, 
        max_length=300,  
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        repetition_penalty=1.5,
        top_p=0.92,
        temperature=.85,
        do_sample=True,
        top_k=125,
        early_stopping=True
    )
    
    txt2 = tokenizer.decode(generated_text2[0][words:], skip_special_tokens=True)
    print("")
    print("{}".format(txt2))


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



def generate_text2(prompt):
    i = 0
    
    prompt_words = 8
    n_word = 300

    txt = tokenizer.encode(prompt, return_tensors='tf')
    prompt_tokens = tokenizer.encode(prompt, return_tensors='tf')

    while i < 2:
        i += 1
        print("Iteration {}".format(i))
        print("")

        txt_generated = generate(prompt_tokens, n_word)
        txt = concat([txt, txt_generated[0][prompt_words:]],0)

        n = len(txt_generated[0]) - prompt_words
        prompt_tokens = tokenizer.decode(txt_generated[0][n:], skip_special_tokens=True)

    #txt1 = tokenizer.decode(txt[0], skip_special_tokens=True)
    print(txt)
    #print("{}".format(txt1))


def generate_text(prompt):
    i = 1

    prompt_words = 8
    n_word = 300

    print("Iteration {}".format(i))
    print("")

    prompt_tokens = tokenizer.encode(prompt, return_tensors='tf')
    txt = generate(prompt_tokens, n_word)[0]
    
    while i < 2:
        i += 1
        print("Iteration {}".format(i))
        print("")

        txt_generated = generate(prompt_tokens, n_word)
        txt2 = txt_generated[0][prompt_words:]

        txt = concat([txt, txt2],0)

        n = len(txt_generated[0]) - prompt_words
        prompt_tokens = tokenizer.decode(txt_generated[0][n:], skip_special_tokens=True)

    gen_text = tokenizer.decode(txt, skip_special_tokens=True)
    print("{}".format(gen_text))


if __name__ == "__main__":
    prompt = '"You know I wouldn? You should see what these Slytherins have done here! Just look!" Hermione said,'
    
    generate_text(prompt)
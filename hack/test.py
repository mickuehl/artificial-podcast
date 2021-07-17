#!/usr/bin/env python
# coding=utf-8

text1 = 'It was obvious that Remus wasn\'t talking to Harry. He immediately reached for the wand, and moved his right hand back over it as though he wanted nothing more than a good time on her part. She made no move against him despite how much she leaned in close with one of the brothers while making small talk about their lives before going silent again. It took just two quick strokes from Dumbledore\'s fingers through Snape who soon collapsed into silence behind them all like an exhausted horse after losing nearly every battle they had ever been involved or fought by blood—even if Voldemort never spoke up once between seasons three-five due…well fuck off then'
#text2 = 'He ran to the edge of their camp, running up it in a circle and pulling out his wand. Voldemort spun around at that moment. He was already halfway down there before he noticed they were gone. "Look who's back," said Harry with amusement as soon Asgore appeared next door on some rubble facing an empty building above them; A large piece for which anyone could make muggle bombs if necessary, along side plenty more stuff from Dumbledore'S school supplies collection – presumably those found by Snape… but still nothing like this Hogwarts house full…… Except not quite…. The boy sighed deeply just then realizing why Ginny had taken him so'
#text3 = '"You know I wouldn? You should see what these Slytherins have done here! Just look!" Hermione said, looking up to find Draco standing over her. He reached into his robes and pulled out a black book that appeared slightly bigger than hers as he stared at it in disbelief for several moments. She shrugged off the surprise but found herself feeling awkward about doing so just then when she heard 'happening' from outside of Hogwarts – they had been there already."No," Harry offered dismissively "Hermione needs your help with something else you can give me if we need anything more before going back home later on today.""I'll take care now; let's go get some dinner first-"Ron laughed loudly like an idiot'

# setup imports to use the model
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

def hack():
 
    prompt = '"You know I wouldn? You should see what these Slytherins have done here! Just look!" Hermione said,'
    
    #model = TFGPT2LMHeadModel.from_pretrained("../datasets/output", from_pt=True)
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    input_word_vect = tokenizer.encode(prompt, return_tensors='tf')


    txt1 = tokenizer.decode(input_word_vect[0], skip_special_tokens=True)
    words1 = txt1.split(' ')
    
    print("")
    print("{}".format(txt1))

    print("")
    print(words1)

    print("")
    print(input_word_vect[0])


    n = len(input_word_vect[0]) - 6
    prompt2 = tokenizer.decode(input_word_vect[0][n:], skip_special_tokens=True)
    print("")
    print(prompt2)

    print("")
    print(input_word_vect[0][n:])
    

def generate():
 
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

    
if __name__ == "__main__":
    generate()
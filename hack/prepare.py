#!/usr/bin/env python
# coding=utf-8

from sklearn.model_selection import train_test_split

INPUT_FILE = '../datasets/input.txt'

def prepare():

    with open(INPUT_FILE, 'r') as data:
        dataset = ["<START>" + x.strip() for x in data.readlines()]

    train, eval = train_test_split(dataset, train_size=.9, random_state=2020)
    print("training size:" + str(len(train)))
    print("Evaluation size: " + str(len(eval)))

    with open('../datasets/train.txt', 'w') as file_handle:
        file_handle.write("<END>".join(train))

    with open('../datasets/eval.txt', 'w') as file_handle:
        file_handle.write("<END>".join(eval))
    
    
if __name__ == "__main__":
    prepare()
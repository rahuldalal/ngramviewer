import ngram_finder as ng
import string
import os

n_max = 5



def tokenize_text(text):
    if not text or text == '':
        return None
    tokenized_words = [word.strip(string.punctuation) for word in text.split()]
    print(tokenized_words)
    return tokenized_words

def read_text(folder_path):
    print('in load_data')
    for dirpath, dir_list, file_list in os.walk(folder_path):
        print(file_list)
        for file_name in file_list:
            file_name = os.path.join(dirpath, file_name)
            print(file_name)
            with open(file_name, encoding="utf8") as file:
                return file.read()

def create_all_ngrams(tokenized_words):
    ngram_tries = list()
    print('Tokenized: {}'.format(tokenized_words))
    if not tokenized_words or len(tokenized_words) ==0:
        print("Pleas provide valid non empty text corpus")
    else:
        print('Max_n : {}'.format(n_max))
        for i in range(n_max):
            ngram = ng.Ngram()
            ngram.build_ngram(i + 1, tokenized_words)
            ngram_tries.append(ngram)
    return ngram_tries

def process_data(folder_name):
    total_words = 0
    tokenized_words = tokenize_text(read_text(folder_name))
    total_words += len(tokenized_words)
    return (create_all_ngrams(tokenized_words),total_words)

def get_frequency(text, total_words, ngram, n):
    tokenized_words = tokenize_text(text)
    if len(tokenized_words) < n:
        return 0
    return ngram.get_count(tokenized_words)/(total_words-n+1)





# ngram_list, total_words = process_data('task')
# print('Words processed : {}'.format(total_words))
# check_text = 'in love with the one'
# print('{} : {}'.format(check_text,get_frequency(check_text, total_words, ngram_list[4], 5)))




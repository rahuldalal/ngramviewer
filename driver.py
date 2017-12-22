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
    home = os.path.expanduser("~")
    print('in load_data')
    for dirpath, dir_list, file_list in os.walk(folder_path):
        print(dirpath)
        print(dir_list)
        print(file_list)
        for file_name in file_list:
            fname = os.path.join(dirpath, file_name)
            print(fname)
            with open(fname, encoding="utf8") as file:
                return file.read()

def create_all_ngrams(tokenized_words, ngram_list):
    print('Tokenized: {}'.format(tokenized_words))
    if not tokenized_words or len(tokenized_words) ==0:
        print("Pleas provide valid non empty text corpus")
    else:
        print('Max_n : {}'.format(n_max))
        for i in range(n_max):
            ngram_list[i].build_ngram(i + 1, tokenized_words)
    return ngram_list

def process_data(folder_name, ngram_list):
    total_words = 0
    tokenized_words = tokenize_text(read_text(folder_name))
    total_words += len(tokenized_words)
    return (create_all_ngrams(tokenized_words, ngram_list),total_words)

def get_frequency(text, total_words, ngram, n):
    tokenized_words = tokenize_text(text)
    if len(tokenized_words) < n:
        return 0
    return ngram.get_count(tokenized_words)/(total_words-n+1)




ngram_list = list()
for i in range(n_max):
    ngram = ng.Ngram()
    ngram_list.append(ngram)
ngram_list, total_words = process_data('sample', ngram_list)
print('Words processed : {}'.format(total_words))
check_text = '2 3 4 5 1'
print('{} : {}'.format(check_text,get_frequency(check_text, total_words, ngram_list[4], 5)))







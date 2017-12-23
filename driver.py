import ngram_finder as ng
import string
import os
import pickle

n_max = 5
final_model = dict()
labels=list()

def tokenize_text(text):
    if not text or text == '':
        return None
    tokenized_words = [word.strip(string.punctuation) for word in text.split()]
    return tokenized_words

def read_text(folder_path):
    text_read = ""
    dir_paths = list()
    for dirpath, dir_list, file_list in os.walk(folder_path):
        for file_name in file_list:
            fname = os.path.join(dirpath, file_name)
            with open(fname, encoding="utf8") as file:
                text_read += file.read()
        return text_read

def create_all_ngrams(tokenized_words, ngram_list):
    if not tokenized_words or len(tokenized_words) ==0:
        print("Pleas provide valid non empty text corpus")
    else:
        for i in range(n_max):
            ngram_list[i].build_ngram(i + 1, tokenized_words)
    return ngram_list

def process_data(raw_text, ngram_list):
    total_words = 0
    tokenized_words = tokenize_text(raw_text)
    total_words += len(tokenized_words)
    return (create_all_ngrams(tokenized_words, ngram_list),total_words)

def get_frequency(text, total_words, ngram_list):
    tokenized_words = tokenize_text(text)
    n = len(tokenized_words)
    return ngram_list[n-1].get_count(tokenized_words)/(total_words-n+1)

def run_model(folder_path='task'):
    model = dict()
    total_text = ''
    for dirpath, dir_list, file_list in os.walk(folder_path):
        if dir_list and len(dir_list) > 0:
            for dir_name in dir_list:
                print('Building Ngrams for year {}'.format(dir_name))
                dir_path = os.path.join(dirpath, dir_name)
                ngram_list = list()
                for i in range(n_max):
                    ngram = ng.Ngram()
                    ngram_list.append(ngram)
                total_text = read_text(dir_path)
                ngram_list, total_words = process_data(total_text, ngram_list)
                model[dir_name]=dict()
                labels.append(dir_name)
                model[dir_name]['total_words'] = total_words
                model[dir_name]['ngram_list'] = ngram_list
                print('Words processed in {}: {}...Ngrams built'.format(dir_name, total_words))
    global final_model
    final_model = model

def find_ngram_freq(check_text):
    print('Loading model')
    if not final_model:
        run_model()
    print('Model loaded....finding fequency')
    freq_year = dict()
    for key, value in final_model.items():
        freq_year[key] = round(get_frequency(check_text, value.get('total_words'), value.get('ngram_list')) * 100, 4)
    return freq_year

def find_ngram_freq_multiple(terms):
    print('In find ngram freq mul terms')
    terms = terms.split(',')
    all_term_freq = list()
    for term in terms:
        term_freq = list()
        for year,freq in find_ngram_freq(term).items():
            term_freq.append(freq)
        all_term_freq.append(term_freq)
    return labels, all_term_freq


if __name__ == "__main__":
    run_model(os.path.join(os.getcwd(), 'task'))

# check_text = 'and'
# print('{} : {}'.format(check_text,get_frequency(check_text, total_words, ngram_list[0], 1)))







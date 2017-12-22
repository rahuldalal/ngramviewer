import ngram_finder as ng
import string
import os
import pickle

n_max = 5



def tokenize_text(text):
    if not text or text == '':
        return None
    tokenized_words = [word.strip(string.punctuation) for word in text.split()]
    # print(tokenized_words)
    return tokenized_words

def read_text(folder_path):
    text_read = ""
    dir_paths = list()
    # print('in read text')
    # print(os.getcwd())
    # print(folder_path)
    for dirpath, dir_list, file_list in os.walk(folder_path):
        # print(dirpath)
        # print(dir_list)
        # print(file_list)
        for file_name in file_list:
            fname = os.path.join(dirpath, file_name)
            # print(fname)
            with open(fname, encoding="utf8") as file:
                text_read += file.read()
        if dir_list and len(dir_list) > 0:
            for dir_name in dir_list:
                dir_path = os.path.join(dirpath, dir_name)
                # print(dir_path)
                dir_paths.append(dir_path)
        # print(text_read)
        return dir_paths, text_read

def create_all_ngrams(tokenized_words, ngram_list):
    # print('Tokenized: {}'.format(tokenized_words))
    if not tokenized_words or len(tokenized_words) ==0:
        print("Pleas provide valid non empty text corpus")
    else:
        # print('Max_n : {}'.format(n_max))
        print('len(ngram_list) : {}'.format(len(ngram_list)))
        for i in range(n_max):
            # print('index : {}'.format(i))
            # print('n_max : {}'.format(n_max))
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


def traverse_dirs(folder_name, total_text):
    # print(folder_name)
    dir_list, file_text = read_text(folder_name)
    total_text += " " +file_text
    if dir_list and len(dir_list) > 0:
        for dir in dir_list:
            total_text = traverse_dirs(dir, total_text)
    return total_text

def run_model(folder_name='task'):
    ngram_list = list()
    total_text = ''
    for i in range(n_max):
        ngram = ng.Ngram()
        ngram_list.append(ngram)
    total_text = traverse_dirs(folder_name,'')
    # print('Run model - len(ngram_list) : {}'.format(len(ngram_list)))
    ngram_list, total_words = process_data(total_text, ngram_list)
    # print('Words processed : {}'.format(total_words))
    model ={
        'total_words': total_words,
        'ngram_list': ngram_list,
    }
    model_file_name = 'ngram_struct'
    try:
        with open(os.path.join(os.getcwd(), model_file_name), "wb") as f:
            pickle.dump(model, f)
    except Exception as e:
        print("ERROR: Exception while trying to save model. " + str(e))
    return(model)

def load_model(model_file_name='ngram_struct'):
    try:
        with open(os.path.join('.', model_file_name), "rb") as f:
            model = pickle.load(f)
            return model
    except Exception as e:
        print('No Ngram structure saved....Creating Ngram structure')
        run_model()

def find_ngram_freq(check_text):
    print('Loading model')
    model = load_model()
    print('Model loaded....finding fequence')
    return get_frequency(check_text, model.get('total_words'), model.get('ngram_list'))*100

if __name__ == "__main__":
    run_model(os.path.join(os.getcwd(), 'task'))

# check_text = 'and'
# print('{} : {}'.format(check_text,get_frequency(check_text, total_words, ngram_list[0], 1)))







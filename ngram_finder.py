import os


class Node:
    def __init__(self, count=0):
        self.count = count
        self.children = dict()


class Ngram:
    def __init__(self):
        self.root = Node()

    def add(self, words, current_node):
        # print("Adding: {}".format(words))
        for word in words:
            if not current_node.children:
                # print('Creating child')
                # print('{} : 1'.format(word))
                current_node.children[word] = Node(1)
            else:
                if current_node.children.get(word):
                    # print('Child already present')
                    current_node.children.get(word).count += 1
                    # print('{} : {}'.format(word, child.count))
                else:
                    # print('Creating child')
                    # print('{} : 1'.format(word))
                    current_node.children[word] = Node(1)
            current_node = current_node.children.get(word)


    def find_last_node(self, words, current_node):
        """
        Returns the last node of the n-gram and None in case the n-gram
        is not preset
        :param self:
        :param words:
        :return:
        """
        # print('In last node')
        # print('Words' + str(words))
        for word in words:
            # for key, value in current_node.children.items():
            #     print('{} : {}'.format(key, value.count))
            child = current_node.children.get(word)
            if not child:
                return None
            current_node = child
        return child

    def build_ngram(self, n, word_list):
        """
        Returns a trie for the ngram. Returns an empty trie (only root present) if the corpus of text
        has less than n words
        :param n:
        :param word_list:
        :return:
        """
        # print('Word list: {}'.format(word_list))
        print('Building {}-grams'.format(n))
        if len(word_list) >= n:
            for i in range(len(word_list)-n+1):
                # print('Word list sliced: {}'.format(word_list[i:i+n]))
                self.add(word_list[i:i+n], self.root)
        print('{}-grams built'.format(n))


    def get_count(self, word_list):
        last_node = self.find_last_node(word_list, self.root)
        if not last_node:
            return 0
        else:
            return last_node.count

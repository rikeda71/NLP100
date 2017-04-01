import re

# 文章を一文ごとに分割する
def separate_sentences(filename='') -> list:
    sentences = []
    with open(filename,'r') as f:
        for line in f.readlines():
            # パターンを保存
            pattern = r'[\.;\?!]\s[A-Z]'
            repatter = re.compile(pattern)
            # 分割
            distance = repatter.finditer(line)
            # 保存
            start = 0
            for sentence in distance:
                sentences.append(line[start:sentence.start()+1].replace('\n',''))
                start = sentence.end()-1
            sentences.append(line[start:].replace('\n',''))
   
    while sentences.count('') > 0:
        sentences.remove('')

    return sentences

# 文章を単語ごとに分割する
def separate_words(sentences)->list:
    words_list = []
    # 一文ごと処理
    for sentence in sentences:
        words = sentence.split(' ')
        words_list.append(words)
    return words_list

if __name__ == '__main__':
    sentences = separate_sentences('nlp.txt')
    words_list = separate_words(sentences)
    for words in words_list:
        for word in words:
            print(word)
        # 文章ごとに改行を入れる
        print('')

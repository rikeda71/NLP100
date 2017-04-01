import re

def separate_sentences(filename=''):
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


if __name__ == '__main__':
    sentences = separate_sentences('nlp.txt')
    for line in sentences:
        print(line)

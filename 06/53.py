import xml
import corenlp
import json
import pprint

if __name__ == '__main__':
    # パーサの生成
    corenlp_dir = "/usr/local/lib/stanford-corenlp-full-2015-04-20/"
    parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

    with open('nlp.txt','r') as f:
        file_sentence = f.read()
    # パースして結果をpretty print
    result_json = json.loads(parser.parse(file_sentence))
    pprint.pprint(result_json)

import pprint
import json
import corenlp

# パーサの生成
corenlp_dir = "/usr/local/lib/stanford-corenlp-full-2015-04-20/"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

# パースして結果をpretty print
result_json = json.loads(parser.parse("I am Alice."))
pprint.pprint(result_json)

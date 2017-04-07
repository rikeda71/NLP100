import xml.etree.ElementTree as ET
import re

# 参照表現のクラス
class Mention:
  def __init__(self, sentence, start, end, head, text):
      self.sentence = int(sentence)
      self.start = int(start)
      self.end = int(end)
      self.head = int(head)
      self.text = text
      

# 参照表現のリストのクラス
# リストのトップが代表参照表現
class Coreference:
    mentions = []
    # リストに参照表現を追加
    def append(self, Mention):
        self.mentions.append(Mention)

# あるファイルのテキストの参照表現を代表参照表現に置き換える
def replace_mention(sentences, coreferences):
    for i in range(len(sentences)):
        rep_dict = make_replace_dict(i, coreferences)
        replace_line(sentences, rep_dict)

# 辞書に沿って1行ごとの置換を行う
def replace_line(sentences, rep_dict) -> str:
    new_sentences = []
    # 参照表現と代表参照表現の結び付け
    for k, v in rep_dict.items():
        #sentences
        print('%s\t:\t%s'%(k,v))
        pass

# 置換を行うための辞書を作成する
def make_replace_dict(num, coreferences) -> dict:
    """
    rep_dict
    { 参照表現 : 代表参照表現 }
    """
    rep_dict = {}
    for i in range(len(coreferences)):
        for j in range(len(coreferences[i].mentions)):
            mention = coreferences[i].mentions[j]
            if mention.sentence == num+1:
                if mention.text in rep_dict: 
                    continue
                if mention.text == coreferences[i].mentions[0].text:
                    #print(mention.text, coreferences[i].mentions[0].text)
                    continue
                rep_dict[mention.text] = coreferences[i].mentions[0].text
    return rep_dict


"""
使い方の例
core_list[0].mentions[0].text
↑のようにして文字列や開始位置などを呼び出す
"""
if __name__ == '__main__':
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()
    core_list = [] # すべての参照表現の関係を保持
    sentences = []
    for parent in root.iterfind('./document/coreference/coreference'): # 間違っている？？ すべてのcoreferenceを一度に取ってきている
        coreference = Coreference()
        # 参照表現の組を格納
        """
        for child in parent.iter('mention'):
            mention = Mention(child[0].text, child[1].text, child[2].text, child[3].text, child[4].text)
            coreference.append(mention)
        """
        # 参照表現の組を格納
        for i in range(len(parent)):
            mention = Mention(parent[i][0].text, parent[i][1].text, parent[i][2].text, parent[i][3].text, parent[i][4].text)
            coreference.append(mention)
        # 参照表現の組を保持
        core_list.append(coreference)
    for parent in root.iterfind('./document/sentences/sentence/tokens'):
        words = []
        for child in parent.iter('token'):
            words.append(child[0].text)
        sentences.append(words)
    
    replace_mention(sentences, core_list)

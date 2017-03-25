#coding:utf-8
class Chunk:
    """
    morphs : Morphオブジェクトのリスト
    dst    : 係り先文節インデックス番号
    srcs   : 係り受け元文節インデックス番号のリスト
    """
    # コンストラクタ
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    # 文字列を返す
    def __str__(self) -> str:
        sentence = ''
        for i in range(len(self.morphs)):
            sentence = sentence + self.morphs[i].surface
        return sentence + '\t係り先:' + str(self.dst)

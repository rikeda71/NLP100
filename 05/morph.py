#coding:utf-8
class Morph:
    surface = '' # 表層系
    base = '' # 基本形
    pos = '' # 品詞
    pos1 = '' # 品詞細分類1

    # コンストラクタ
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    # 表示メソッド
    def show(self) -> None:
        print('表層系:%s 基本形:%s 品詞: %s 品詞細分類: %s'%(self.surface, self.base, self.pos, self.pos1))
    
    # 表層系がある文字列かどうか
    def surface_search(self,line='') -> bool:
        if self.surface == line:
            return True
        return False


NLP100
======
[言語処理100本ノック](http://www.cl.ecei.tohoku.ac.jp/nlp100/)をPythonで解きます

MeCabの設定(chap4)
--------------------------
#### MeCabのインストール

    $ sudo apt-get install libmecab2 libmecab-dev mecab mecab-ipadic mecab-ipadic-utf8 mecab-utils python-mecab
    $ pip install mecab-python3

CaboChaの設定(chap5)
----------------------------
#### CRF++のインストール

「CRF++-0.58.tar.gz」を[こちら](https://drive.google.com/drive/u/0/folders/0B4y35FiV1wh7fngteFhHQUN2Y1B5eUJBNHZUemJYQV9VWlBUb3JlX0xBdWVZTWtSbVBneU0)からDL
    
    # 解凍
    $ tar zxvf CRF++-0.58.tar.gz
    $ cd CRF++-0.58
    # インストール
    $ ./configure
    $ make
    $ sudo make install
    # キャッシュクリア
    $ sudo ldconfig

#### CaboChaのインストール

「cabocha-0.69.tar.bz2」を[こちら](https://drive.google.com/drive/u/0/folders/0B4y35FiV1wh7cGRCUUJHVTNJRnM)からDL

    # 解凍
    $ bzip2 -dc cabocha-0.69.tar.bz2 | tar xvf -
    $ cd cabocha-0.69
    # インストール
    $ ./configure --with-mecab-config='which mecab-config' --with-charset=UTF8
    $ make
    $ make check
    $ sudo make install
    # キャッシュクリア
    $ sudo ldconfig
    # python用のインストール
    $ cd python
    $ python setup.py install


進捗
----
〇2017/03/20 chapter3終了

〇2017/03/18 chapter2終了

〇2017/03/16 chapter1終了

〇2017/03/09 開始

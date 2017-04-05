CaboChaの設定
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

有効グラフ可視化の導入
------------
#### pydotのインストール

    # python3の場合
    pip install pydot_ng

#### graphvizのインストール

    sudo apt-get install graphviz

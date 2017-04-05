MeCabの設定
--------------------------
#### MeCabのインストール

    $ sudo apt-get install libmecab2 libmecab-dev mecab mecab-ipadic mecab-ipadic-utf8 mecab-utils python-mecab
    $ pip install mecab-python3

matplotlibの設定
---------------------------
#### matplotlibのインストール

    $ sudo apt-get install python3-matplotlib python3-gi-cairo python3-tk 
    $ pip install matplotlib

#### python3-cairocffiのインストール

[こちら](https://launchpad.net/ubuntu/xenial/amd64/python3-cairocffi/0.7.2-1)から「python3-cairocffi_0.7.2-1_all.deb」をDLしてインストールする(Ubuntu16.04の場合)

__Tkinter(pythonのGUI操作に必要なもの)を導入しておらず、pyenv上のpythonを使用している場合、Tkinterを導入したいバージョンを1度アンインストールしてからTkinterをインストールする必要がある__ ([参考](http://dragstar.hatenablog.com/entry/2016/09/23/110714))

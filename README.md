# about

LTSV形式のファイルをpandasのデータフレーム形式に変換し、表示およびpandasのクエリ検索を行う。

ログの解析で使えるかなって思ったけどデータフレームに変換するのは重すぎるしメモリ全乗せしちゃうのでシェル芸の有難みがわかった。

# usage

```shell script
$ ./main.py [file path]
$ ./main.py [file path] [pandas query]
```

* `pandas query` is optional

# dependency

* python3
  * if you use python2, fix `from io import StringIO` to `from cStringIO import StringIO`
* pandas
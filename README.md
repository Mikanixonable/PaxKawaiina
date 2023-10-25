# PaxKawaiina
ダウンロードした大量の画像から二次絵/非二次絵を一括でフォルダに分類するツールです。lobe等で作成したtensorflow形式の学習済み画像分類モデルを使います。学習済みの二次絵分類用モデル、乗り物分類用モデルを同梱しています。

## 使い方  
### pythonをインストールし、tensorflowとpillowの入った環境を構築する
- anacondaをダウンロードしインストールする  
- anaconda promptを起動する。
- 仮想環境"PaxKawaiina"を作成する（名前は自由に決めてよい）
~~~shell
conda create -n PaxKawaiina
~~~
- 仮想環境を起動する
~~~shell
conda activate PaxKawaiina
~~~
- tensorflowとpillowをインストールする
~~~shell
conda install tensorflow
~~~
~~~shell
conda install pillow
~~~

## 実行  
- このリポジトリをクローンしたりzipを落として解凍したりしてダウンロードする
- 「パクス・カワイーナ」を分類したい画像があるフォルダにコピペして置く
- PaxKawaiina.batをダブルクリックして起動する 
二次絵は「KawaiiPictures」に入り、非二次絵は「Not2D」に入る。jpg,png以外のファイルは「sonota」に入る。  

## 二次絵以外へのカスタマイズ  
microsoft lobeやその他の手段でモデルを作成しTensorflow形式でエクスポートする。  
エクスポートしたモデルのjsonがあるフォルダにPaxKawaiina.batとPaxKawaiina.pyをコピーすればそのフォルダをパクス・カワイーナフォルダと同じように使える。  

## 使用ライブラリのバージョン情報 
tensorflow: 2.10.0  
pillow: 9.3.0  

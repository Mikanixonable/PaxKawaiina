使い方  

準備  

anacondaをダウンロードしインストールする  
anaconda promptを起動する。  
「conda create -n PaxKawaiina」と入力しエンターキーを押す。  
y or nと聞かれるのでyと打つ  
「conda activate PaxKawaiina」と入力しエンターキーを押す。成功すると(PaxKawaiina)という表示になる。  
y or nと聞かれるのでyと打つ  
「conda install tensorflow」と入力しエンターキーを押す。(PaxKawaiina)という表示が出るまで待つ。  
y or nと聞かれるのでyと打つ  
「conda install pillow」と入力しエンターキーを押す。(PaxKawaiina)という表示が出るまで待つ。  
y or nと聞かれるのでyと打つ  

実行  

「パクス・カワイーナ」をダウンロードして、分類したい画像があるフォルダに置く。  
PaxKawaiina.batをダブルクリックする。  
二次絵は「KawaiiPictures」に入り、非二次絵は「Not2D」に入る。jpg,png以外のファイルは「sonota」に入る。  

二次絵以外へのカスタマイズ  
microsoft lobeやその他の手段でモデルを作成しTensorflow形式でエクスポートする。  
エクスポートしたモデルのjsonがあるフォルダにPaxKawaiina.batとPaxKawaiina.pyをコピーすればそのフォルダをパクス・カワイーナフォルダと同じように使える。  

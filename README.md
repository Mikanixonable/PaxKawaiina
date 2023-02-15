ダウンロードした大量の画像から二次絵/二次絵以外を自動でフォルダに分類するツールです

使い方  

準備  

anacondaをダウンロードしインストールする  
anaconda promptを起動する。  
「conda create -n PaxKawaiina」と入力しエンターキーを押す。  
y or nと聞かれるのでyと打つ  
「conda activate PaxKawaiina」と入力しエンターキーを押す。成功すると(PaxKawaiina)という表示になる。  
「conda install tensorflow」と入力しエンターキーを押す。(PaxKawaiina)という表示が出るまで待つ。  
y or nと聞かれるのでyと打つ  
「conda install pillow」と入力しエンターキーを押す。(PaxKawaiina)という表示が出るまで待つ。  
y or nと聞かれるのでyと打つ  

実行  

「パクス・カワイーナ」のフォルダをダウンロードして、分類したい画像があるフォルダに置く。  
PaxKawaiina.batをダブルクリックする。  
二次絵は「KawaiiPictures」に入り、非二次絵は「Not2D」に入る。jpg,png以外のファイルは「sonota」に入る。  

二次絵以外へのカスタマイズ  
microsoft lobeやその他の手段でモデルを作成しTensorflow形式でエクスポートする。  
エクスポートしたモデルのjsonがあるフォルダにPaxKawaiina.batとPaxKawaiina.pyをコピーすればそのフォルダをパクス・カワイーナフォルダと同じように使える。  


使用ライブラリのバージョン情報 
主要:  
tensorflow: 2.10.0  
pillow: 9.3.0  

全部:
_tflow_select             2.3.0                       mkl 
absl-py                   1.3.0           py310haa95532_0
aiohttp                   3.8.3           py310h2bbff1b_0
aiosignal                 1.2.0              pyhd3eb1b0_0
astunparse                1.6.3                      py_0
async-timeout             4.0.2           py310haa95532_0
attrs                     22.1.0          py310haa95532_0
blas                      1.0                         mkl
blinker                   1.4             py310haa95532_0
brotlipy                  0.7.0           py310h2bbff1b_1002
bzip2                     1.0.8                he774522_0
ca-certificates           2023.01.10           haa95532_0
cachetools                4.2.2              pyhd3eb1b0_0
certifi                   2022.12.7       py310haa95532_0
cffi                      1.15.1          py310h2bbff1b_3
charset-normalizer        2.0.4              pyhd3eb1b0_0
click                     8.0.4           py310haa95532_0
colorama                  0.4.6           py310haa95532_0
cryptography              38.0.4          py310h21b164f_0
fftw                      3.3.9                h2bbff1b_1
flatbuffers               2.0.0                h6c2663c_0
flit-core                 3.6.0              pyhd3eb1b0_0
freetype                  2.12.1               ha860e81_0
frozenlist                1.3.3           py310h2bbff1b_0
gast                      0.4.0              pyhd3eb1b0_0
giflib                    5.2.1                h8cc25b3_1
google-auth               2.6.0              pyhd3eb1b0_0
google-auth-oauthlib      0.4.4              pyhd3eb1b0_0
google-pasta              0.2.0              pyhd3eb1b0_0
grpcio                    1.42.0          py310hc60d5dd_0
h5py                      3.7.0           py310hfc34f40_0
hdf5                      1.10.6               h1756f20_1
icc_rt                    2022.1.0             h6049295_2
icu                       58.2                 ha925a31_3
idna                      3.4             py310haa95532_0
intel-openmp              2021.4.0          haa95532_3556
jpeg                      9e                   h2bbff1b_0
keras                     2.10.0          py310haa95532_0
keras-preprocessing       1.1.2              pyhd3eb1b0_0
lerc                      3.0                  hd77b12b_0
libcurl                   7.87.0               h86230a5_0
libdeflate                1.8                  h2bbff1b_5
libffi                    3.4.2                hd77b12b_6
libpng                    1.6.37               h2a8f88b_0
libprotobuf               3.20.3               h23ce68f_0
libssh2                   1.10.0               hcd4344a_0
libtiff                   4.5.0                h6c2663c_1
libwebp                   1.2.4                h2bbff1b_0
libwebp-base              1.2.4                h2bbff1b_0
lz4-c                     1.9.4                h2bbff1b_0
markdown                  3.4.1           py310haa95532_0
markupsafe                2.1.1           py310h2bbff1b_0
mkl                       2021.4.0           haa95532_640
mkl-service               2.4.0           py310h2bbff1b_0
mkl_fft                   1.3.1           py310ha0764ea_0
mkl_random                1.2.2           py310h4ed8f06_0
multidict                 6.0.2           py310h2bbff1b_0
numpy                     1.23.5          py310h60c9a35_0
numpy-base                1.23.5          py310h04254f7_0
oauthlib                  3.2.1           py310haa95532_0
openssl                   1.1.1s               h2bbff1b_0
opt_einsum                3.3.0              pyhd3eb1b0_1
packaging                 22.0            py310haa95532_0
pillow                    9.3.0           py310hd77b12b_2
pip                       22.3.1          py310haa95532_0
protobuf                  3.20.3          py310hd77b12b_0
pyasn1                    0.4.8              pyhd3eb1b0_0
pyasn1-modules            0.2.8                      py_0
pycparser                 2.21               pyhd3eb1b0_0
pyjwt                     2.4.0           py310haa95532_0
pyopenssl                 22.0.0             pyhd3eb1b0_0
pysocks                   1.7.1           py310haa95532_0
python                    3.10.9               h966fe2a_0
python-flatbuffers        2.0                pyhd3eb1b0_0
requests                  2.28.1          py310haa95532_0
requests-oauthlib         1.3.0                      py_0
rsa                       4.7.2              pyhd3eb1b0_1
scipy                     1.9.3           py310h86744a3_0
setuptools                65.6.3          py310haa95532_0
six                       1.16.0             pyhd3eb1b0_1
snappy                    1.1.9                h6c2663c_0
sqlite                    3.40.1               h2bbff1b_0
tensorboard               2.10.0          py310haa95532_0
tensorboard-data-server   0.6.1           py310haa95532_0
tensorboard-plugin-wit    1.8.1           py310haa95532_0
tensorflow                2.10.0          mkl_py310hd99672f_0
tensorflow-base           2.10.0          mkl_py310h6a7f48e_0
tensorflow-estimator      2.10.0          py310haa95532_0
termcolor                 2.1.0           py310haa95532_0
tk                        8.6.12               h2bbff1b_0
typing_extensions         4.4.0           py310haa95532_0
tzdata                    2022g                h04d1e81_0
urllib3                   1.26.14         py310haa95532_0
vc                        14.2                 h21ff451_1
vs2015_runtime            14.27.29016          h5e58377_2
werkzeug                  2.2.2           py310haa95532_0
wheel                     0.37.1             pyhd3eb1b0_0
win_inet_pton             1.1.0           py310haa95532_0
wincertstore              0.2             py310haa95532_2
wrapt                     1.14.1          py310h2bbff1b_0
xz                        5.2.10               h8cc25b3_1
yarl                      1.8.1           py310h2bbff1b_0
zlib                      1.2.13               h8cc25b3_0
zstd                      1.5.2                h19a0ad4_0

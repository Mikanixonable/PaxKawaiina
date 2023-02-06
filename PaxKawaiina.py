import json
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
import os
import re
import shutil
import glob
import pathlib

# path(str型)を入れると二要素の配列を返す。
#一つ目にはjpgとpngのファイル名一覧の配列が入っている、
#二つ目にはそれ以外のファイルとフォルダ一覧の配列が入っている
def imglist(path):

    patternStr = '.+\.(jpg|png)'
    pattern = re.compile(patternStr)
    listup = []
    unlistup = []
    for item in os.listdir(path):
        result = pattern.match(item)
        # resultがNone以外=画像 なのでパスをリストに追加
        if result:
            listup.append(path + '\\' + item)
        else:
            unlistup.append(path + '\\' + item)
    i = 0
    for item in listup:
        print(str(i) + ' : ' + item)
    for item in unlistup:
        print(str(i) + ' : ' + item)
    return [listup,unlistup]

# signature読込
with open('signature.json', 'r') as f:
    signature = json.load(f)

inputs = signature.get('inputs')
outputs = signature.get('outputs')
classes = signature.get('classes')



# モデルの学習画像サイズを取得
input_width, input_height = inputs['Image']['shape'][1:3]

# model読込
model = tf.saved_model.load('') #ここで時刻がプリントされる
infer = model.signatures['serving_default']

# 画像データ読込

parent = str(pathlib.Path(os.getcwd()).parent)
list = imglist(parent)
imglist = list[0]
unimglist = list[1]

for item in imglist:
    img = item

    #画像を配列に変換
    imgPIL = Image.open(img)
    imgPIL = imgPIL.convert('RGB')
    imgPIL = imgPIL.resize((input_width, input_height))
    x = img_to_array(imgPIL) / 255 #正規化
    x = x[None, ...]


    # 推論
    predict = infer(tf.constant(x))

    label = classes['Label']
    varr = predict['Confidences'][0].numpy()
    value = label[np.argmax(varr)]


    os.makedirs(parent+'/'+str(value), exist_ok=True)
    shutil.copy(img, parent+'/'+str(value))

for path in unimglist:
    if os.path.isfile(path):
        os.makedirs(parent+'/sonota', exist_ok=True)
        shutil.copy(path, parent+'/sonota')

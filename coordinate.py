# モジュール読み込み
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np



#画像の読み込み
im = Image.open("./sources/hata2.png")

#画像をarrayに変換
im_list = np.asarray(im)
#貼り付け
plt.imshow(im_list)
#表示
plt.show()

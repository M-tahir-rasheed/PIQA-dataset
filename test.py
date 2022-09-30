import glob
import numpy as np
import time
import os
import tensorflow as tf
# import tensorflow_addons as tfa
from tensorflow import keras
from tensorflow.keras import layers
from PIL import Image
import pandas as pd
import datetime
np.random.seed(0)


test_dir = './PIQA_dataset/images/'
output_dir = './results/'
loaded = keras.models.load_model("checkpoints/ckpt")


mos_df   = pd.read_csv('./PIQA_dataset/X_test.csv')
mos_np = np.array(mos_df)
nam_dict = {}
for i in mos_np:
    nam_dict[i[0]] = i[1]
    
print(len(nam_dict))

prediction_list = []

for key in nam_dict:
    x = key
    print(key)
    input_img = Image.open(test_dir+key)
    
    img_np = np.asarray(input_img)
    H = img_np.shape[0]

    W = img_np.shape[1]
    xx = np.random.randint(0, W - 256)
    yy = np.random.randint(0, H - 256)
    # siz = gt_rgb_arr.shape
    # gt_nor = (gt_rgb_arr.astype(np.float32))/255
    img = img_np[xx:xx+256,yy:yy+256,:]
    
    test_img = np.expand_dims(np.float32(img / 255.0), axis=0)
    pred_test = loaded.predict(test_img)
    print('file_name =',key, 'MOS = ', pred_test)
    
    prediction_list.append([key,np.squeeze(pred_test)])

data = pd.DataFrame(prediction_list)   
data.to_csv(output_dir+'results.csv',header=True,index=False)


##################################################################################


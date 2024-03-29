# -*- coding: utf-8 -*-
"""prepare_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qv5tNgMGWoioJItfcD3qKTIv6tBKhzYD
"""

# Change this to True to replicate the result
# COMPLETE_RUN = False
COMPLETE_RUN = True

import pandas as pd

train = pd.read_csv("train.csv")

LABELS = list(train.label.unique())
label_idx = {label: i for i, label in enumerate(LABELS)}
train.set_index("fname", inplace=True)
train["label_idx"] = train.label.apply(lambda x: label_idx[x])
if not COMPLETE_RUN:
    train = train[:2000]

# Select a test sample from TRAIN dataset with same number of audio per class

n_samples_per_class=20
test_sample=train.groupby('label')['label_idx'].apply(lambda x: x.sample(n=n_samples_per_class))

# test_sample is a Multilevel panadas Series with the file names in the second level (1)


test_list= list(test_sample.index.get_level_values(1))
test_df=train.loc[train.index.isin(test_list)]

train_df=train.loc[~train.index.isin(test_list)]

import librosa

def divide_data2(data, max_power=0.001):    
    iterations = len(data)   
    maximum=1
    for n in range(iterations):
        power = np.abs(data[n]) # sensitive
        if power > max_power:
            max_power = power
            maximum = n
    
    return maximum

class Config(object): #Python class
    def __init__(self,
                 sampling_rate=8000, audio_duration=2, n_classes=41,
                 use_mfcc=False, n_folds=10, learning_rate= 0.001, 
                 max_epochs=50, n_mfcc=20):
        self.sampling_rate = sampling_rate
        self.audio_duration = audio_duration
        self.n_classes = n_classes
        self.use_mfcc = use_mfcc
        self.n_mfcc = n_mfcc
        self.n_folds = n_folds
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs

        self.audio_length = self.sampling_rate * self.audio_duration
        if self.use_mfcc:
            self.dim = (self.n_mfcc, 1 + int(np.floor(self.audio_length/512)), 1)
        else:
            self.dim = (self.audio_length, 1)

config = Config(sampling_rate=8000, audio_duration=2, n_folds=10, learning_rate= 0.001)
if not COMPLETE_RUN:
    config = Config(sampling_rate=8000, audio_duration=2, n_folds=2, learning_rate= 0.001, max_epochs=1)

#Crear nueva base de datos

import shutil
import os
import numpy as np
import sys

import soundfile as sf

def copy_folder(in_folder,out_folder):
  if not(os.path.isdir(out_folder)):
    shutil.copytree(in_folder, out_folder, ignore=ig_f)

def ig_f(dir, files):
  return [f for f in files if os.path.isfile(os.path.join(dir, f))]

copy_folder('./audio_train8/','./audio_train18/')

input_length = config.audio_length 
for i, fname in enumerate(test_df.index):
        file_path = './audio_train8/' + fname
        data, _ = librosa.core.load(file_path, sr=config.sampling_rate, res_type="kaiser_fast")
        if len(data) > input_length/2:
        # Random offset / Padding
          maximum = divide_data2(data)
          begtotal = int(maximum - input_length/2)
          beg = int(maximum - input_length/4)
          end =int (maximum + input_length/4)
          endtotal =int (maximum + input_length/2)
          if beg> 0 and end <len(data):
            data = data[beg:end]
          else:
            if begtotal> 0:
                data = data[maximum-int(input_length/2):maximum]
            else:
              if endtotal <len(data):
                data = data[maximum:maximum+int(input_length/2)] 
              else:
                data = data[0:int(input_length/2)]
        else: 
          if input_length/2 > len(data):
            data = np.pad(data,(abs(int(input_length/2)-len(data)),0),"constant")   
          else:
            data = np.pad(data,int(input_length/2)-len(data),"constant")

          
        file_out='./audio_train18/' + fname
        sf.write(file_out, data, config.sampling_rate)

input_length = config.audio_length 
for i, fname in enumerate(train_df.index):
        file_path = './audio_train8/' + fname
        data, _ = librosa.core.load(file_path, sr=config.sampling_rate, res_type="kaiser_fast")
        if len(data) > input_length/2:
        # Random offset / Padding
          maximum = divide_data2(data)
          begtotal = int(maximum - input_length/2)
          beg = int(maximum - input_length/4)
          end =int (maximum + input_length/4)
          endtotal =int (maximum + input_length/2)
          if beg> 0 and end <len(data):
            data = data[beg:end]
          else:
            if begtotal> 0:
                data = data[maximum-int(input_length/2):maximum]
            else:
              if endtotal <len(data):
                data = data[maximum:maximum+int(input_length/2)] 
              else:
                data = data[0:int(input_length/2)]
        else: 
          if input_length/2 > len(data):
            data = np.pad(data,(abs(int(input_length/2)-len(data)),0),"constant")   
          else:
            data = np.pad(data,int(input_length/2)-len(data),"constant")

          
        file_out='./audio_train18/' + fname
        sf.write(file_out, data, config.sampling_rate)
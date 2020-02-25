# -*- coding: utf-8 -*-
"""
network
fun:

env:
	Linux ubuntu 4.4.0-31-generic x86_64 GNU;python 2.7;tensorflow1.10.1;Keras2.2.4
	pip2,matplotlib2.2.3
"""
from __future__ import print_function
import os
import numpy as np
import pandas as pd
import keras
import sklearn.datasets.base as bs
from sklearn import preprocessing

class DataSets:
    @staticmethod
    def load_passenger_car(sale_csv_path):
        train_sale_csv = pd.read_csv(sale_csv_path,header=0, index_col=None,
                               names=["province", "adcode", "model", "bodyType", "regYear", "regMonth", "salesVolume"],
                               dtype={"province": np.str, "adcode": np.int, "model": np.str, "regYear": np.int,
                                      "regMonth": np.int, "salesVolume": np.int},
                               encoding="utf-8"#  gb2312 ascii
                               )#
        # model 字符串转换成整形以便于可以排序
        # model 02aab221aabc03b9--0  04e66e578f653ab9--1
        #df['sex'] = df['sex'].map({'female':0,'male':1}).astype(int)
        #sort_csv = train_sale_csv.sort_index(axis=0, ascending=True, by=['adcode', 'model', 'regYear','regMonth'])
        sort_csv = train_sale_csv.sort_values(by=['adcode', 'model', 'regYear','regMonth'], axis=0, ascending=True)
        #sort_csv.to_csv("temp.csv", index=False, header=None)
        data = list()
        target = list()
        predict_data = list()
        adcode = list()
        car_model = list()
        for id in range(1320):
            start = 24*id
            end = start + 24
            sale = sort_csv.iloc[start:end]['salesVolume']
            data_arr = np.asarray(sale.iloc[:12], dtype=np.float32)
            target_arr = np.asarray(sale.iloc[12:16], dtype=np.float32)
            predict_data_arr = np.asarray(sale.iloc[12:24], dtype=np.float32)
            data.append(data_arr)
            target.append(target_arr)
            predict_data.append(predict_data_arr)
            adcode.append(np.asarray(sort_csv.iloc[start:start + 1]['adcode'], dtype=np.str))
            car_model.append(np.asarray(sort_csv.iloc[start:start + 1]['model'], dtype=np.str))
        target_seq = np.array(target)[:,:]
        car_seq = np.array(data)[:,:]
        # 为了追求机器学习和最优化算法的最佳性能，我们将特征缩放
        from sklearn.preprocessing import StandardScaler,MinMaxScaler
        # 1.归一化 MinMaxScaler
        #minmax_scale = MinMaxScaler(feature_range=(0, 1))
        #X_scaled = minmax_scale.fit_transform(X)
        #car_seq = minmax_scale.fit_transform(car_seq)
        #target_seq = minmax_scale.fit_transform(target_seq) # label Y一般没必要做标准化
        # print("X_scaled\n", X_scaled)
        #X_back = minmax_scale.inverse_transform(X_scaled)
        #print("X_back\n", X_back)

        # 2.标准化 StandardScaler
        sc = StandardScaler()
        #X_scaled = sc.fit_transform(X)
        car_seq = sc.fit_transform(car_seq)
        #target_seq = sc.fit_transform(target_seq) # label Y一般没必要做标准化
        # X_back = sc.inverse_transform(X_scaled)
        # print("X_back\n", X_back)

        print("car_seq.shape", car_seq.shape)
        print("target_seq.shape", target_seq.shape)
        predict_data = np.array(predict_data)[:]
        trainX = car_seq[:, :]
        trainY = target_seq[:, :]
        validX = car_seq[::12, :]
        validY = target_seq[::12, :]
        print("trainX.shape",trainX.shape)
        print("trainX[3,:]", trainX[3,:])#每次查看输出数据都是一样的，保证训练输入数据顺序一致
        print("trainY.shape", trainY.shape)
        print("validX.shape", validX.shape)
        print("validY.shape", validY.shape)
        return trainX,trainY,validX,validY



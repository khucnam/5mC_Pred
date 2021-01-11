# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:41:34 2021

@author: Yang
"""

import pickle
#from sklearn.externals import joblib
import sys
import joblib
import os
import math
import numpy as np
from sklearn.metrics import confusion_matrix, roc_auc_score
import pandas as pd

def kmerEmbedding(embeddingFile):
    f=open(embeddingFile,"r")
    lines=f.readlines()
    f.close()
    
    #kmer_Emb is a dictionary of (key, value) where key is the kmer and value is the corresponding kmer embedding
    kmer_Emb={}
    for line in lines[1:]:
        temp=line[:-1].split()
        kmer_Emb[temp[0]]=temp[1:]
    
    return kmer_Emb

def promoterSegToFeature(segFile):
    
    f=open(segFile,"r")
    lines=f.readlines()
    f.close()
    
    kmerEmb=kmerEmbedding("Embedding vectors/Emb.vec")
    
    if not(os.path.exists("tmp")):
        os.mkdir("tmp")
    f=open("tmp/feature.csv","w")
    #k=3
    for line in lines:
        for i in range(len(line)-3):
            tri_mer=line[i]+line[i+1]+line[i+2]
            tri_mer_emb_values=kmerEmb.get(tri_mer)
            for value in tri_mer_emb_values:
                f.write(value+",")
        f.write("\n")
    f.close()
    return lines
    
def predict(threshold, inputFile, outputFile="Result.txt"):
    segs=promoterSegToFeature(inputFile)
    
    #loading the model
    try:
        classifier=joblib.load("Model/model_with_XGBoost.sav")
    except (IOError, pickle.UnpicklingError, AssertionError):
        print(pickle.UnpicklingError)
        return True
    
    #loop through each promoter segment and predict
    ftFile=open("tmp/feature.csv","r")
    lines=ftFile.readlines()
    ftFile.close()
    
    
    f=open(outputFile,"w")
    f.write("No. of promoter segments = "+str(len(lines))+"\n")
    f.write("User threshold: "+str(threshold)+"\n")
    f.write("--------------------------------------------------------------------------\n")
    f.write("Segment                                           Score         Prediction\n")
    f.write("--------------------------------------------------------------------------\n") 
    
    
    
        
    dataset = pd.read_csv("tmp/feature.csv", header=None)
    X_test = dataset.iloc[:,:-1].values
    y_pred = classifier.predict_proba(X_test)
    for seg, predict in zip(segs,y_pred):
        if predict[1]>=threshold:
            f.write("{:42s}".format(seg[:-1])+"    "+"{:10.4f}".format(predict[1])+"        5mC site\n")
        else:
            f.write("{:42s}".format(seg[:-1])+"    "+"{:10.4f}".format(predict[1])+"        Non_5mC site\n")
    

threshold=float(sys.argv[1])
inputFile= sys.argv[2]
outputFile="Result.txt" 
predict(threshold, inputFile, outputFile="Result.txt")  
print("Prediction complete! Please check the results in Result.txt file!")  
from scapy.all import *
import argparse
import pandas as pd 
import statistics
import numpy as np 
import pickle
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import sklearn.neighbors._base
from sklearn.metrics import classification_report, confusion_matrix



def read_pcap(filename):
    packets = rdpcap(filename)
    return packets

P_source = []
P_dest = []
P_len = []
P_dt=[]
P_surcePort = []
P_dt2=[]
direction=[]
inp=[]
out=[]
leng_mean=[]
leng_std=[]
leng_min=[]
leng_max=[]
sum_dt=[]
port=[]
myip=''

my_parser = argparse.ArgumentParser(description='input pcap file')
my_parser.add_argument('-f', '--file', help='The file to read', required=True)
my_parser.add_argument('-i', '--ip', help='The ip to read', required=True)
args = my_parser.parse_args()


# ip_parser=argparse.ArgumentParser(description='input ip address')
# ip_parser.add_argument('-i', '--ip', help='The ip address', required=True)
# ip_args = ip_parser.parse_args()
# myip=ip_args.ip
myip=args.ip
scapy_cap = read_pcap(args.file)


for packets in scapy_cap:
    P_source.append(packets[IP].src)
    P_dest.append(packets[IP].dst)
    P_len.append(packets[IP].len)
    P_dt.append(packets[IP].time)
    P_surcePort.append(packets[TCP].sport)

for i in range(1,len(P_dt)):
    P_dt2.append(P_dt[i]-P_dt[i-1])

dt=pd.DataFrame({'Source':P_source,'Destination':P_dest,'Length':P_len,'DT':P_dt,'Source Port':P_surcePort})
dt.fillna(443,inplace=True)

for i in dt['Destination']:
    if(i==myip):
        direction.append('in')
    else:
        direction.append('out')
dt.insert(0,'direction',direction)
start=0
end=100
inps=0
outs=0
cc=round(dt.shape[0]/100)
tempdf=[]
tempport=[]
tempdt=0
for i in range(cc):
    for k in range(start,end):
        if(dt['direction'][k]=='in'):
            inps=inps+1
        else:
            outs=outs+1
        tempdf.append(dt['Length'][k])
        tempdt=tempdt+dt['DT'][k]
        tempport.append(dt['Source Port'][k])

        
    leng_mean.append(statistics.mean(tempdf))
    leng_std.append(statistics.stdev(tempdf))
    leng_min.append(min(tempdf))
    leng_max.append(max(tempdf))
    sum_dt.append(tempdt)
    port.append(max(tempport,key=tempport.count))
    
    inp.append(inps)
    out.append(outs)
    start=start+100
    end=end+100
    inps=0
    outs=0
    tempdf=[]
    tempport=[]
    tempdt=0

df=pd.DataFrame()

df.insert(0,'inp',inp)
df.insert(1,'out',out)
df.insert(2,'leng_mean',leng_mean)
df.insert(3,'leng_std',leng_std)
df.insert(4,'leng_min',leng_min)
df.insert(5,'leng_max',leng_max)
df.insert(6,'sum_dt',sum_dt)
df.insert(7,'port',port)

filename = 'KNN2.sav' 
X2=df[[ 'inp', 'out', 'leng_mean', 'leng_std', 'leng_min', 'leng_max', 'sum_dt']].values
loaded_model = pickle.load(open(filename, 'rb')) # Load the model 

Result = loaded_model.predict(X2) # Predict the test data
df.insert(8,'Result',Result)

df.to_csv('result.csv')


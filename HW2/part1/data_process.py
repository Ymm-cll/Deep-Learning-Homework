import os
from tqdm import tqdm
path_in='tiny-imagenet-200/val/images/'
path_out='tiny-imagenet-200/val_new/'
path_txt='tiny-imagenet-200/val/val_annotations.txt'

anno_file=open(path_txt,"r",encoding="utf-8")
anno=anno_file.readlines()
names=[]
labels=[]
for i in anno:
    anno_split=i.split("\t")
    names.append(anno_split[0])
    labels.append(anno_split[1])
for label in labels:
    if not os.path.exists(path_out+label):
        os.makedirs(path_out+label)
for i,name in tqdm(enumerate(names)):
    with open(path_in+name, 'rb') as file_in:
        image_data = file_in.read()
    with open(path_out+labels[i]+"/"+name, 'wb') as file_out:
        file_out.write(image_data)


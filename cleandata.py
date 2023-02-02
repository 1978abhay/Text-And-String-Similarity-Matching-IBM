import csv
import json
with open('C:/Users/yupfe/Downloads/crypto_news_dataset.csv (2)/crypto_news_dataset.csv',encoding= 'utf-8', errors= 'ignore') as f:
 csv_reader = csv.reader(f)
 data = str(f.read())


to_array = [char for char in data]
for character in range(len(data)):
    if(to_array[character])=='<':
        while(to_array[character])!='>':
            to_array[character]=''
            character+=1
            if(to_array[character])=='>':
                to_array[character]=''
                break
               
            
string = " ".join(str(x) for x in to_array)
print(string)



        




    
import pandas as pd
import math
from numpy import linspace
import matplotlib.pyplot as plt

#Writen by Mohamed ayman abdelfattah sherrif 
############################################

sheet_reader = pd.read_excel('E:\\Olympic Hockey Teams 2018 - Canada and USA.xlsx'
                  ,sheet_name='PlayerData')
weight_players = sheet_reader['Weight'].tolist()
WP = sorted((weight_players))

Num_class = int(input('Enter number of Classes : '))

if Num_class == 0:
    Num_class = int(math.ceil(math.log(2,len(WP))))

rangs = linspace(119, 240,Num_class+1)
    

count_dict = dict()
count = 0
for fill in WP:
    for i in range(len(rangs)-1):
        k = '%d ==> %d' %(int(rangs[i]+1),int(rangs[i+1]))
        
        if (rangs[i])< fill and fill <= (rangs[i+1]):
            if k in count_dict:
                count_dict[k] = count_dict[k]+1
                
            else:
                count_dict[k] = 1
                
print('''\nfrequency distribution:
Weight of Olympic Hockey Teams 2018 at %d classes\n''' %Num_class)           
        
print('  Weights \t frequency')
for k,v in count_dict.items():
    
    print(k,'\t',v)   

Weights = list(count_dict.keys())
Values  = list(count_dict.values())

plt.bar(range(len(count_dict)),Values,tick_label=Weights) 
plt.show()         
            
            
            
            
            
            
        
        
        
        
        
        
           
                            
                        

        
            
        
            





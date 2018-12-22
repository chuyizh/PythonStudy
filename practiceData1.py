import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
%matplotlib inline
d=pd.read_csv('DataAnalyst.csv',encoding='gb2312')
d_duplicates=d.drop_duplicates(subset='positionId',keep='first')
def cut_word(word,method):
    position=word.find('-')
    length=len(word)
    if position !=-1:
        bottomSalary=word[:position-1]
        topSalary=word[position+1:length-1]
    else:
        bottomSalary=word[:word.upper().find('K')]
        topSalary=bottomSalary
    if method =='bottom':
        return bottomSalary
    else:
        return topSalary
d_duplicates['bottomSalary']= d_duplicates.salary.apply(cut_word,method= 'bottom')
d_duplicates['topSalary']= d_duplicates.salary.apply(cut_word,method= 'top')
d_duplicates.topSalary=d_duplicates.topSalary.astype('int')
d_duplicates.bottomSalary=d_duplicates.bottomSalary.astype('int')
d_duplicates['avgSalary']=d_duplicates.apply(lambda x:(x.bottomSalary+x.topSalary)/2,axis=1)
d_clean=d_duplicates[['city','companyShortName','companySize','education','positionName','positionLables','workYear','avgSalary']]
d_clean.avgSalary.hist()
d_clean.avgSalary.hist(bins=15)

import pandas as pd
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import xlrd

with xlrd.open_workbook('D:/Personal/ML using PYthon/Assignment/Sample - Superstore.xls') as records:
    Data = pd.read_excel(records, index_col=0)
#print(Data.head())


sns.regplot(x='Sales',y='Profit',data=Data,fit_reg=True,order=3)
plt.show()
plt.savefig(fname='Regplot_Profit')
plt.clf()
plt.cla()
plt.close()
sns.jointplot(x='Sales',y='Profit',data=Data)
plt.show()
plt.savefig(fname='JoinPlot')
plt.clf()
plt.cla()
plt.close()
Data.hist(column=['Profit','Sales'], bins=[-100,-50,-20,-10,0,10,20,50,100])
plt.show()
plt.savefig(fname='HistPlot')
plt.clf()
plt.cla()
plt.close()
from scipy.stats import norm
sns.distplot(Data.Sales,rug= True, hist= False,fit=norm)
plt.show()
plt.savefig(fname='DistPlot')
plt.clf()
plt.cla()
plt.close()
sns.boxplot(x=Data.Segment,y=Data.Sales,data=Data)
plt.show()
plt.savefig(fname='BoxPlot')
plt.clf()
plt.cla()
plt.close()
#data1 = Data.sort_values()
#ax = sns.distplot(Data, rug=True, hist=False)

#ax = sns.distplot(x, fit=norm, kde=False)
#print(Data.columns)
#Data.hist(x='Sales',bins=100)
#sns.boxplot(x=Data.Segment,y=Data.Sales,data=Data)
#order = sns.load_dataset("D:/Personal/ML using PYthon/Assignment/Sample - Superstore'")
#print(order.head())z
#ab = excel_input["segment"]
#print(ax)
#ax=sns.boxplot(x=excel_input['segment'], y=excel_input['sales'], data=excel_input)
#plt.show()
#plt.savefig(fname='distplot_Sales')
#sns.distplot(Data.Profit,rug= True, hist= False,fit=norm)
#sns.distplot(Data.Sales,rug= True, hist= False,fit=

#plt.show()

#plt.savefig(fname='distplot_Profit')
from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pandas as pd
import pylab as p

#download daily data from Yahoo!Finance starting from 1 Jan 2011 until 20 July 2015
start = dt(2011, 1, 1)
end = dt(2015, 7, 20)

#Digi.com(code: 6947) is chosen
DIGI_close = DR("6947.KL", 'yahoo', start, end)['Close'] 

#5-day moving average of Digi.com stock prices
ave = 5
mov_ave = pd.rolling_mean(DIGI_close,ave) 

#5-day moving average plot for the downloaded data
p.plot(mov_ave)
p.xlabel('Day')
p.ylabel('5-day Moving Average')
p.title('5-day Moving Average Plot of Digi.com \n [1 Jan 2011 - 20 July 2015] ' )
p.show()

#download and combine FTSEKLCI daily data for the same duration
combine=['6947.KL','^KLSE']
closing = DR(combine, 'yahoo', start, end)['Adj Close']

#compute correlation of Digi.com with FTSEKLC
correlation = closing.corr()
print('Correlation between Digi.com and FTSEKLCI:  \n' + str(correlation)) 
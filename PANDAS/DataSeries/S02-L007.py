import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

nameList = ['Albania', 'Austria', 'Belarus', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia',
            'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy',
            'Latvia', 'Lithuania', 'Luxembourg', 'Macedonia', 'Malta', 'Montenegro', 'Netherlands',
            'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
            'United', 'Kingdom', 'Turkey', 'Ukraine']

energy2010List = [1947, 8347, 3564, 8369, 4560, 3814, 4623, 6348, 6328, 6506, 16483, 7736, 7264, 5318, 3876,
                  51440, 5911, 5494, 3230, 3471, 16830, 3521, 4171, 5420, 7010, 24891, 3797, 4959, 2551,
                  6410, 4359, 6521, 5707, 14934, 8175, 2498, 3550, 5701]

energy2012List = [2118, 8507, 3698, 7987, 4762, 3819, 4057, 6305, 6039, 6689, 15687, 7344, 7270, 5511, 3919,
                  53203, 5665, 5398, 3588, 3608, 14696, 3626, 4761, 5416, 6871, 23658, 3899, 4736, 2604,
                  6617, 4387, 6778, 5573, 14290, 7886, 2794, 3641, 5452]

nameSeries = pd.Series(nameList)
energy2010Series = pd.Series(energy2010List)
energy2012Series = pd.Series(energy2012List)

mean2010 = energy2010Series.mean()
print(mean2010)
mean2012 = energy2012Series.mean()
print(mean2012)
filterAboveMean2010 = energy2010Series > mean2010
filterAboveMean2012 = energy2010Series > mean2012

print(nameSeries.where(filterAboveMean2010 & filterAboveMean2012).dropna())
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

ix = ["do 6", "7-14", "15-17", "18-24", "25-39", "40-59", "60 i więcej"]
val = [14, 334, 312, 5823, 9491, 7486, 4343]
incidents = pd.Series(data=val, index=ix)

print(incidents.where(incidents > 1000))
print(incidents.where(incidents > 1000).dropna())

incident1000 = incidents.where(incidents > 1000).dropna()
print(incident1000)
print(incidents)

print(incidents.filter(items=["18-24", "25-39", "40-59"]))

incidents.where(incidents <= 1000, inplace=True)
incidents.dropna(inplace=True)
print(incidents)
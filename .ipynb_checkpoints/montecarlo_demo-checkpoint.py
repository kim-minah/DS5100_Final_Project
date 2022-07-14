from montecarlo import Die,Game,Analyzer
import numpy as np

die = Die(np.array([1,2,3,4,5,6]))
die.change_weight(1,5)
print(die.show())
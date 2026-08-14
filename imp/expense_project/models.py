from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction:
    amount : float
    category : str 
    date : str = str(datetime.now()) #json can't parse datetime as it is so into string

# t1= Transaction ( 2000, "Robox")
# print(t1.amount)
# print(t1.category)
# print(t1.date)
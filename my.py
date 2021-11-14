import statistics
import random
import pandas as pd
import csv

def mode():
    list = []
    for i in range(0,100):
        x = random.randint(0,100)
        list.append(x)
        mean = statistics.mean(list)
    return mean

mode()

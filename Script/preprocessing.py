import numpy as np
import pandas as pd

import traceback
import datetime
import re


def find_chunk(df, col_name):
    all_words = []
    for a,b in df.col_name.iteritems():
        x = b.split(' ')
        all_words.extend(x)


    # non ascii characters 
    print("Non ascii characters in the names: ")
    unusual_chars = set()
    for x in all_words:
        res = re.sub('[0-9a-zA-Z()]+', '', x)
        if len(res)>0:
            unusual_chars.add(res) 
    print(unusual_chars + "\n")      

    # Print chunk words with times
    res = pd.DataFrame()
    for x in unusual_chars:
        if len(x)>0:
            res = df[df.col_name.str.contains(re.escape(str(x)))]
            print (x,' found ', len(res), ' times')
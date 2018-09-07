import pandas as pd
from datetime import datetime

class data_logs():

    def __init__(self, cid,cph,off,crt,cr,rep):
        self.cid= cid
        self.cph = cph
        self.off = off
        self.crt = crt
        self.cr = cr
        self.rep = rep

    def add_data(self):
        data = {'Customer ID':[self.cid],
            'Customer Phone': [self.cph],
            'Offer': [self.off] ,
            'Customer Response Time': [self.crt],
            'Customer Response': [self.cr],
            'Reply': [self.rep]}
        
        new_df = pd.DataFrame(data, columns = ['Customer ID', 'Customer Phone', 'Offer', 'Customer Response Time', 'Customer Response', 'Reply'])
        self.logs_df = self.logs_df.append(new_df)
        # print(self.logs_df)
        return self.logs_df.to_csv('RM_LOGS.csv')

    def write_logs(self):
        f = open('rm_logs.txt', 'a+')
        logs = '\n123456,+185698765,car loan,5-10-2018,yes,good'
        for i in range(1):
            f.write(logs)

        f.close()
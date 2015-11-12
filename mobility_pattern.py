# -*- coding:UTF-8 -*-
#####################################################################################################
### this program allows you to define and identify human's mobility pattern and inhalation rate#####
#####################################################################################################


__author__ = 'wgx'
import psycopg2
from gps_dump_home import gps_dump
from sklearn import cluster


class activity(gps_dump):

    def __init__(self):
        gps_dump.__init__()


    def find_home(self):
        self.num_uid()
        for i in range(0,self.num_users,1):
            try:
                self.cur.execute("SELECT * FROM geolife.gps_points WHERE uid= {0} "
                                 "and hour_day>'02:00:00' and hour_day<'04:00:00' "
                                 "and day_week>=0 and day_week<=4".format(self.list_uid[i]))
                rows = self.cur.fetchall()


            except Exception as err:
                print "------>something wrong happened during inferring home cluster"
                print err.message




if __name__ =="__main__":
    pass
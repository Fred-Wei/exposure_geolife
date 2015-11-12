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
        gps_dump.__init__(self)
        gps_dump.conn()
        self.nop = 0
        self.nou=1 # for now the # of users is only 1

    def calc_nop(self):#determine the #mini for cluster of NBSC algorithm
        self.cur.execute(r'select count(*) from geolife.gps_points where uid=0 and day_week<5')
        rows = self.cur.fetchall()
        if self.nop == 0:
            self.nop = rows

    def find_home(self):
        for i in range(0,self.nou,1):
            try:
                self.cur.execute("SELECT * FROM geolife.gps_points WHERE uid= {0} "
                                 "and hour_day>'02:00:00' and hour_day<'04:00:00' "
                                 "and day_week>=0 and day_week<=4".format(self.list_uid[i]))
                rows = self.cur.fetchall()


            except Exception as err:
                print "------>something wrong happened during inferring home cluster"
                print err.message


if __name__ =="__main__":

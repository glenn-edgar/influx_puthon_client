#
# File: influx_client.py
# Demo file for accessing lacima Ranch
#
#
#
#


import sys

from influxdb import InfluxDBClient

class Influx_Client( object ):
 
   def __init__( self, user_name, password ):
       self.client = InfluxDBClient( "lacimaRanch.cloudapp.net", 8086, user_name, password,"moisture_data", ssl = True, verify_ssl = False )
       #print self.client.get_list_database()
   
   def query( self, query_string ):
       return self.client.query( query_string )


if __name__ == "__main__":

   user_name = sys.argv[1] 
   password  = sys.argv[2]

   influx_client = Influx_Client( user_name, password )
   # print out tags

   # print out fields


   print influx_client.query( "select * from moisture_a ")

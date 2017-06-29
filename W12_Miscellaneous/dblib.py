#!/usr/bin/env python
"""
## install related
sudo apt-get install python-psycopg2 python-sqlalchemy
sudo pip install sqlalchemy_schemadisplay

## ensure there is a user and db ready if you run this script
sudo su - postgres
psql -U postgres
CREATE USER ender WITH ENCRYPTED PASSWORD 'bugger';
\q

create a database
----------------------
sudo su - postgres
psql -U postgres
CREATE DATABASE foo WITH OWNER ender;
\q

## if you run into privalages issue
sudo su - postgres
psql -U postgres
\c readychef
GRANT ALL PRIVILEGES ON TABLE visits,meals,events,referrals,users to ENDER;
"""


import sys,os,csv,re
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session,relationship
from sqlalchemy import MetaData,Table,Column,Sequence,ForeignKey, Integer, String
from sqlalchemy.inspection import inspect
from sqlalchemy.sql import select
from sqlalchemy.ext.declarative import declarative_base

try:
    from sqlalchemy_schemadisplay import create_schema_graph
    createGraph = True
except:
    createGraph = False

class DbWrapper(object):
    """
    interface with a generic database
    """

    def __init__(self,uname,upass,dbname,dbhost='localhost',port='5432',reflect=False):
        """
        Constructor

        uname - database username
        upass - database password
        dbname - database name
        dbhost - database host address
        port - database port
        """

        ## db variables
        self.uname = uname
        self.upass = upass
        self.dbname = dbname
        self.dbhost = dbhost
        self.port = port

        ## initialize
        self.connect()

    def connect(self):
        ## basic connection
        self.Base = automap_base()    
        self.engine = create_engine('postgresql://%s:%s@%s:%s/%s'%(self.uname,self.upass,self.dbhost,self.port,self.dbname))
        self.conn = self.engine.connect()
        self.session = Session(self.engine)
        self.meta = MetaData()
        self.tables = {}
        
        ## reflect the tables 
        self.meta.reflect(bind=self.engine)
        for tname in self.engine.table_names():
            tbl = Table(tname,self.meta,autoload=True,autoload_with=self.engine)
            self.tables[tname] = tbl
            
    def print_summary(self):
        """
        print a list of the tables
        """

        print("-----------------------")
        print("%s"%(self.dbname))
        print("%s tables"%len(self.tables.keys()))
        
        for tname,tbl in self.tables.iteritems():
            print("\t %s"%(tname)) 
            print("\t\tPK: %s "%";".join([key.name for key in inspect(tbl).primary_key]))
            for col in tbl.columns:
                print("\t\t%s"%col)

    def draw_schema(self,filename="schema.png"):
        
        if createGraph:
            # create the pydot graph object by autoloading all tables via a bound metadata object
            graph = create_schema_graph(metadata=self.meta,
                                        show_datatypes=False,   # can get large with datatypes
                                        show_indexes=False,     # ditto for indexes
                                        rankdir='LRA',           # From left to right (LR), top to bottom (TB)
                                        concentrate=False       # Don't try to join the relation lines together
            )

            if re.search("\.png",filename):
                graph.write_png(filename)
            elif re.search("\.svg",filename):
                graph.write_svg(filename)
            else:
                raise Exception("invalid filename specified [*.png or *.svg")
        
            print("...%s created"%filename)
        else:
            print "Not creating schema figure because 'sqlalchemy_schemadisplay' is not installed"
        
        
if __name__ == "__main__":
    print "Running..."
    
    ## basic connect for existing db
    db = DbWrapper('ender','bugger','foo')
    db.print_summary()
    db.draw_schema()

    ## sqlalchemy ORM queries
    Member = db.tables['member']
    all_members = db.session.query(Member).all()
    specific_rows = db.session.query(Member).filter_by(name="pipin").all()

    print all_members
    print specific_rows
    
    ## sqlalchemy core queries
    s = select([Member])
    _result = db.conn.execute(s)
    result = _result.fetchall()
    print str(s)
    print result[0]
   
    print("have fun!")

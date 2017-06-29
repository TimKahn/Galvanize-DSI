import os,sys,getpass,datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    signup_store = Column(String(250))

class Purchase(Base):
    __tablename__ = 'purchase'
    id = Column(Integer, primary_key=True)
    item_number = Column(Integer, nullable=False)
    item_category = Column(String(250), nullable=False)
    item_name = Column(String(250), nullable=False)
    item_amount = Column(Float, nullable=False)
    purchace_date = Column(DateTime,default=datetime.datetime.utcnow)
    member_id = Column(Integer, ForeignKey('member.id'))
    member = relationship(Member)        
        
class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True)
    game_name = Column(String(250))
    game_type = Column(String(250))
    game_maker = Column(String(250), nullable=False)
    game_date = Column(DateTime, default=datetime.datetime.utcnow)
    member_id = Column(Integer, ForeignKey('member.id'))
    member = relationship(Member)        

## Create an engine
uname = 'ender'
upass = getpass.getpass()
dbname = 'foo'
dbhost = 'localhost'
port = '5432'
engine = create_engine('postgresql://%s:%s@%s:%s/%s'%(uname,upass,dbhost,port,dbname))

## erase the taples if they exist (CAREFUL the drop_all!!!)
Base.metadata.reflect(bind=engine)
Base.metadata.drop_all(engine)

## Create all tables in the engine. This is equivalent to "Create Table"
Base.metadata.create_all(engine)

## create a session (staging zone)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

## add some members
new_member_1 = Member(name='pipin',address='west shire',signup_store='prancing pony')
new_member_2 = Member(name='peregrin',address='south shire',signup_store='prancing pony')

session.add(new_member_1)
session.add(new_member_2)
session.commit()

## add some purchases
new_purchase = Purchase(item_number=1234,
                        item_category='role playing',
                        item_name='playing mat',
                        item_amount = 10.45,
                        purchace_date = datetime.datetime.utcnow,                        
                        member_id = new_member_1.id
)

session.commit()

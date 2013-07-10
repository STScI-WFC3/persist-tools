import os
import yaml

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def loadConnection(connection_string, echo=False):
    '''
    Create and engine using an engine string. Declare a base and 
    metadata. Load the session and return a session object.
    '''
    engine = create_engine(connection_string, echo=echo)
    Base = declarative_base(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, Base


def get_configuration_data():
    '''
    Returns a dictionary of the configuration settings from a text 
    file called 'configuration.txt' in the same directory as this 
    module.
    '''
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
        'config.yaml')
    with open(filename, 'r') as f:
        data = yaml.load(f)
    return data

config = get_configuration_data()
session, Base = loadConnection(config['database_string'], config['echo'])


class Master(Base):
    '''
    The Mapped class for the master table.
    '''
    __tablename__ = 'master'
    __table_args__ = {'autoload':True}


class IR_FLT_0(Base):
    '''
    The mapped class for the ir_flt_0 table.
    '''
    __tablename__ = 'ir_flt_0'
    __table_args__ = {'autoload':True}

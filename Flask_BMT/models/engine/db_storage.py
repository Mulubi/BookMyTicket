''' contains the DBStorage class '''

from ..base_model import BaseModel, Base
from ..patients import Patient
from ..procedures import Procedure
from ..surgeons import Surgeon
from ..theatres import Theatre
from ..users import User
from ..anaesthetists import Anaesthetist
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {"Patient": Patient, "Procedure": Procedure,
           "Surgeon": Surgeon, "Theatre": Theatre,
           "User": User, "Anaesthetist": Anaesthetist}


class DBStorage:
    """ This represents the storage class that interacts with MySQL Database. """
    __engine = None
    __session = None

    def __init__(self):
        ''' Initializes the DBStorage object '''
        #BMT_MYSQL_USER = getenv("BMT_MYSQL_USER")
        #BMT_MYSQL_PWD = getenv("BMT_MYSQL_PWD")
        #BMT_MYSQL_HOST = getenv("BMT_MYSQL_HOST")
        #BMT_MYSQL_DB = getenv("BMT_MYSQL_DB")
        #BMT_ENV = getenv("BMT_ENV")
        #self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                     #format(BMT_MYSQL_USER,
                                             #BMT_MYSQL_PWD,
                                             #BMT_MYSQL_HOST,
                                             #BMT_MYSQL_DB))
        self.__engine = create_engine("sqlite:///site.db")
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
                    return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""    
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return

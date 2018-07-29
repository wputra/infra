from sqlalchemy import Column, DateTime, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id        = Column(Integer(int64), primary_key=True)
    username  = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(20))
    lastname  = Column(String(20))
    email     = Column(String(100), nullable=False, unique=True)
    password  = Column(String(50), nullable=False)

    def update(self, id=None, username=None, firstname=None, lastname=None, email=None, password=None):
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password

class ApiResponse(Base):
    __tablename__ = 'api_response'
    code    = Column(Integer(int32))
    message = Column(String(100))



def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=True, autoflush=False, bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
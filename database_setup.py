from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True)
  name = Column(String(250), nullable=False)
  email = Column(String(250), nullable=False)
  picture = Column(String(250))

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    image_url = Column(String(500), nullable=False)
    embed_youtube_url = Column(String(500), nullable=False)
    personal_score = Column(Integer, nullable=False)
    short_description = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'title'                     : self.title,
           'id'                        : self.id,
           'image_url'                 : self.image_url,
           'embed_youtube_url'         : self.embed_youtube_url,
           'personal_score'            : self.personal_score,
           'short_description'         : self.short_description
       }

# class MenuItem(Base):
#     __tablename__ = 'menu_item'


#     name =Column(String(80), nullable = False)
#     id = Column(Integer, primary_key = True)
#     description = Column(String(250))
#     price = Column(String(8))
#     course = Column(String(250))
#     restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
#     restaurant = relationship(Restaurant)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship(User)

#     @property
#     def serialize(self):
#        """Return object data in easily serializeable format"""
#        return {
#            'name'         : self.name,
#            'description'         : self.description,
#            'id'         : self.id,
#            'price'         : self.price,
#            'course'         : self.course,
#        }



engine = create_engine('sqlite:///media.db')


Base.metadata.create_all(engine)

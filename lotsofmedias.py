from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Media, Base, User

engine = create_engine('sqlite:///media.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# media = Media(title = "",
#                     image_url="",
#                     embed_youtube_url="",
#                     personal_score="",
#                     short_review ="")

# Menu for UrbanBurger
media1 = Media(title="Mad Max",
               image_url="https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
               embed_youtube_url='<iframe width="560" height="315" src="https://www.youtube.com/embed/b_4nzm9ICuo" frameborder="0" allowfullscreen></iframe>',
               personal_score=100,
               short_description="Non Stop Car Chase in Post Apocalyptic World.",
               user_id=1)

session.add(media1)
session.commit()


print "added medias!"

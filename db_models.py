from sqlalchemy import Column, Integer, String, Date, DateTime, Float, Boolean
from db_connection import Base, engine


class Calendar(Base):
    __tablename__ = 'calendar'

    date = Column(Date, primary_key=True)
    day = Column(Integer)
    month_number = Column(Integer)
    year = Column(Integer)

    def __repr__(self):
        return f'<Calendar {self.date}>'


class Game(Base):
    __tablename__ = 'game'

    game_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'<Game {self.game_id} {self.name} >'


class Player(Base):
    __tablename__ = 'player'

    current_count_owned_games = Column(Integer)
    current_count_reviews = Column(Integer)
    datetime_load = Column(DateTime)
    page_url = Column(String)
    player_code_store = Column(String)
    player_id = Column(Integer, primary_key=True)
    store_id = Column(String(10))

    def __repr__(self):
        return f'<Player {self.player_id} {self.page_url} >'


class Review(Base):
    __tablename__ = 'review'

    content = Column(String)
    date_posted = Column(Date)
    game_id = Column(Integer)
    hours_in_game = Column(Float)
    player_id = Column(Integer)
    review_code = Column(Integer)
    review_id = Column(Integer, primary_key=True)
    review_type_id = Column(Boolean)
    store_id = Column(String(10))
    page_url = Column(String)

    def __repr__(self):
        return f'<Review {self.review_id} {self.page_url}>'


class Review_type(Base):
    __tablename__ = 'review_type'

    name = Column(String(10))
    review_type_id = Column(Boolean, primary_key=True)

    def __repr__(self):
        return f'<Review_type {self.review_type_id} {self.name}>'


class Store(Base):
    __tablename__ = 'store'

    name = Column(String)
    store_id = Column(String, primary_key=True)

    def __repr__(self):
        return f'<Store {self.store_id} {self.name}>'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

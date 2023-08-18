from model import Agentura, Skelbimas, sessionmaker, engine

Session = sessionmaker(bind=engine)
session = Session()


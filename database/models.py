from sqlalchemy import Column, Integer, String, Boolean
from database import Base
from datetime import datetime
import pytz
tashkent_tz = pytz.timezone("Asia/Tashkent")

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer, nullable=True)
    title = Column(String)
    text = Column(String)
    # в photo хранится путь к фотографии /./photo/<name>.jpeg
    photo = Column(String, nullable=True)
    reg_date = Column(String, default=lambda: datetime.now(tashkent_tz))

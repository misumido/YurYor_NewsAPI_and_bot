from database import get_db
from database.models import News

def add_news_db(title: str, text: str,
             photo: str | None = None) -> int:
    with next(get_db()) as db:
        news = News(title=title,
                    text=text,
                    photo=photo)
        db.add(news)
        db.commit()
        db.refresh(news)
        return news.id
def publish_news_db(id: int, message_id: int)-> bool:
    with next(get_db()) as db:
        news = db.query(News).filter_by(id=id).first()
        if news:
            news.message_id = message_id
            db.commit()
            return True
        return False
def delete_news_db(message_id: int) -> bool:
    with next(get_db()) as db:
        news = db.query(News).filter_by(message_id=message_id).first()
        if news:
            db.delete(news)
            db.commit()
            return True
        return False

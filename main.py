from fastapi import FastAPI, Depends, HTTPException, Query, status, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from typing import List
from sqlalchemy.orm import Session
import os
from configs import API_SECRET_KEY, PHOTO_DIR
from database.models import News
from database import engine, Base, get_db
from schemas import NewsResponse

Base.metadata.create_all(bind=engine)
app = FastAPI(title="YurYor News API", description="API для работы с опубликованными новостями",
              docs_url="/")

API_TOKEN = API_SECRET_KEY


def verify_token(api_token: str = Header(..., description="API токен для авторизации")):
    if api_token != API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный API токен"
        )
    return api_token

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # заменить на список разрешенных доменов
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/news", response_model=List[NewsResponse], tags=["News"])
def get_all_news(
        skip: int = Query(0, description="Количество пропускаемых записей"),
        limit: int = Query(100, description="Максимальное количество возвращаемых записей"),
        db: Session = Depends(get_db),
        token: str = Depends(verify_token)
):
    """
    Получить все опубликованные новости.
    """
    news = db.query(News).filter(News.message_id.isnot(None)).offset(skip).limit(limit).all()
    return news


@app.get("/api/news/photo/{news_id}", tags=["News"])
def get_news_photo(news_id: int, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    """
    Получить фотографию новости по ID новости.
    """
    news = db.query(News).filter(News.id == news_id, News.message_id.isnot(None)).first()
    if news is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Новость не найдена")

    if not news.photo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="У новости нет фотографии")
    photo_name = news.photo
    photo_path = os.path.join(PHOTO_DIR, photo_name)
    if not os.path.exists(photo_path):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Файл изображения не найден")
    filename = os.path.basename(photo_path)
    if filename.lower().endswith('.jpeg') or filename.lower().endswith('.jpg'):
        media_type = 'image/jpeg'
    elif filename.lower().endswith('.png'):
        media_type = 'image/png'
    else:
        media_type = 'application/octet-stream'

    return FileResponse(
        path=photo_path,
        media_type=media_type,
        filename=filename
    )


@app.get("/api/news/{news_id}", response_model=NewsResponse, tags=["News"])
def get_news_by_id(news_id: int, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    """
    Получить опубликованную новость по ID.
    """
    news = db.query(News).filter(News.id == news_id, News.message_id.isnot(None)).first()
    if news is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Новость не найдена")
    return news


@app.get("/api/news/message/{message_id}", response_model=NewsResponse, tags=["News"])
def get_news_by_message_id(message_id: int, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    """
    Получить новость по message_id.
    """
    news = db.query(News).filter(News.message_id == message_id).first()
    if news is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Новость не найдена")
    return news


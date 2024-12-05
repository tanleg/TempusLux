from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import get_db, Base, engine
from models import Watch
from pydantic import BaseModel

app = FastAPI()

# Modèles Pydantic pour validation
class WatchBase(BaseModel):
    name: str
    brand_id: int
    category_id: int
    price: float
    description: str
    image_url: str

class WatchCreate(WatchBase):
    pass

class WatchResponse(WatchBase):
    id: int

    class Config:
        orm_mode = True

# Initialisation de la base de données
Base.metadata.create_all(bind=engine)

@app.get("/watches", response_model=list[WatchResponse])
def get_watches(db: Session = Depends(get_db)):
    try:
        watches = db.query(Watch).all()
        return watches
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/watches/{watch_id}", response_model=WatchResponse)
def get_watch(watch_id: int, db: Session = Depends(get_db)):
    watch = db.query(Watch).filter(Watch.id == watch_id).first()
    if not watch:
        raise HTTPException(status_code=404, detail="Watch not found")
    return watch


@app.post("/watches", response_model=WatchResponse)
def create_watch(watch: WatchCreate, db: Session = Depends(get_db)):
    new_watch = Watch(**watch.dict())
    db.add(new_watch)
    db.commit()
    db.refresh(new_watch)
    return new_watch

@app.put("/watches/{watch_id}", response_model=WatchResponse)
def update_watch(watch_id: int, watch: WatchCreate, db: Session = Depends(get_db)):
    db_watch = db.query(Watch).filter(Watch.id == watch_id).first()
    if not db_watch:
        raise HTTPException(status_code=404, detail="Watch not found")
    for key, value in watch.dict().items():
        setattr(db_watch, key, value)
    db.commit()
    db.refresh(db_watch)
    return db_watch

@app.delete("/watches/{watch_id}")
def delete_watch(watch_id: int, db: Session = Depends(get_db)):
    db_watch = db.query(Watch).filter(Watch.id == watch_id).first()
    if not db_watch:
        raise HTTPException(status_code=404, detail="Watch not found")
    db.delete(db_watch)
    db.commit()
    return {"detail": "Watch deleted"}

@app.exception_handler(404)
def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "Resource not found"}
    )


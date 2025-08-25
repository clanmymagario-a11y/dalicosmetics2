from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud
from .database import SessionLocal, engine, Base

# Crear tablas en la BD si no existen
Base.metadata.create_all(bind=engine)

# Inicializar FastAPI
app = FastAPI(title="API de Productos", version="1.0")

# Dependencia para obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =====================
# 📦 ENDPOINTS PRODUCTOS
# =====================

@app.post("/productos", response_model=schemas.ProductoOut)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.create_producto(db=db, producto=producto)


@app.get("/productos", response_model=List[schemas.ProductoOut])
def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_productos(db=db, skip=skip, limit=limit)


@app.get("/productos/{producto_id}", response_model=schemas.ProductoOut)
def read_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.get_producto(db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto


@app.put("/productos/{producto_id}", response_model=schemas.ProductoOut)
def update_producto(producto_id: int, producto: schemas.ProductoUpdate, db: Session = Depends(get_db)):
    db_producto = crud.update_producto(db, producto_id=producto_id, update_data=producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto


@app.delete("/productos/{producto_id}", response_model=schemas.ProductoOut)
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.delete_producto(db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto
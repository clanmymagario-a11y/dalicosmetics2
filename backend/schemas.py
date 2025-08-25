from pydantic import BaseModel
from typing import List, Optional


# =====================
# 📦 SCHEMAS PRODUCTO
# =====================

# Base compartida
class ProductoBase(BaseModel):
    nombre: str
    categoria: str
    precioDetal: float
    precioMayor: float
    costo: float
    imagenes: List[str] = []  # lista de URLs o nombres de archivo
    descripcion: Optional[str] = None
    estado: Optional[str] = "disponible"


# Crear producto
class ProductoCreate(ProductoBase):
    pass


# Actualizar producto
class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    categoria: Optional[str] = None
    precioDetal: Optional[float] = None
    precioMayor: Optional[float] = None
    costo: Optional[float] = None
    imagenes: Optional[List[str]] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None


# Respuesta con ID
class ProductoOut(ProductoBase):
    id: int

    class Config:
        from_attributes = True  # reemplazo de orm_mode en Pydantic v2
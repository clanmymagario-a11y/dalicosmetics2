from sqlalchemy.orm import Session
from . import models, schemas

# =====================
# 📦 PRODUCTOS
# =====================

# Crear producto
def create_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.Producto(
        nombre=producto.nombre,
        categoria=producto.categoria,
        precioDetal=producto.precioDetal,
        precioMayor=producto.precioMayor,
        costo=producto.costo,
        imagenes=",".join(producto.imagenes),  # Guardamos lista como string
        descripcion=producto.descripcion,
        estado=producto.estado
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto


# Obtener todos los productos
def get_productos(db: Session, skip: int = 0, limit: int = 100):
    productos = db.query(models.Producto).offset(skip).limit(limit).all()
    for p in productos:
        p.imagenes = p.imagenes.split(",") if p.imagenes else []
    return productos


# Obtener un producto por ID
def get_producto(db: Session, producto_id: int):
    producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if producto:
        producto.imagenes = producto.imagenes.split(",") if producto.imagenes else []
    return producto


# Actualizar producto
def update_producto(db: Session, producto_id: int, update_data: schemas.ProductoUpdate):
    producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if not producto:
        return None

    if update_data.nombre is not None:
        producto.nombre = update_data.nombre
    if update_data.categoria is not None:
        producto.categoria = update_data.categoria
    if update_data.precioDetal is not None:
        producto.precioDetal = update_data.precioDetal
    if update_data.precioMayor is not None:
        producto.precioMayor = update_data.precioMayor
    if update_data.costo is not None:
        producto.costo = update_data.costo
    if update_data.imagenes is not None:
        producto.imagenes = ",".join(update_data.imagenes)
    if update_data.descripcion is not None:
        producto.descripcion = update_data.descripcion
    if update_data.estado is not None:
        producto.estado = update_data.estado

    db.commit()
    db.refresh(producto)
    producto.imagenes = producto.imagenes.split(",") if producto.imagenes else []
    return producto


# Eliminar producto
def delete_producto(db: Session, producto_id: int):
    producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if not producto:
        return None
    db.delete(producto)
    db.commit()
    return producto
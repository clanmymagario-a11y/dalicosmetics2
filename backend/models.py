from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.types import TypeDecorator
import json
from .database import Base

# Custom type para guardar listas como JSON en un campo TEXT
class JSONEncodedList(TypeDecorator):
    impl = Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return "[]"
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return []
        return json.loads(value)

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    categoria = Column(String)
    precioDetal = Column(Float)
    precioMayor = Column(Float)
    costo = Column(Float)
    imagenes = Column(JSONEncodedList)  # 👈 ahora soporta arrays
    descripcion = Column(String, nullable=True)
    estado = Column(String, default="disponible")
from sqlalchemy import String, Float, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="dpg-d840hi7aqgkc73a7fo70-a.oregon-postgres.render.com",
        database="flask_database_hm8f",
        user="flask_database_hm8f_user",
        password="04wuX0sGZ6Y29Cp4nU6LuFIUPIRQV1AD",
    )

engine = create_engine("postgresql+psycopg2://", creator=get_connection)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Conversion(Base):
    __tablename__ = 'conversions'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    from_currency: Mapped[str] = mapped_column(String(3))
    to_currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Float)
    result: Mapped[float] = mapped_column(Float)

Base.metadata.create_all(engine)
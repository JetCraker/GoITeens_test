from sqlalchemy import String, Float, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

PGUSER = "Ваші_дані"
PGPASSWORD = "Ваші_дані"

engine = create_engine(
    f"postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@localhost:5433/web_convertor",
    echo=True
)
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
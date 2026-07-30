from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn


class Base(DeclarativeBase):
    pass


class ShortURL(Base):
    __tablename__ = "short_urls"

    slug: Mapped[str] = MappedColumn(primary_key=True)
    long_url: Mapped[str] = MappedColumn(nullable=False)
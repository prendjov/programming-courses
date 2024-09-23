"""
Database models for courses.
"""


from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    ...

class Course(Base):
    """Represents a course."""

    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    price: Mapped[float]
    duration: Mapped[int]
    url: Mapped[str]
    buyable: Mapped[bool] = mapped_column(default=False)

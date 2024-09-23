"""
DTO for courses.
"""

from pydantic import BaseModel

class CoursesDTO(BaseModel):
    """DTO representing courses."""

    id: int
    title: str
    description: str
    price: float
    duration: int
    buyable: bool

class BoughtCoursesDTO(BaseModel):
    """DTO representing courses."""

    id: int
    title: str
    description: str
    price: float
    duration: int
    url: str
    buyable: bool




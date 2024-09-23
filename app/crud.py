"""
Module containing CRUD operations for courses.
"""

from sqlalchemy.orm import Session
from app import models

from app.dto import CoursesDTO


def create_course(db: Session, course_data: CoursesDTO):
    """Create a new course."""
    course_obj = models.Course(**course_data.dict())
    db.add(course_obj)
    db.commit()
    db.refresh(course_obj)
    return course_obj


def read_course(db: Session, course_id: int):
    """Retrieve a course by ID."""
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def update_course(db: Session, course_id: int, course_data: CoursesDTO):
    """Update a course."""
    course_obj = read_course(db, course_id)
    if course_obj:
        for field, value in course_data:
            setattr(course_obj, field, value)
        db.commit()
        db.refresh(course_obj)
    return course_obj

def delete_course(db: Session, course_id: int):
    """Delete a course."""
    course_obj = read_course(db, course_id)
    if course_obj:
        db.delete(course_obj)
        db.commit()
    return course_obj

def toggle_buyable_course(db: Session, course_id: int):
    """Toggle course buyable attribute."""
    course_obj = read_course(db, course_id)
    course_obj.buyable = not course_obj.buyable
    db.commit()
    db.refresh(course_obj)
    return course_obj

def list_courses(db: Session):
    """List all courses."""
    return db.query(models.Course).all()

def list_buyable_courses(db: Session):
    """List buyable courses."""
    return db.query(models.Course).filter(models.Course.buyable).all()

def read_bought_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id and models.Course.buyable).first()
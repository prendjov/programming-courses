"""
Main FastAPI application and endpoints.
"""
import time
from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from app.db import SessionLocal, engine
from app import crud
from app.models import Base

from app.dto import CoursesDTO, BoughtCoursesDTO

app = FastAPI()

for i in range(5):
    try:
        Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        time.sleep(i + 1)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/course/", response_model=CoursesDTO)
def create_course(courseData: BoughtCoursesDTO, db: Session = Depends(get_db)):
    """Create a course."""
    return crud.create_course(db=db, course_data=courseData)


@app.get("/course/{course_id}", response_model=CoursesDTO)
def read_course(course_id: int, db: Session = Depends(get_db)):
    """Read a single course."""
    course_response = crud.read_course(db=db, course_id=course_id)
    if course_response is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course_response

@app.put("/course/{course_id}", response_model=CoursesDTO)
def update_course(course_id: int, courseData: CoursesDTO, db: Session = Depends(get_db)):
    """Update a course."""
    course_response = crud.update_course(db=db, course_id=course_id, data=courseData)
    if course_response is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course_response


@app.delete("/course/{course_id}", response_model=CoursesDTO)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    """Delete a course."""
    course_response = crud.delete_course(db=db, course_id=course_id)
    if course_response is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course_response


@app.get("/courses/", response_model=List[CoursesDTO])
def list_courses(db: Session = Depends(get_db)):
    """List all courses."""
    return crud.list_courses(db=db)

@app.get("/courses/buyable/", response_model=List[CoursesDTO])
def list_courses(db: Session = Depends(get_db)):
    """List all buyable courses."""
    return crud.list_buyable_courses(db=db)

@app.get("/course/buy/{course_id}", response_model=CoursesDTO)
def toggle_course_buyable(course_id: int, db: Session = Depends(get_db)):
    """Toggle course buyable attribute."""
    course_response = crud.toggle_buyable_course(db=db, course_id=course_id)
    if course_response is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course_response

@app.get("/course/buy/{course_id}", response_model=BoughtCoursesDTO)
def read_course(course_id: int, db: Session = Depends(get_db)):
    """Buy course."""
    course_response = crud.bu(db=db, course_id=course_id)
    if course_response is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course_response


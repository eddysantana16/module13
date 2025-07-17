from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/calculations", tags=["Calculations"])

@router.post("/", response_model=schemas.CalculationRead)
def create_calculation(calc: schemas.CalculationCreate, db: Session = Depends(get_db)):
    db_calc = models.Calculation(**calc.model_dump())
    db.add(db_calc)
    db.commit()
    db.refresh(db_calc)
    return db_calc

@router.get("/", response_model=list[schemas.CalculationRead])
def get_all_calculations(db: Session = Depends(get_db)):
    return db.query(models.Calculation).all()

@router.get("/{calc_id}", response_model=schemas.CalculationRead)
def get_calculation(calc_id: int, db: Session = Depends(get_db)):
    calc = db.query(models.Calculation).filter(models.Calculation.id == calc_id).first()
    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found")
    return calc

@router.put("/{calc_id}", response_model=schemas.CalculationRead)
def update_calculation(calc_id: int, updated: schemas.CalculationCreate, db: Session = Depends(get_db)):
    calc = db.query(models.Calculation).filter(models.Calculation.id == calc_id).first()
    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found")
    for key, value in updated.model_dump().items():
        setattr(calc, key, value)
    db.commit()
    db.refresh(calc)
    return calc

@router.delete("/{calc_id}")
def delete_calculation(calc_id: int, db: Session = Depends(get_db)):
    calc = db.query(models.Calculation).filter(models.Calculation.id == calc_id).first()
    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found")
    db.delete(calc)
    db.commit()
    return {"detail": "Calculation deleted"}

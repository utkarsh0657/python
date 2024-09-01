from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Request

router = APIRouter()

@router.get("/status/{request_id}")
def get_status(request_id: str, db: Session = Depends(get_db)):
    request = db.query(Request).filter(Request.request_id == request_id).first()
    if not request:
        return {"error": "Request not found"}
    return {"status": request.status}

from fastapi import APIRouter, UploadFile, File, Depends
from uuid import uuid4
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Request, Product
from app.workers import process_images
import csv
import asyncio

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    request_id = str(uuid4())
    
    # Save request
    new_request = Request(request_id=request_id)
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    
    # Process CSV
    csv_data = await file.read()
    decoded_csv = csv_data.decode('utf-8').splitlines()
    csv_reader = csv.reader(decoded_csv)
    
    for row in csv_reader:
        if row[0].lower() == "s. no.":
            continue
        
        product = Product(
            request_id=new_request.request_id,
            serial_number=int(row[0]),
            product_name=row[1],
            input_image_urls=row[2],
        )
        db.add(product)
    
    db.commit()

    # Process images asynchronously
    asyncio.create_task(process_images(request_id))
    
    return {"request_id": request_id}

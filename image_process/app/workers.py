import asyncio
from app.database import SessionLocal
from app.models import Product, Request
from app.services.webhook import trigger_webhook
from app.utils import fetch_image, compress_image

async def process_images(request_id: str):
    db = SessionLocal()
    products = db.query(Product).filter(Product.request_id == request_id).all()

    for product in products:
        input_urls = product.input_image_urls.split(",")
        output_urls = []

        for url in input_urls:
            image_data = await fetch_image(url.strip())
            compressed_image = compress_image(image_data)
            # Simulate saving the compressed image to a storage service
            output_url = url.replace("public", "processed")
            output_urls.append(output_url)

        product.output_image_urls = ",".join(output_urls)
        product.status = "COMPLETED"
        db.commit()

    # Update request status
    request = db.query(Request).filter(Request.request_id == request_id).first()
    request.status = "COMPLETED"
    db.commit()

    # Trigger webhook
    await trigger_webhook(request_id)

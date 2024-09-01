from fastapi import APIRouter, BackgroundTasks

router = APIRouter()

@router.post("/webhook")
def webhook_handler(background_tasks: BackgroundTasks):
    # Handle webhook events here
    background_tasks.add_task(handle_event)
    return {"message": "Webhook received"}

def handle_event():
    # Logic to handle webhook
    pass

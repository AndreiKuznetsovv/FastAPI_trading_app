from fastapi import APIRouter, Depends

from src.auth.config import current_user
from src.background_tasks.services import send_email_report_dashboard

router = APIRouter()


# protected route for authenticated users
@router.get('/dashboard')
async def get_dashboard_report(user=Depends(current_user)):
    send_email_report_dashboard.delay(username=user.username)
    return {
        "status": 200,
        "data": None,
        "detail": "Mail successfully sent"
    }

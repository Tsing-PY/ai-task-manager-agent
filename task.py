from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/")
def get_tasks():
    return {"tasks": []}

@router.post("/")
def create_task():
    return {"message": "Task created"}

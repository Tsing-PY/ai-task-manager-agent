from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# 初始化FastAPI应用
app = FastAPI(title="AI Agent Task Manager", version="1.0")

# 任务数据模型
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = "medium"
    status: str = "pending"

# 示例接口
@app.get("/")
def home():
    return {"message": "AI Agent 智能任务管理系统 - 后端服务运行中"}

# 任务创建接口
@app.post("/task/create")
def create_task(task: Task):
    return {"status": "success", "data": task.dict(), "msg": "任务创建成功"}

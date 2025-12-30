from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from datetime import datetime

from database import db
from auth import get_current_user
from models import TaskCreate, TaskUpdate

router = APIRouter()

tasks_collection = db["tasks"]


# 🟢 CREATE TASK
@router.post("/tasks")
def create_task(
    task: TaskCreate,
    current_user: dict = Depends(get_current_user)
):
    new_task = {
        "title": task.title,
        "description": task.description,
        "completed": False,
        "user_email": current_user["sub"],
        "created_at": datetime.utcnow()
    }

    result = tasks_collection.insert_one(new_task)

    return {
        "message": "Task created successfully",
        "task_id": str(result.inserted_id)
    }


# 🟢 GET ALL TASKS (USER ONLY)
@router.get("/tasks")
def get_tasks(current_user: dict = Depends(get_current_user)):
    tasks = []

    for task in tasks_collection.find({"user_email": current_user["sub"]}):
        task["_id"] = str(task["_id"])
        tasks.append(task)

    return tasks


# 🟢 UPDATE TASK
@router.put("/tasks/{task_id}")
def update_task(
    task_id: str,
    task: TaskUpdate,
    current_user: dict = Depends(get_current_user)
):
    updated_data = {k: v for k, v in task.dict().items() if v is not None}

    result = tasks_collection.update_one(
        {"_id": ObjectId(task_id), "user_email": current_user["sub"]},
        {"$set": updated_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task updated successfully"}


# 🟢 DELETE TASK
@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: str,
    current_user: dict = Depends(get_current_user)
):
    result = tasks_collection.delete_one(
        {"_id": ObjectId(task_id), "user_email": current_user["sub"]}
    )

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}

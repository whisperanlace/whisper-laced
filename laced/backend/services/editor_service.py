# services/Editor_service.py
from sqlalchemy.orm import Session
from app.models.Editor import Editor
from fastapi import HTTPException, status

class EditorService:
    async def create_project(self, db: Session, user_id: int, data: dict):
        project = Editor(user_id=user_id, **data)
        db.add(project)
        db.commit()
        db.refresh(project)
        return project

    async def get_project(self, db: Session, project_id: int):
        project = db.query(Editor).filter(Editor.id == project_id).first()
        if not project:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
        return project

    async def update_project(self, db: Session, project_id: int, updates: dict):
        project = await self.get_project(db, project_id)
        for key, value in updates.items():
            setattr(project, key, value)
        db.commit()
        db.refresh(project)
        return project

# services/Report_service.py
from sqlalchemy.orm import Session
from app.models.Report import Report

class ReportService:
    async def create_report(self, db: Session, reporter_id: int, target_id: int, reason: str):
        report = Report(reporter_id=reporter_id, target_id=target_id, reason=reason)
        db.add(report)
        db.commit()
        db.refresh(report)
        return report

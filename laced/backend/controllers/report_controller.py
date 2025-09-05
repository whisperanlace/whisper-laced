from fastapi import HTTPException
from backend.services.report_service import ReportService
from backend.schemas.report_schema import ReportSchema

report_service = ReportService()

class ReportController:

    async def submit_report(self, payload: ReportSchema, current_user):
        try:
            return await report_service.submit_report(payload, current_user)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def list_reports(self, current_user):
        return await report_service.get_reports(current_user)

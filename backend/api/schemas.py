from pydantic import BaseModel
from typing import Optional


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


class UploadResponse(BaseModel):
    report_id: str
    filename: str
    status: str
    message: str


class ReportStatus(BaseModel):
    report_id: str
    status: str
    progress: int
    message: Optional[str] = None

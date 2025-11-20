from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from typing import Optional


class AssetBase(BaseModel):
    name: str
    category: str
    purchase_date: date
    serial_number: str


class AssetCreate(AssetBase):
    pass


class AssetUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    purchase_date: Optional[date] = None
    serial_number: Optional[str] = None


class Asset(AssetBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None


class PDFReportResponse(BaseModel):
    message: str
    file_path: str
    generated_at: datetime
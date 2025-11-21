import os
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.database.database import get_db
from app.services.assets_service import get_assets, get_asset, create_asset, update_asset, delete_asset
from app.schemas.asset import Asset, AssetCreate, AssetUpdate, PDFReportResponse
from app.services.pdf_service import generate_assets_report

router = APIRouter(prefix="/assets", tags=["assets"])

@router.post("/", response_model=Asset)
def create_asset_endpoint(asset: AssetCreate, db: Session = Depends(get_db)):
    try:
        return create_asset(db, asset)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/", response_model=List[Asset])
def read_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        assets = get_assets(db, skip=skip, limit=limit)
        return assets
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/{asset_id}", response_model=Asset)
def read_asset(asset_id: int, db: Session = Depends(get_db)):
    try:
        db_asset = get_asset(db, asset_id)
        if db_asset is None:
            raise HTTPException(status_code=404, detail="Asset not found")
        return db_asset
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.put("/{asset_id}", response_model=Asset)
def update_asset_endpoint(asset_id: int, asset_update: AssetUpdate, db: Session = Depends(get_db)):
    try:
        db_asset = update_asset(db, asset_id, asset_update)
        if db_asset is None:
            raise HTTPException(status_code=404, detail="Asset not found")
        return db_asset
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/{asset_id}")
def delete_asset_endpoint(asset_id: int, db: Session = Depends(get_db)):
    try:
        success = delete_asset(db, asset_id)
        if not success:
            raise HTTPException(status_code=404, detail="Asset not found")
        return {"message": "Asset deleted successfully"}
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/report/pdf", response_model=PDFReportResponse)
def generate_pdf_report(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"assets_report_{timestamp}.pdf"
        filepath = os.path.join("reports", filename)

        def generate_report():
            try:
                assets = get_assets(db)
                generate_assets_report(assets)
            except Exception:
                pass

        background_tasks.add_task(generate_report)

        return PDFReportResponse(
            message="PDF report generation started in background",
            file_path=filepath,
            generated_at=datetime.now()
        )
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to start PDF generation")
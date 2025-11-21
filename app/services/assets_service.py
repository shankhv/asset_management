from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate


def get_assets(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Asset).offset(skip).limit(limit).all()
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to fetch assets")


def get_asset(db: Session, asset_id: int):
    try:
        return db.query(Asset).filter(Asset.id == asset_id).first()
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to fetch asset")


def create_asset(db: Session, asset: AssetCreate):
    try:
        existing = db.query(Asset).filter(Asset.serial_number == asset.serial_number).first()
        if existing:
            raise HTTPException(status_code=400, detail="Asset with this serial number already exists")

        db_asset = Asset(
            name=asset.name,
            category=asset.category,
            purchase_date=asset.purchase_date,
            serial_number=asset.serial_number
        )
        db.add(db_asset)
        db.commit()
        db.refresh(db_asset)
        return db_asset
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create asset")


def update_asset(db: Session, asset_id: int, asset: AssetUpdate):
    try:
        db_asset = db.query(Asset).filter(Asset.id == asset_id).first()
        if not db_asset:
            return None

        for field, value in asset.dict(exclude_unset=True).items():
            setattr(db_asset, field, value)

        db.commit()
        db.refresh(db_asset)
        return db_asset
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update asset")


def delete_asset(db: Session, asset_id: int):
    try:
        db_asset = db.query(Asset).filter(Asset.id == asset_id).first()
        if not db_asset:
            return False

        db.delete(db_asset)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to delete asset")
from sqlalchemy.orm import Session
from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate


def get_assets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Asset).offset(skip).limit(limit).all()


def get_asset(db: Session, asset_id: int):
    return db.query(Asset).filter(Asset.id == asset_id).first()


def create_asset(db: Session, asset: AssetCreate):
    # Check if serial number exists
    existing = db.query(Asset).filter(Asset.serial_number == asset.serial_number).first()
    if existing:
        raise Exception("Serial number already exists")

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


def update_asset(db: Session, asset_id: int, asset: AssetUpdate):
    db_asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if db_asset:
        for field, value in asset.dict(exclude_unset=True).items():
            setattr(db_asset, field, value)
        db.commit()
        db.refresh(db_asset)
    return db_asset


def delete_asset(db: Session, asset_id: int):
    db_asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if db_asset:
        db.delete(db_asset)
        db.commit()
        return True
    return False
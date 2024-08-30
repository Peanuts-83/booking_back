import re
from fastapi import HTTPException
from sqlalchemy.orm import Session

from .db_models import Models

def validate_foreign_keys_before_insert(mapper, connection, target):
    """
    Check for existing FK in database for any "ref_<foreign_key_name>_id"
    """
    session = Session(bind=connection)
    for prop in target.__table__.columns:
        if re.search(r"ref_(\w+)_id", prop.name):
            modelName = re.match(r"ref_(\w+)_id", prop.name).group(1)
            model = [m for m in Models if m.__name__ == modelName.capitalize()][0]
            #  request DB for <modelName>_id value
            if not session.query(model).filter(getattr(model, modelName + '_id') == getattr(target, prop.name)).first():
                raise HTTPException(status_code=409, detail={"msg": "undefined Foreign Key reference", "key": modelName + '_id', "value": getattr(target, prop.name)})
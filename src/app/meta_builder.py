from typing import Any
from pydantic import BaseModel

from .bo import get_lib


class Meta(BaseModel):
    aff: bool
    lib: str
    order: int
    name: str


def set_metas(bean: BaseModel) -> list[Meta]:
    metas = []
    counter = 0
    for column in bean.model_fields:
        metas.append(
            {"name": column, "lib": get_lib(column), "order": counter, "aff": True}
        )
        counter += 1
    return metas

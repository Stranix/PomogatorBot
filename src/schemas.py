from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    full_name: str
    tg_id: int
    is_admin: bool
    btrx_id: Optional[int] = 0
    department_id: Optional[int] = 0
    id: Optional[int] = 0


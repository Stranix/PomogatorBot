from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: int
    full_name: str
    tg_id: int
    btrx_id: Optional[int]
    department_id: int
    is_admin: bool

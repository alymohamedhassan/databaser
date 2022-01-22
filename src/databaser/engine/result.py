from typing import Optional, List, Dict

from pydantic import BaseModel


class ExecutionResult(BaseModel):
    has_values: bool
    sql: str
    result: Optional[List[Dict]]

"""
Description: The file containing Pydantic schemas for resource1.
"""

## -- 3rd Party Imports -- ##
from pydantic import BaseModel

## -- Schema For Resource 1 -- ##

# Example of how to create a Pydantic Schema
class Resource1(BaseModel):
    name: str
    email: str
    year: int
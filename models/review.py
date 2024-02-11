#!/usr/bin/python3
"""Review class module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represent a review.
    All attrbutes should be empty
    """
    place_id = ""
    user_id = ""
    text = ""

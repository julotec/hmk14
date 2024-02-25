from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr



class UserModel(BaseModel):
    """
    Model representing user data.

    Attributes:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The user's email address.
        phone_number (str): The user's phone number.
        date_of_birth (date): The user's date of birth.
        additional_data (Optional[str]): Additional data about the user (optional).
    """

    first_name: str
    last_name: str
    email: str
    phone_number: str
    date_of_birth: date
    additional_data: Optional[str] = None

class ContactCreate(BaseModel):
    """
    Model for creating a new contact.
    """
    pass

class Contact(BaseModel):
    """
    Model representing a contact.

    Attributes:
        id (int): The contact's identifier.
    """
    id: int

    class Config:
        orm_mode = True

class ContactUpdate(BaseModel):
    """
    Model for updating contact information.

    Attributes (optional):
        first_name (str): The contact's new first name.
        last_name (str): The contact's new last name.
        email (str): The contact's new email address.
        phone_number (str): The contact's new phone number.
        date_of_birth (date): The contact's new date of birth.
        additional_data (str): Additional data about the contact.
    """
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    additional_data: Optional[str] = None

class ContactSearchQuery(BaseModel):
    """
    Model for searching contacts.

    Attributes:
        query (str): The search query.
    """
    query: str

class ContactBirthday(BaseModel):
    """
    Model representing contacts with upcoming birthdays.

    Attributes:
        contacts (List[Contact]): List of contacts with upcoming birthdays.
    """
    contacts: List[Contact]


class UserDb(BaseModel):
    """
    Model representing user data retrieved from the database.

    Attributes:
        id (int): The user's identifier.
        username (str): The user's username.
        email (str): The user's email address.
        created_at (datetime): The timestamp when the user was created.
        avatar (str): URL of the user's avatar.
    """
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True

class TokenModel(BaseModel):
    """
    Model representing authentication tokens.

    Attributes:
        access_token (str): The access token.
        refresh_token (str): The refresh token.
        token_type (str): The type of token (default: "bearer").
    """
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RequestEmail(BaseModel):
    """
    Model representing a request containing an email address.

    Attributes:
        email (EmailStr): The email address.
    """
    email: EmailStr


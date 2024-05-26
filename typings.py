from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum


class Currency(str, Enum):

    pkr = "pkr"
    usd = "usd"


class Contract(BaseModel):

    id: Optional[str]
    title: str
    description: str
    price: float
    currency: Currency
    valid_till: str
    complete_till: str


class Bid(BaseModel):

    id: Optional[str]
    contract_id: str
    contractor_id: Optional[str]
    remarks: str
    bid_price: float
    expected_complete_till: str


class ContractAward(BaseModel):

    id: Optional[str]
    contract_id: str
    contractor_id: str
    bid_id: str
    remarks: str
    awarded_on: str
    awarded_by: Optional[str]
    awarded_by_address: Optional[str]
    signature: Optional[str]


class VerifyAward(BaseModel):
    id: Optional[str]
    award_id: str
    remarks: str
    verified_on: str
    verified_by: Optional[str]
    verified_by_address: Optional[str]
    signature: Optional[str]


class Deliverable(BaseModel):

    id: Optional[str]
    award_id: str
    contractor_id: str
    created_by: Optional[str]
    created_by_address: Optional[str]
    deliverable_text: str
    deliverable_expected_complete_till: str


class DeliverableCompletion(BaseModel):

    id: Optional[str]
    deliverable_id: str
    deliverable_complete: str
    contractor_id: str
    remarks: str
    cost: float
    documents: List[str]
    completed: bool = True


class MarkDeliverableCompletion(BaseModel):
    id: Optional[str]
    completed_deliverable_id: str
    remarks: str
    marked_on: str
    marked_by: Optional[str]
    marked_by_address: Optional[str]
    signature: Optional[str]
    tokens: float


class PasswordChangeRequest(BaseModel):
    username: str
    password_old: str
    password_new: str


class SignUpContractor(BaseModel):
    username: str
    password: str
    role: str = "CONTRACTOR"
    licenses: List[str]
    documents: List[str]


class ContractCompletion(BaseModel):
    id: Optional[str]
    contract_id: str
    remarks: str
    marked_on: str
    marked_by: Optional[str]
    marked_by_address: Optional[str]
    signature: Optional[str]

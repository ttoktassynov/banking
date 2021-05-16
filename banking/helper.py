from enum import IntEnum

class AccountStatuses(IntEnum):
  ENABLED = 1
  DISABLED = 2
  DELETED = 3
  PROFORMA = 4 
  PENDING = 5
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class CreditDebitCodes(IntEnum):
  CREDIT = 1
  DEBIT = 2
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]


from datetime import datetime

class Expense:
    def __init__(self, id, description, amount):
        self.id = id
        self.description = description
        self.amount = amount
        self.createdAt = datetime.now().date().isoformat()
        self.createdBy = datetime.now().time().isoformat()
        self.updatedAt = datetime.now().isoformat()
        self.month =  datetime.now().month


    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "createdAt": self.createdAt,
            "createdBy": self.createdBy,
            "updatedAt": self.updatedAt,
            "month": self.month,
        }

class AccountNumber:
    def __init__(self, value):
        self.validate(value)
        self.value = value

    def validate(self, value):
        if len(value) != 6:
            raise ValueError("wrong number account")

    def __hash__(self):
        return hash(self.value)

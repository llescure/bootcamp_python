class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest: int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        is_str_origin = isinstance(origin, str)
        is_int_origin = isinstance(origin, int)
        is_str_dest = isinstance(dest, str)
        is_int_dest = isinstance(dest, int)
        is_present_origin = False
        is_present_dest = False
        check_number_attributes = 0
        check_attributes_start = False

        #Check the object type
        for accounts in self.account:
            if type(accounts) != Account:
                print("Accounts given are not of the good type")

        #Check type and if the name/id given are correct for origin
        if is_str_origin:
            self.origin = str(origin)
            for accounts in self.account:
                if accounts.name == self.origin:
                    is_present_origin = True
        elif is_int_origin:
            self.origin = int(origin)
            for accounts in self.account:
                if accounts.id == self.origin:
                    is_present_origin = True
        else:
            print("The type of the origin doesn't match")
            return False
        if is_present_origin is False:
            print("The name of the origin account doesn't match any \
name/id account")
            return False

        #Check type and if the name/id given are correct for dest
        if is_str_dest:
            self.dest = str(dest)
            for accounts in self.account:
                if accounts.name == self.dest:
                    is_present_dest = True
        elif is_int_origin:
            self.dest = int(dest)
            for accounts in self.account:
                if accounts.id == self.dest:
                    is_present_dest = True
        else:
            print("The type of the dest doesn't match")
            return False
        if is_present_dest is False:
            print("The name of the dest account doesn't match any \
name/id account")
            return False

        #Check the type and value of amount is correct
        try:
            self.amount = float(amount)
        except ValueError:
            print("The type of the amount doesn't match")
            return False
        else:
            if self.amount < 0:
                print("The transaction is invalid the amount is negative")
                return False
            for accounts in self.account:
                if accounts.id is self.dest or accounts.name is self.dest:
                    if accounts.__dict__["value"] < self.amount:
                        print("Not enough money on the account of {} for the \
transfer".format(self.origin))
                        return False

        #Check if bank account is corrupted
        for accounts in self.account:
            if accounts.id is self.dest or accounts.name is self.dest:
                bank_account_parameters = dir(accounts)
        if (len(bank_account_parameters)) % 2 == 0:
            print("Even number of attributes, the file is corrupted")
            return False
        for attributes in bank_account_parameters:
            if attributes is "name":
                check_number_attributes += 1
            elif attributes is "id":
                check_number_attributes += 1
            elif attributes is "value":
                check_number_attributes += 1
            elif attributes.startswith("b"):
                print("An attribute starts with b")
                return False
            elif attributes.startswith("zip") or attributes.startswith("addr"):
                check_attributes_start = True
        if check_number_attributes != 3:
            print("All attributes name, id and value are not present")
            return False
        if check_attributes_start is False:
            print("No attributes start with zip or addr")
            return False

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return True if success, False if an error occured
        """
        is_str_account = isinstance(account, str)
        is_str_account = isinstance(account, int)
        if is_str_account:
            self.account = str(account)
        elif is_int_account:
            self.account = int(account)
        else:
            print("The type of the account doesn't match")
            return False

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

    def bank_account_is_corrupted(self, whois):
        check_number_attributes = 0
        check_attributes_start = False
        self.whois = whois
        for accounts in self.account:
            if accounts.id is self.whois or accounts.name is self.whois:
                bank_account_parameters = dir(accounts)
        if (len(bank_account_parameters)) % 2 == 0:
            return True
        for attributes in bank_account_parameters:
            if attributes is "name":
                check_number_attributes += 1
            elif attributes is "id":
                check_number_attributes += 1
            elif attributes is "value":
                check_number_attributes += 1
            elif attributes.startswith("b"):
                return True
            elif attributes.startswith("zip") or attributes.startswith("addr"):
                check_attributes_start = True
        if check_number_attributes != 3:
            return True
        if check_attributes_start is False:
            return True
        return False

    def transfer(self, origin, dest, amount):
        is_str_origin = isinstance(origin, str)
        is_int_origin = isinstance(origin, int)
        is_str_dest = isinstance(dest, str)
        is_int_dest = isinstance(dest, int)
        is_present_origin = False
        is_present_dest = False

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

        #Check if banks accounts are corrupted
        if self.bank_account_is_corrupted(self.origin) or \
        self.bank_account_is_corrupted(self.dest):
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

    def modify_bank_account(self, account_selected, bank_parameters):
        self.account_selected = account_selected
        self.bank_parameters = bank_parameters
        even = False
        check_attributes_name = False
        check_attributes_id = False
        check_attributes_value = False
        check_attributes_start = False
        check_attributes_start_b = False
        #Find the parameters which don't correspond to the criteria
        if (len(self.bank_parameters)) % 2 == 0:
            even = True
        for attributes in self.bank_parameters:
            if attributes is "name":
                check_attributes_name = True
            elif attributes is "id":
                check_attributes_id = True
            elif attributes is "value":
                check_attributes_value = True
            elif attributes.startswith("b"):
                check_attributes_start_b = True
            elif attributes.startswith("zip") or attributes.startswith("addr"):
                check_attributes_start = True
        #Modify the parameters inside the class
        for accounts in self.account:
               if accounts.id is self.account_selected or accounts.name \
                is self.account_selected:
                    if even:
                        if check_attributes_start is False:
                            accounts.__dict__["zip"] = 0
                            check_attributes_start = True
                        elif check_attributes_name is False:
                            accounts.__dict__["name"] = "Unknown"
                            check_attributes_name = True
                        elif check_attributes_id is False:
                            accounts.__dict__["id"] = None
                            check_attributes_id = True
                        elif check_attributes_value is False:
                            check_attributes_value = True
                            accounts.__dict__["value"] = 0
                        else:
                            accounts.__dict__["toto"] = ""
                    elif check_attributes_start is False:
                        check_attributes_start = True
                        accounts.__dict__["zip"] = 0
                        accounts.__dict__["toto"] = ""
                    elif check_attributes_name is False:
                        check_attributes_name = True
                        accounts.__dict__["name"] = "Unknown"
                        accounts.__dict__["toto"] = ""
                    elif check_attributes_id is False:
                        check_attributes_id = True
                        accounts.__dict__["id"] = None
                        accounts.__dict__["toto"] = ""
                    elif check_attributes_value is False:
                        check_attributes_value = True
                        accounts.__dict__["value"] = 0
                        accounts.__dict__["toto"] = ""

    def fix_account(self, account):
        is_str_account_selected = isinstance(account, str)
        is_int_account_selected = isinstance(account, int)
        if is_str_account_selected:
            self.account_selected = str(account)
        elif is_int_account_selected:
            self.account_selected = int(account)
        else:
            print("The type of the account doesn't match")
            return False
        if self.bank_account_is_corrupted(self.account_selected):
            for accounts in self.account:
               if accounts.id is self.account_selected or accounts.name \
                       is self.account_selected:
                    bank_account_parameters = dir(accounts)
            #for accounts in self.account:
             #   print(accounts.__dict__)
            while self.bank_account_is_corrupted(self.account_selected):
                self.modify_bank_account(self.account_selected, \
                bank_account_parameters)
            print("The file is not corrupted anymore")
        else:
            print("The account is not corrupted. The error is elsewhere")
            return False

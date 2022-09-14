class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        print(f'{kwargs=}')
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

    def is_corrupted(self) -> bool:
        attributes = dir(self)
        if len(attributes) % 2 == 0:
            return True
        if any(attr.startswith('b') for attr in self.__dict__.keys()):
            return True
        if not any(attr.startswith('zip') or attr.startswith('addr') for attr in self.__dict__.keys()):
            return True
        if not all(k in self.__dict__.keys() for k in ['name', 'id', 'value']):
            return True
        if not isinstance(self.name, str):
            return True
        if not isinstance(self.id, int):
            return True
        if not isinstance(self.value, int) and not isinstance(self.value, float):
            return True
        return False

    def fix(self) -> bool:
        if not self.is_corrupted():
            return True
        if 'id' not in dir(self) or not isinstance(self.id, int):
            setattr(self, 'id', Account.ID_COUNT)
            self.id = Account.ID_COUNT
            Account.ID_COUNT += 1
        if 'name' not in dir(self) or not isinstance(self.name, str):
            setattr(self, 'name', f'Peer de Bakker_{self.id}')
        if 'value' not in dir(self) or (not isinstance(self.value, int) and not isinstance(self.value, float)):
            setattr(self, 'value', 0)
        _ = [delattr(self, attr) for attr in dir(self) if attr.startswith('b')]
        if not any(attr.startswith('zip') or attr.startswith('addr') for attr in dir(self)):
            setattr(self, 'zip', 75017)
        if len(dir(self)) % 2 == 0:
            setattr(self, 'super_secret_dummy_var', '#Vela')
        return not self.is_corrupted()


class Bank:
    """The bank"""

    def __init__(self):
        self.accounts = []

    def find_account(self, name: str) -> Account | None:
        if not isinstance(name, str):
            return None
        for acc in self.accounts:
            if acc.name == name:
                return acc
        return None

    def add(self, new_account: Account) -> bool:
        """Add new account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            return False
        if any(acc.name == new_account.name for acc in self.accounts):
            return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin: str, dest: str, amount: float) -> bool:
        """"Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            return False
        acc_origin = self.find_account(origin)
        acc_dest = self.find_account(dest)
        if acc_origin is None or acc_origin.is_corrupted() or acc_dest is None or acc_dest.is_corrupted():
            return False
        if acc_origin.value < amount:
            return False
        acc_origin.value -= amount
        acc_dest.value += amount
        return True

    def fix_account(self, name: str) -> bool:
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        account = self.find_account(name)
        if account is None:
            print('cant find account')
            return False
        if not account.is_corrupted():
            print('its not corrupted tho?')
            return True
        if 'id' not in dir(account) or not isinstance(account.id, int):
            setattr(account, 'id', Account.ID_COUNT)
            account.id = Account.ID_COUNT
            Account.ID_COUNT += 1
        if 'name' not in dir(account) or not isinstance(account.name, str):
            setattr(account, 'name', f'Peer de Bakker_{account.id}')
        if 'value' not in dir(account) or (not isinstance(account.value, int) and not isinstance(account.value, float)):
            setattr(account, 'value', 0)
        _ = [delattr(account, attr) for attr in dir(account) if attr.startswith('b')]
        if not any(attr.startswith('zip') or attr.startswith('addr') for attr in dir(account)):
            setattr(account, 'zip', 75017)
        if len(dir(account)) % 2 == 0:
            setattr(account, 'super_secret_dummy_var', '#Vela')
        print(f'{account.is_corrupted() = }')
        return not account.is_corrupted()


def test() -> None:
    bank = Bank()
    peer = Account('Peer')
    print(f'{peer.is_corrupted()=}')
    add_ret = bank.add(peer)
    fix_ret = bank.fix_account('Peer')
    print(f'{add_ret=}, {fix_ret=}')
    print(f'{dir(peer)=}, {peer.zip}')


if __name__ == '__main__':
    test()

import abc
import json

from .models import Income


class BaseStorage(abc.ABC):
    @abc.abstractmethod
    def __len__(self) -> int:
        raise RuntimeError("Not implemented")

    @property
    @abc.abstractmethod
    def incomes(self):
        raise RuntimeError("Not implemented")
    
    @abc.abstractmethod
    def get_incomes(self):
        raise RuntimeError("Not implemented")
    
    @abc.abstractmethod
    def add_income(self, income):
        raise RuntimeError("Not implemented")
    
    @abc.abstractmethod
    def load(self):
        raise RuntimeError("Not implemented")

    @abc.abstractmethod
    def save(self):
        raise RuntimeError("Not implemented")
    

class MemoryStorage(BaseStorage):
    def __init__(self, incomes=None) -> None:
        self.items = incomes if incomes is not None else []

    def __repr__(self) -> str:
        return "<MemoryStorage total_incomes={}>".format(len(self))
    
    def __len__(self) -> int:
        return len(self.items)
    
    @property
    def incomes(self):
        return self.items

    def load(self):
        pass

    def save(self):
        pass

    def get_incomes(self):
        return self.items

    def add_income(self, income):
        if not isinstance(income, Income):
            raise ValueError("Should be an instance of Income")
        
        self.items.append(income)


class Storage(BaseStorage):
    def __init__(self, filename="store.json") -> None:
        if filename is None or len(filename) == 0:
            raise ValueError("Storage filename should be provided")
        
        self.filename = filename
        self.objects = []
    
    def __repr__(self) -> str:
        return "<Storage filename={}>".format(self.filename)
    
    def __len__(self) -> int:
        return len(self.objects)
    
    @property
    def incomes(self):
        return self.objects
    
    def load(self):
        try:
            with open(self.filename, "r") as f:
                incomes = list(map(Income.from_dict, json.load(f)))
            
            self.objects = incomes if incomes is not None else []
        except FileNotFoundError:
            print(f"Warning: {self.filename} does not exist. It will be created automatically with your first income.")

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(list(map(lambda x: x.to_dict(), self.objects)), f, indent=2)

    def get_incomes(self):
        return self.objects

    def add_income(self, income):
        if not isinstance(income, Income):
            raise ValueError("Should be an instance of Income")
        
        self.objects.append(income)

from dataclasses import dataclass

@dataclass
class DisplayDatatype:
    index: float
    data: str

class DisplayData:

    def __init__(self, display_data: DisplayDatatype):
        self.display_data = display_data
    
    def show_data(self):
        print(f"3rd party functionality: {self.display_data.index} - {self.display_data.data}")

@dataclass
class DatabaseDatatype:
    position: int
    amount: int

class StoreDatabaseData:

    def __init__(self, database_data: DatabaseDatatype):
        self.database_data = database_data
    
    def store_data(self):
        print(f"database data stored {self.database_data.position} - {self.database_data.amount}")


class DisplayDataAdapter(StoreDatabaseData, DisplayData):
    
    def __init__(self, data):
        self.data = data
    
    def store_data(self):
        for item in self.data:
            ddt = DisplayDatatype(float(item.position), str(item.amount))
            self.display_data = ddt
            self.show_data()


def generate_data():
    data = list()
    data.append(DatabaseDatatype(2,2))
    data.append(DatabaseDatatype(2,3))
    data.append(DatabaseDatatype(5,5))
    return data

if __name__ == "__main__":
    adapter = DisplayDataAdapter(generate_data())
    adapter.store_data()
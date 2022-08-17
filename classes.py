from abc import abstractmethod, ABC


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):

    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, count):
        self.__capacity = count

    def add(self, name, count):
        if name in self.__items.keys():
            if self._get_free_space() >= count:
                print("Товар добавлен!")
                self.__items[name] += count
                return True
            else:
                if isinstance(self, Shop):
                    print("Недостаточно места в магазине!")
                elif isinstance(self, Store):
                    print("Недостаточно места на складе!")
                return False
        else:
            if self._get_free_space() >= count:
                print("Товар добавлен!")
                self.__items[name] = count
                return True
            else:
                if isinstance(self, Shop):
                    print("Недостаточно места в магазине!")
                elif isinstance(self, Store):
                    print("Недостаточно места на складе!")
                return False

    def remove(self, name, count):
        if self.__items[name] >= count:
            print("Нужное количество есть на складе!")
            self.__items[name] -= count
            return True
        else:
            print("Недостаточно товара на складе!")
            return False

    def _get_free_space(self):
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space

    @property
    def get_items(self):
        return self.__items

    def _get_unique_items_count(self):
        return len(self.__items.keys())

    def __str__(self):
        st = "\n"
        for key, value in self.__items.items():
            st += f"{key}: {value}\n"
        return st

class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):
        if self._get_unique_items_count() >= 5:
            print("Слишком много уникальных товаров!")
            return False
        else:
            super().add(name, count)


class Request:

    # Доставить 3 печеньки из "склад" в магазин
    # Забрать 3 печеньки из "склад"
    # Привезти 3 печеньки из "склад

    def __init__(self, request_str):
        reg_list = request_str.split()
        action = reg_list[0]
        self.__count = int(reg_list[1])
        self.__item = reg_list[2]
        if action == "Доставить":
            self.__from = reg_list[4]
            self.__to = reg_list[6]
        elif action == "Забрать":
            self.__from = reg_list[4]
            self.__to = None
        elif action == "Привезти":
            self.__to = reg_list[4]
            self.__from = None

    def move(self):
        if self.__to and self.__from:
            if eval(self.__to).add(self.__item, self.__count):
                eval(self.__from).remove(self.__item, self.__count)
        elif self.__to:
            eval(self.__to).add(self.__item, self.__count)
        elif self.__from:
            eval(self.__from).remove(self.__item, self.__count)


storage_1 = Store(items={"Телефон": 10, "Компьютер": 10, "Телевизор": 20})
storage_2 = Store(items={"Телефон": 10, "Компьютер": 10, "Приставка": 10})
shop_1 = Shop(items={"Телефон": 3, "Компьютер": 3, "Телевизор": 3})



# storage_1 = Shop(items={"Телефон": 3, "Компьютер": 3})
#
# storage_1.add("Планшет", 3)
# storage_1.add("Приставка", 3)
# storage_1.add("Телевизор", 3)
# storage_1.add("Наушники", 3)
# storage_1.remove("Телефон", 2)
# print(storage_1.get_free_space())
# print(storage_1.get_items())
# print(storage_1.get_unique_items_count())
# print(storage_1)

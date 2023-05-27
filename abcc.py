from abc import ABC, abstractmethod


# Entity Classes
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Order:
    def __init__(self, id, user, products):
        self.id = id
        self.user = user
        self.products = products


class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Review:
    def __init__(self, id, product, user, rating, comment):
        self.id = id
        self.product = product
        self.user = user
        self.rating = rating
        self.comment = comment


# Generic Repository Interface
class Repository(ABC):
    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def search(self, criteria):
        pass


# Generic Unit of Work abstract class
class UnitOfWork(ABC):
    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass


# User Repository
class UserRepository(Repository):
    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)

    def delete(self, user):
        self.users.remove(user)

    def update(self, user):
        for i, u in enumerate(self.users):
            if u.id == user.id:
                self.users[i] = user
                break

    def get(self, id):
        for user in self.users:
            if user.id == id:
                return user
        return None

    def search(self, criteria):
        result = []
        for user in self.users:
            if criteria in user.name:
                result.append(user)
        return result


# Product Repository
class ProductRepository(Repository):
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def delete(self, product):
        self.products.remove(product)

    def update(self, product):
        for i, p in enumerate(self.products):
            if p.id == product.id:
                self.products[i] = product
                break

    def get(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None

    def search(self, criteria):
        result = []
        for product in self.products:
            if criteria in product.name:
                result.append(product)
        return result


# Order Repository
class OrderRepository(Repository):
    def __init__(self):
        self.orders = []

    def add(self, order):
        self.orders.append(order)

    def delete(self, order):
        self.orders.remove(order)

    def update(self, order):
        for i, o in enumerate(self.orders):
            if o.id == order.id:
                self.orders[i] = order
                break

    def get(self, id):
        for order in self.orders:
            if order.id == id:
                return order
        return None

    def search(self, criteria):
        result = []
        # for order in

from abc import ABC, abstractmethod

class FoodType:
    gujarati = 1
    punjabi = 2

class Restaurant:

    @abstractmethod
    def make_food(self):
        pass
    
    @abstractmethod
    def make_drink(self):
        pass

class GujaratiRestaurant(Restaurant):

    def make_food(self):
        return "Bhakhari"

    def make_drink(self):
        return "Chass"

class PunjabiRestaurant(Restaurant):

    def make_food(self):
        return "Panir Tufani"

    def make_drink(self):
        return "Punjabi chass"

class RestaurantFactory:

    @staticmethod
    def suggest_restaurant(res_type: FoodType):
        if res_type == FoodType.gujarati:
            return GujaratiRestaurant()
        else:
            return PunjabiRestaurant()

def dine_at(restaurant: Restaurant):
    print("For dinner we are having....")
    print(restaurant.make_food())
    print(restaurant.make_drink())


if __name__== "__main__":
    suggestion1 = RestaurantFactory.suggest_restaurant(FoodType.gujarati)
    suggestion2 = RestaurantFactory.suggest_restaurant(FoodType.punjabi)

    dine_at(suggestion1)
    dine_at(suggestion2)

class Cake:
    def __init__(self, name, price, ingredient):
        self.name = name
        self.price = price
        self.ingredient = ingredient


class Shop:
    def __init__(self):
        self.ingredient = {}
        self.product = {}

    def buy_ingredient(self, buy_dict):
        for key, value in buy_dict.items():
            if key in self.ingredient.keys():
                self.ingredient[key] += value
            else:
                self.ingredient[key] = value

    def current_ingredient(self):
        print("현재 보유한 재료는 ", end="")
        for idx, (key, value) in enumerate(self.ingredient.items()):
            print(f"{key}({value}개)", end=", " if idx < len(self.ingredient) - 1 else "입니다.\n")

    def make_cake(self, cake):
        need_ingredients = {}
        for key, value in cake.ingredient.items():
            if key not in self.ingredient.keys():
                need_ingredients[key] = value
            elif self.ingredient[key] < value:
                need_ingredients[key] = value - self.ingredient[key]

        if len(need_ingredients) != 0:
            for idx, (key, value) in enumerate(need_ingredients.items()):
                print(f"{key} 재료가 {value}개", end=", " if idx < len(need_ingredients) - 1 else " 부족합니다.\n")
            return

        for key, value in cake.ingredient.items():
            if value == self.ingredient[key]:
                del self.ingredient[key]
            else:
                self.ingredient[key] -= value

        self.product[cake] = self.product[cake] + 1 if cake in self.product.keys() else 1

        print(f"{cake.name} 1개 완성!")


class Pos:
    def __init__(self, cake_shop):
        self.cake_shop = cake_shop
        self.money = 0

    def current_cakes(self):
        print("현재 재고는")
        for key, value in self.cake_shop.product.items():
            print(f"{key.name}: {value}")

    def sell_cake(self, cakename):
        for key, value in self.cake_shop.product.items():
            if key.name == cakename and value > 0:
                print(f"{key.name} 판매 완료. 현재 남은 {key.name}의 개수는 {value - 1}개 입니다.")
                self.money += key.price
                if value == 1:
                    del self.cake_shop.product[key]
                else:
                    self.cake_shop.product[key] -= 1
                return

        print(f"{cakename} 재고가 없습니다.")

    def print_current_money(self):
        print(f"현재 판매 금액은 총 {self.money}원 입니다.")


cheesecake = Cake("Cheese Cake", 6900, {'cheese': 2, 'egg': 2, 'butter': 2})
chococake = Cake("Chocolate Cake", 5900, {'chocolate': 2, 'egg': 2, 'butter': 2})
carrotcake = Cake("Carrot Cake", 5500, {'carrot': 2, 'walnut': 2, 'egg': 1, 'butter': 1})
creamcake = Cake("Fresh Cream Cake", 4500, {'cream': 3, 'egg': 1, 'butter': 1})
swpotatocake = Cake("Sweet Potato Cake", 6500, {'sweet potato': 3, 'egg': 2, 'butter': 1})

cake_shop = Shop()
cake_shop.buy_ingredient({'cheese': 5, 'carrot': 3, 'sweet potato': 3, 'egg': 10, 'butter': 10})
cake_shop.current_ingredient()
cake_shop.buy_ingredient({'chocolate': 3, 'walnut': 2, 'egg': 12, 'butter': 12})
cake_shop.current_ingredient()

print("\nMAKE CAKE")
cake_shop.make_cake(creamcake)
print(cake_shop.ingredient)
cake_shop.make_cake(carrotcake)
print(cake_shop.ingredient)
cake_shop.make_cake(carrotcake)
print(cake_shop.ingredient)
cake_shop.make_cake(cheesecake)
print(cake_shop.ingredient)
cake_shop.make_cake(cheesecake)
print(cake_shop.ingredient)
cake_shop.make_cake(chococake)
print(cake_shop.ingredient)
cake_shop.make_cake(swpotatocake)
print(cake_shop.ingredient)
cake_shop.current_ingredient()

pos = Pos(cake_shop)
print()
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')
pos.current_cakes()

print()
pos.sell_cake('Chocolate Cake')
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')

print()
pos.print_current_money()

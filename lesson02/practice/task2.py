class Store:

    total_amount = 0

    def __init__(self, name_store, amount_sold_goods=0):
        self.name_store = name_store
        self.amount_sold_goods = amount_sold_goods

    def sold(self,name_goods):
        print(f'Магазин {self.name_store} продал {name_goods}')
        Store.total_amount += 1
        self.amount_sold_goods += 1
        print(f'В магазине {self.name_store} же продали {self.amount_sold_goods} товаров')
        print(f'Общее количество товаров проданных всеми магазинами {Store.total_amount}')
        print()

store1 = Store('Березка')
store2 = Store('Солнышко')
store3 = Store('Чайка')

store1.sold('Ручка')
store2.sold('Шляпа')
store1.sold('Шарф')
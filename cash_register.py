
import random

class CashRegister:
    
    DEFAULT_TAX = 0.05 
    
    def __init__(self, cashier_name):
        self._items = {'name':{},
                       'subtotal': 0
                       }
        self._cashier_id = random.randint(1002,4000)
        self._cashier_name = cashier_name
        
    
    #method to get list of products in current purchase
    @property
    def get_items(self):
        print(self._items)
        return self._items
    
    #method to remove a product from a purchase
    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)

    #Products
    def roti_skins(self, quantity=1, price='6.00', item='roti_skins'):
        if self._items['name'].get(item):
            #add to quantity
            self._items['name'][item] += quantity
            
            #Add to current price
            self._subtotal_before_taxes(price, self._items['name'][item] )
        else:
            self._subtotal = float(price)
            self._items['name'][item] = quantity
        return self
            
    
    def curry_goat(self, quantity=1, price='10.00', item='curry_goat'):
        if self._items['name'].get(item):
            #add to quantity
            self._items['name'][item] += quantity
            
            #Add to current price
            self._subtotal_before_taxes(price, self._items['name'][item] )
        else:
            self._subtotal = float(price)
            self._items['name'][item] = quantity
        return self
            
    
    def curry_chicken(self, quantity=1, price='8.00', item='curry_chicken'):
        if self._items['name'].get(item):
            #add to quantity
            self._items['name'][item] += quantity
            
            #Add to current price
            self._subtotal_before_taxes(price, self._items['name'][item] )
        else:
            self._subtotal = float(price)
            self._items['name'][item] = quantity
        return self


    def show_list_of_items(self):
        print('Current items ready for purchase:')
        for item in self._items['name'].keys():
            print(f"{self._items['name'][item]} x {item}")
        return self
            
                    
    def _subtotal_before_taxes(self, item_price, quantity ):
        self._items['subtotal'] += float(item_price) * quantity
        return self
    
    def subtotal_after_taxes(self):
        self._items['subtotal'] = (self._items['subtotal'] * CashRegister.DEFAULT_TAX) + self._items['subtotal']
        print(f"Subtotal: ${self._items['subtotal']}0")
        print(f"Your Cashier For Today: {self._cashier_name}-ID#: {self._cashier_id}")
    
    def clear_items(self):
        pass
    

    
    
jamila = CashRegister('Jamila')


jamila.roti_skins() \
    .roti_skins() \
    .curry_chicken() \
    .curry_chicken() \
    .curry_chicken() \
    .curry_goat() \
    .curry_chicken() \
    .show_list_of_items() \
    .subtotal_after_taxes() \



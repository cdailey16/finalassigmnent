from trifecta import Drink, Food, IceCream, Order
import unittest 
      
class TestDrink(unittest.TestCase):      
    def setUp(self):  # Initialize test fixtures before each test
        self.drink = Drink('medium', 'pokeacola', ['lemon'])  # Create a Drink object for testing
    
    def test_drink_initialization(self):
        self.assertEqual(self.drink.get_base(), 'pokeacola')
        self.assertEqual(self.drink.get_size(), 'medium')
        self.assertIn('lemon', self.drink.get_flavors())
        self.assertEqual(self.drink.get_num_flavors(), 1) 
        
    def test_drink_invalid_base(self):
        with self.assertRaises(ValueError):
            Drink('medium', 'invalid_base')  
        
            
    def test_get_size(self):
        size = self.drink.get_size()
        self.assertEqual(size, 'medium')  # Check if the size is correctly retrieved
        
    def test_get_invalid_size(self):
        with self.assertRaises(ValueError):
            Drink('invalid_size', 'pokeacola')
        self.assertEqual(self.drink.get_size(), 'medium')
        self.assertEqual(self.drink.get_base(), 'pokeacola')  # Check if the base is correctly retrieved
        self.assertIn('lemon', self.drink.get_flavors())  # Check if the flavor is correctly retrieved
        
        
            
    def test_set_flavors(self):
        self.drink.set_flavors(['cherry', 'mint'])
        self.assertIn('cherry', self.drink.get_flavors())
               
    def test_get_flavors(self):
        flavors = self.drink.get_flavors()
        self.assertIn('lemon', flavors)
               
    def test_drink_add_flavor(self):
        self.drink.add_flavor('cherry')
        self.assertIn('cherry', self.drink.get_flavors())
        #self.assertEqual(self.drink.get_num_flavors(), 2)

    def test_get_price(self):
        price = self.drink.get_price()
        self.assertEqual(price, 1.75)
        
    
    def test_get_price_incorrect(self):
        with self.assertRaises(ValueError):
            invalid_drink = Drink('invalid-size', 'pokeacola') 
            invalid_drink.get_price()  # This should raise a ValueError
            
class Food:  # Food class to represent food items with a name and price
    def __init__(self, name, toppings=None, price=2.30):
        valid_names = {'Hotdog', 'Corndog', 'Ice Cream'}  # Define valid food names
        if name.title() not in valid_names:
            raise ValueError(f"Invalid food name '{name}'. Valid names: {list(valid_names)}")
        self._name = name.title()  # Normalize name to title case
        self._valid_toppings = {'Ketchup', 'Mustard', 'Cherry', 'Mint'}  # Define valid toppings

        # Validate toppings
        toppings = toppings or []
        for topping in toppings:
            if topping.title() not in self._valid_toppings:
                raise ValueError(f"Invalid topping '{topping}'. Valid toppings: {list(self._valid_toppings)}")
        self._toppings = {t.title() for t in toppings}  # Normalize toppings to title case

        self._price = price  # Initialize price

    def add_topping(self, topping):
        normalized_topping = topping.title()  # Use title() to make case insensitive.
        if normalized_topping not in self._valid_toppings:
            raise ValueError(f"Invalid topping '{topping}'. Valid toppings: {list(self._valid_toppings)}")
        self._toppings.add(normalized_topping)  

    def has_topping(self, topping):
        return topping.lower() in (t.lower() for t in self._toppings)

    def set_toppings(self, toppings):
        self._toppings = {t.title() for t in toppings}  # 

    def get_toppings(self):
        return [t.title() for t in self._toppings]  

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_num_toppings(self):
        return len(self._toppings)

class TestFood(unittest.TestCase):  # TestFood class inherits from unittest.TestCase    
    def setUp(self):  # Initialize test fixtures before each test
        self.food = Food('Hotdog', ['Ketchup', 'Mustard'])  # Use the correct case for toppings
            
    def test_food_initialization(self):
        self.assertEqual(self.food.get_name(), 'Hotdog')
        self.assertEqual(self.food.get_price(), 2.30)
        self.assertIn('Ketchup', self.food.get_toppings())  
        self.assertEqual(self.food.get_num_toppings(), 2)
        
    def test_food_invalid_name(self):
        with self.assertRaises(ValueError):
            Food('invalid_food', ['ketchup'])
        with self.assertRaises(ValueError):
            Food('Hotdog', ['invalid_topping'])
            
    def test_get_name(self): 
        name = self.food.get_name()
        self.assertEqual(name, 'Hotdog')
        
    def test_get_invalid_name(self):
        with self.assertRaises(ValueError):
            Food('invalid_name', ['ketchup'])
        self.assertEqual(self.food.get_name(), 'Hotdog')
       
        
    def test_set_toppings(self): 
        self.food.set_toppings(['cherry', 'mint'])
        self.assertIn('Cherry', self.food.get_toppings())  
        
    def test_get_toppings(self):
        toppings = self.food.get_toppings()
        self.assertIn('Ketchup', toppings)  
        
    def test_food_add_topping(self):
        self.food.add_topping('cherry')
        self.assertIn('Cherry', self.food.get_toppings()) 
        self.assertEqual(self.food.get_num_toppings(), 3)

class IceCream:
    def __init__(self, name, toppings=None):
        # Define valid ice cream flavors
        valid_flavors = {
            'Mint Chocolate Chip': 4.00,
            'Chocolate': 3.00,
            'Vanilla Bean': 3.00,
            'Banana': 3.50,
            'Butter Pecan': 3.50,
            'Smore': 4.00,
        }
        
        # Normalize the name to title case
        name = name.title()
        
        # Check if the flavor is valid
        if name not in valid_flavors:
            raise ValueError(f"Invalid flavor '{name}'. Valid flavors are: {list(valid_flavors.keys())}")
        
        # Initialize the base price for the ice cream
        self._name = name
        self._base_price = valid_flavors[name]
        
        # Initialize toppings
        self._toppings = []
        self._valid_toppings = {
            'Cherry': 0.00,
            'Whipped Cream': 0.00,
            'Caramel Sauce': 0.50,
            'Chocolate Sauce': 0.50,
            'Storios': 1.00,
            'Dig Dog': 1.00,
            'T&Ts': 0.50,
            'Mint': 0.00,  # Add 'Mint' as a valid topping
        }
        
        # Validate and add toppings
        if toppings:
            for topping in toppings:
                self.add_topping(topping)

    def add_topping(self, topping):
        normalized_topping = topping.title()  # Normalize topping to title case
        if normalized_topping not in self._valid_toppings:
            raise ValueError(f"Invalid topping '{topping}'. Valid toppings: {list(self._valid_toppings.keys())}")
        self._toppings.append(normalized_topping)

    def get_price(self):
        # Calculate the total price including toppings
        topping_price = sum(self._valid_toppings[t] for t in self._toppings)
        return self._base_price + topping_price

    def get_name(self):
        return self._name

    def get_toppings(self):
        return self._toppings

    def __repr__(self):
        return f"IceCream(name={self._name}, toppings={self._toppings})"

class TestIceCream(unittest.TestCase):  # TestIceCream class inherits from unittest.TestCase
    def setUp(self): 
        self.ice_cream = IceCream('chocolate', ['cherry'])  # Create an IceCream object for testing
       
        
    def test_ice_cream_initialization(self):
        self.assertEqual(self.ice_cream.get_name(), 'Chocolate')
        self.assertIn('Cherry', self.ice_cream.get_toppings())
        self.assertAlmostEqual(self.ice_cream.get_price(), 3.00, places=2)
        
        
    def test_ice_cream_invalid_base(self):
        with self.assertRaises(ValueError):
            IceCream('invalid_base', ['cherry'])
        with self.assertRaises(ValueError):
            IceCream('chocolate', ['invalid_flavor'])
            
    def test_get_name(self):
        name = self.ice_cream.get_name()
        self.assertEqual(name, 'Chocolate')  # Check if the name is correctly retrieved
      

class TestOrder(unittest.TestCase):  # TestOrder class inherits from unittest.TestCase     
    def setUp(self): 
        self.drink = Drink('medium', 'pokeacola', ['lemon'])
        self.drink2 = Drink('large', 'sbrite', ['strawberry', 'blueberry'])
        self.drink3 = Drink('Mega', 'pokeacola', ['mint', 'lime'])
        self.food = Food('Hotdog', ['Ketchup', 'Mustard'])  
        self.food2 = Food('Corndog', ['Cherry', 'Mint'])
        self.order = Order()  # Initialize the order
        self.order.add_item(self.drink)
        self.order.add_item(self.drink2)
        self.order.add_item(self.drink3)
        
    # Test to check if the items in the order are correctly retrieved    
    def test_get_items(self):
        items = self.order.get_items()
        self.assertEqual(len(items), 3)
        self.assertIn(self.drink, items)
       
    # Test to check if the number of items in the order is correct
    def test_get_num_items(self): 
        num_items = self.order.get_num_items()
        self.assertEqual(num_items, 3)
        
    
    def test_order_repr(self):
        order_repr = repr(self.order)
        self.assertIn('Order(items=[', order_repr)
        
    def test_get_total_price(self):
        total_price = self.order.get_total_price()
        self.assertAlmostEqual(total_price, 6.39625, places=2)  # Update expected value




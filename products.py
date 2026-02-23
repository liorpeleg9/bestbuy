class Product:
    """
    Represents a product in the store.
    """

    def __init__(self, name, price, quantity):
        # Validate inputs
        if not isinstance(name, str) or not name.strip():
            raise Exception("Invalid name (cannot be empty).")
        if price < 0:
            raise Exception("Invalid price (cannot be negative).")
        if quantity < 0:
            raise Exception("Invalid quantity (cannot be negative).")

        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

        # A product is active as long as it has stock
        self.active = True
        if self.quantity == 0:
            self.active = False

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise Exception("Invalid quantity (cannot be negative).")

        self.quantity = int(quantity)

        # If we hit 0 stock, deactivate. Otherwise activate.
        if self.quantity == 0:
            self.active = False
        else:
            self.active = True

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        # Format price so 1450.0 prints as 1450
        price_str = f"{self.price:g}"
        print(f"{self.name}, Price: {price_str}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Invalid purchase quantity (must be > 0).")
        if not self.active:
            raise Exception("Product is not active.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price
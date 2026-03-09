class Store:
    """Represent a store that holds products."""

    def __init__(self, products):
        """Initialize the store with a list of products."""
        self.products = list(products)

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self):
        """Return the total quantity of all products in the store."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        """Return a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Process a shopping list and return the total order cost.

        This method is atomic:
        - It first sums quantities for duplicate products
        - Validates the whole order (no partial deductions)
        - Only then performs the buys
        """

        combined = {}
        for product, quantity in shopping_list:
            if quantity <= 0:
                raise Exception("Invalid purchase quantity (must be > 0).")
            if product not in self.products:
                raise Exception("Product is not in store.")
            combined[product] = combined.get(product, 0) + quantity

        for product, total_qty in combined.items():
            if not product.is_active():
                raise Exception("Product is not active.")
            if total_qty > product.get_quantity():
                raise Exception("Not enough quantity in stock.")

        total_price = 0.0
        for product, total_qty in combined.items():
            total_price += product.buy(total_qty)

        return total_price

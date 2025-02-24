import csv
import random

# Generate Product.csv
def generate_product_csv():
    with open("dummy/Product.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "price", "discount", "stock_remaining", "size", "images", "description", "materials", "weight", "dimension", "type_of", "categories"])
        for i in range(1, 6):
            writer.writerow([i, f"Product {i}", random.uniform(10, 500), random.randint(0, 50), random.randint(1, 100), random.choice(['S', 'M', 'L']),
                             f"https://example.com/image{i}.jpg", "Sample description", "cotton", random.randint(100, 1000), "10x10x10", random.choice(['P', 'S', 'B']), "Category A"])

def generate_product_listing_csv():
    with open("dummy/ProductListing.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "product_id", "quantity", "listing_price", "coupon_discount"])
        for i in range(1, 6):
            writer.writerow([i, i, random.randint(1, 50), random.randint(10, 500), random.randint(0, 30)])

def generate_review_csv():
    with open("dummy/Review.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "customer_id", "product_id", "description", "rating", "images"])
        for i in range(1, 6):
            writer.writerow([i, i, i, "Great product!", random.randint(1, 5), f"https://example.com/review{i}.jpg"])

def generate_sales_csv():
    with open("dummy/Sales.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "buyer_name", "price", "verified"])
        for i in range(1, 6):
            writer.writerow([i, f"Buyer {i}", random.randint(10, 500), random.choice([True, False])])

def generate_cart_csv():
    with open("dummy/Cart.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "paid", "product_id", "buyer_id", "product_listing_id", "sales_id"])
        for i in range(1, 6):
            writer.writerow([i, random.choice(['P', 'F', 'P']), i, i, i, i])

generate_product_csv()
generate_product_listing_csv()
generate_review_csv()
generate_sales_csv()
generate_cart_csv()

print("CSV files generated successfully!")
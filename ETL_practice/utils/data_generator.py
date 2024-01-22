import csv
import random


def generate_fake_data(file_path, num_records):
    products = ["Laptop", "Tablet", "Smartphone", "Desktop"]
    brands = ["Dell", "Apple", "HP", "Samsung", "Lenovo", "Asus", "Acer"]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Producto", "Marca", "Precio", "Cantidad"])

        for i in range(num_records):
            product = random.choice(products)
            brand = random.choice(brands)
            price = round(random.uniform(3800, 8050), 2)
            quantity = random.randint(1, 4)
            writer.writerow([i + 1, product, brand, price, quantity])


if __name__ == "__main__":
    generate_fake_data('tech_products.csv', 500)

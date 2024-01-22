import pandas as pd
from faker import Faker
import random
import numpy as np
import datetime

fake = Faker()

def generate_fake_data(file_path, num_records):
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)

    ids = range(1, num_records + 1)
    fechas = [fake.date_between(start_date=start_date, end_date=end_date) for _ in range(num_records)]
    clientes = [fake.name() for _ in range(num_records)]
    productos = np.random.choice(["Laptop", "Desktop", "Monitor"], size=num_records)
    marcas = np.random.choice(["Dell", "Apple", "HP", "Samsung", "Lenovo", "Asus", "Acer"], size=num_records)
    precios = np.random.uniform(3800, 8050, size=num_records)
    cantidades = np.random.randint(1, 4, size=num_records)
    totales = precios * cantidades

    df = pd.DataFrame({
        "ID Venta": ids,
        "Fecha": fechas,
        "Cliente": clientes,
        "Producto": productos,
        "Marca": marcas,
        "Precio": precios,
        "Cantidad": cantidades,
        "Total": totales
    })

    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    generate_fake_data("sales_data.csv", 100000)

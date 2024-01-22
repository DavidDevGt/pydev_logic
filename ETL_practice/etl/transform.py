import pandas as pd


class Transformer:
    @staticmethod
    def transform_data(file_path):
        # Load
        df = pd.read_csv(file_path)

        # Format
        df['Precio'] = df['Precio'].astype(float)
        df['Total'] = df['Total'].astype(float)
        df['Cantidad'] = df['Cantidad'].astype(int)

        # Analyze popular products and brands
        popularidad = df.groupby(
            ['Marca', 'Producto']).size().reset_index(name='Ventas')

        # Range of prices and average
        precios = df.groupby('Producto').agg(
            {'Precio': ['min', 'max', 'mean']}).reset_index()
        precios.columns = ['Producto', 'Precio_Min',
                           'Precio_Max', 'Precio_Promedio']

        # Predictions stock
        stock = df.groupby('Producto').agg({'Cantidad': 'sum'}).reset_index()
        stock.columns = ['Producto', 'Cantidad_Total_Vendida']

        return popularidad, precios, stock

FILE_PATH = "data/raw_data/sales_data.csv"

if __name__ == "__main__":
    popularidad, precios, stock = Transformer.transform_data(FILE_PATH)
    print("Popularidad por Marca y Producto:")
    print(popularidad)
    print("\nRango de Precios y Promedios:")
    print(precios)
    print("\nPredicción de Necesidades de Stock:")
    print(stock)

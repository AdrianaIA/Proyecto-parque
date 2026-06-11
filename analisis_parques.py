DRIVE_PATH = '/content/drive/MyDrive/Horizontes Senior/Tarea 2/'

df_csv_1 = pd.read_csv(
    DRIVE_PATH + "usos_parques_2024_2025.csv"
)

df_csv_2 = pd.read_csv(
    DRIVE_PATH + "usos_parques_2024_2025.2.csv"
)

df = pd.concat(
    [df_csv_1, df_csv_2],
    ignore_index=True
)


sedes = pd.read_excel(
    DRIVE_PATH + "codigos_sedes_producto.xlsx",
    sheet_name="Sedes"
)

productos = pd.read_excel(
    DRIVE_PATH + "codigos_sedes_producto.xlsx",
    sheet_name="Productos"
)

df.info()
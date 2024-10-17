import psycopg2
from psycopg2 import Error
conn = psycopg2.connect(
    "postgresql://neondb_owner:i7MqZnBdOl1e@ep-curly-fog-a5soxpav.us-east-2.aws.neon.tech/donapy?sslmode=require"
)

def main():
    try:
        # Establecer la conexión a la base de datos (asumiendo que ya está establecida)
        # connection = psycopg2.connect(
        #     user="tu_usuario",
        #     password="tu_contraseña",
        #     host="tu_host",
        #     port="tu_puerto",
        #     database="tu_base_de_datos"
        # )

        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()

        # Consulta SQL para seleccionar todos los registros de la tabla 'grupo_usuario'
        sql_query = "SELECT * FROM grupo_usuario;"

        # Ejecutar la consulta
        cursor.execute(sql_query)

        # Obtener los resultados de la consulta
        records = cursor.fetchall()
        print("Registros de la tabla 'grupo_usuario':")
        for row in records:
            print(row)

    except (Exception, Error) as error:
        print("Error al ejecutar la consulta:", error)

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        # connection.close()
        print("Consulta finalizada")

if __name__ == "__main__":
    main()

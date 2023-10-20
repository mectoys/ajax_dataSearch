from database.connectDB import get_connection


class model_dataSearch:

    @staticmethod
    def get_data(codigo):
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL_SELECT = "SELECT de_ubigeo FROM Flask_Ubigeo WHERE co_ubigeo= %s"
            value = (codigo,)
            cursor.execute(SQL_SELECT, value)
            result = cursor.fetchall()
            data = [row[0] for row in result]

        return data

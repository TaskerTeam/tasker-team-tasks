from datetime import datetime

class DateTimeUtils:
    @staticmethod
    def convert_to_string(date):
        """Converte um timestemp do PostgreSQL para uma string."""
        return date.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def convert_to_datetime(date_str):
        """Converte uma string para um timestemp do PostgreSQL."""
        return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
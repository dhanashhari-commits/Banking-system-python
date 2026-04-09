import csv
import os

class FileHandler:

    @staticmethod
    def ensure_file_exists(file_path, headers):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)

    @staticmethod
    def read_csv(file_path):
        if not os.path.exists(file_path):
            return []

        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader, None)
            return list(reader)

    @staticmethod
    def write_csv(file_path, headers, rows):
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(rows)

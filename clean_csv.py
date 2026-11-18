import csv
import sys

def clean_rows(rows):
    seen = set()
    cleaned = []
    for row in rows:
        norm = tuple(cell.strip() for cell in row)
        if norm not in seen and any(norm):
            seen.add(norm)
            cleaned.append(norm)
    return cleaned

if __name__ == "__main__":
    print("CSV Cleaner ready. Import clean_rows() or pass a file path.")

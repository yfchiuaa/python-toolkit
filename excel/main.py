import pandas as pd
import openpyxl
from typing import Tuple


def reader(input_file: str) -> pd.DataFrame:

    df = pd.read_excel(input_file)
    print(df.to_makrdown())

    return df


def writer() -> Tuple[openpyxl.workbook, openpyxl.worksheet]:

    workbook = openpyxl.Workbook()

    return workbook, workbook.active


def write(row: int, col: int, val: str, sheet: openpyxl.worksheet):

    sheet.cell(row=row, column=col).value = val


def save(output_file: str, workbook: openpyxl.workbook):

    workbook.save(output_file)


if __name__ == "__main__":

    input_file = input("Please input your excel file")
    data = reader(input_file)

    workbook, sheet = writer()
    write(0, 0, "test", sheet)
    save("output_file.excel", workbook)

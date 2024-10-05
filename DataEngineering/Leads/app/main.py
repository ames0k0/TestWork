import csv
import json
from datetime import datetime
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Generator
from urllib.parse import urlparse

import pandas
from prefect import flow, task


@task(log_prints=True)
def notify_via_tgbot(
        task_name: str, input_filename: Path, output_filename: Path
):
    print(
        f"Task: {task_name}, has been finished!\n"
        f"InputFile: {input_filename}\n"
        f"OutputFile: {output_filename}"
    )


@task(
    retries=2,          # Требования .4
    log_prints=True,
)
def make_an_api_request_and_process(data_url: str) -> dict:
    """ Returns the processed data or empty
    """
    result_data = {}
    # NOTE: not catching an errors
    data_frames = pandas.read_html(data_url, encoding="utf-8")
    if not data_frames:
        return result_data

    # XXX: first table
    for key, values in data_frames[0].items():
        result_data[key] = list(values)

    return result_data


def generate_output_filename() -> Path:
    filename = TASK_NAME + datetime.now().strftime(" - %Y-%m-%d %H-%M.json")
    filepath = CSV_FILEPATH.parent / filename
    return filepath


@task(log_prints=True)
def save_the_processed_data(data: dict) -> Path:
    """ Returns the filepath
    """
    output_filepath = generate_output_filename()
    print(data)

    with open(output_filepath, "w", encoding="utf-8") as ftw:
        json.dump(data, ftw, ensure_ascii=False)

    return output_filepath


@task(log_prints=True)
def load_csv_file(
        fieldnames: Iterable | None = None
) -> Generator[tuple[str, str], None, None]:
    """ Yields `data_title`, `data_url`
    """
    if fieldnames is None:
        fieldnames = ("Файл", "Ссылка")

    with open(CSV_FILEPATH, newline="", encoding="utf-8") as ftr:
        reader = csv.DictReader(ftr)
        for row in reader:
            file_title = row.get(fieldnames[0])
            file_url = row.get(fieldnames[1])
            # XXX: skip empty cells
            if not any((file_title, file_url)):
                continue
            url_diss = urlparse(file_url)
            # XXX: skip not valid urls
            if not any((url_diss.scheme, url_diss.netloc)):
                continue
            yield file_title, file_url


@flow
def process_csv_file():
    """ Processes the csv file
    """
    result_data = defaultdict(dict)

    for data_title, data_url in load_csv_file():
        processed_data = make_an_api_request_and_process(
            data_url
        )
        # NOTE: may rewrite the `result_data` for `data_title`
        result_data[data_title]["Ссылка"] = data_url
        result_data[data_title]["Данные"] = processed_data

    output_filename = save_the_processed_data(result_data)
    notify_via_tgbot(
        TASK_NAME, CSV_FILEPATH, output_filename
    )


if __name__ == "__main__":
    TASK_NAME = "CSV File Processor"
    CSV_FILEPATH = Path('./data/stock-data.csv')

    if not CSV_FILEPATH.exists():
        raise FileNotFoundError(CSV_FILEPATH)

    process_csv_file.serve(name=TASK_NAME)

import json
import pathlib


def read_json(file_path):
    path = pathlib.Path(file_path)
    with path.open(encoding="utf-8") as file:
        return json.load(file)

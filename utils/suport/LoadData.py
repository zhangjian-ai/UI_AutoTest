import os

from utils import BASE_DIR
from utils.operation.file import load_json


class LoadData:
    Data = dict()

    @classmethod
    def load_local(cls):
        path = os.path.join(BASE_DIR, "DataSource")

        for path, _, files in os.walk(path):
            for file in files:
                # 加载json文件数据
                if file.endswith(".json"):
                    data = load_json(os.path.join(path, file))
                    cls.Data[file.split(".", 1)[0]] = data

# -*- coding: utf-8 -*-
import pytoml


# 配置加载
class ConfigClass:
    def __init__(self) -> None:
        self._path = ""
        self._config = {}
        self._name = "Config加载"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        self._name = value

    def load(self, path: str) -> None:
        try:
            self._path = path
            with open(path, "r") as f:
                self._config = pytoml.load(f)
        except Exception as e:
            print(f"Error: {e}")

    def getVul(self, key: str) -> str:
        try:
            temp = self._config
            key_list = key.split(".")
            for i in key_list[:]:
                temp = temp[i]
            return temp
        except:
            return ""

# -*- coding: utf-8 -*-
# 初始化模块

from conf import config

class InitClass():

    def __init__(self) -> None:
        self._config = config.ConfigClass()
        self._config.load(".\conf\config.toml")


    @property
    def Config(self) -> config.ConfigClass:
        return self._config

    @property
    def MysqlConfig(self) -> dict[any, str]:
        return self._config.getVul("app.store.mysql")


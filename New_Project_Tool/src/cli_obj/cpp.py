# cpp_proj.py

from src.cli_obj._base import CliBase


class CppProj(CliBase):
    def __init__(self, path):
        CliBase.__init__(self, _path=path)

    def create(self, path: str, *args):
        pass

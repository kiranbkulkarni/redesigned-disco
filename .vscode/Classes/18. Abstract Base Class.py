from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already Open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already Closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading Data from network stream")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")


stream = MemoryStream()
# stream.open()

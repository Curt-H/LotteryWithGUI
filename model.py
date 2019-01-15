import json


class Employee(object):
    def __init__(self, meta: list):
        self.id = meta[0]
        self.name = meta[1]
        self.depart = meta[2]

    def __repr__(self):
        
        return result

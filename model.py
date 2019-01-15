import json
import os

from utils import log


def get_data(fname='list.csv'):
    fn = fname
    items = []
    with open(fn, 'r', encoding='utf-8-sig') as f:
        item = csv.reader(f)
        items.append(item)
    return items


def load(filename='temp.json'):
    fn = filename

    log(os.path.exists(fn))

    if not os.path.exists(fn):
        with open(fn, 'w', encoding='utf-8'):
            data = ''
    else:
        if os.path.getsize(fn) == 0:
            data = ''
        else:
            with open(fn, 'r', encoding='utf-8') as f:
                data = json.load(f)
                log(f'Load File {fn}\n[{data}]')

    return data


def save(data, filename='temp.json'):
    fn = filename
    d = data
    with open(fn, 'w+', encoding='utf-8') as f:
        json.dump(d, f)
    log(f'successfully save data to {fn}')


class Employee(object):
    def __init__(self, meta: list):
        self.id = meta[0]
        self.name = meta[1]
        self.depart = meta[2]
        self.selected = False

    def __repr__(self):
        result = ''
        for key, value in self.__dict__.items():
            result += ' '.join([key, value]) + '\n'
        return result

    @classmethod
    def new(cls):
        es = []
        items = get_data()
        for i in items:
            e = cls(i)
            es.append(e)
        es.save()


if __name__ == '__main__':
    b = load()
    log(b)

import hashlib
import os



GIT_DIR = '.pygit'

def init():
    os.makedirs(GIT_DIR)
    os.makedirs(f'{GIT_DIR}/objects')


def set_HEAD(oid):
    with open(f'{GIT_DIR}/HEAD', 'w') as f:
        f.write(oid)

def get_HEAD():
    if os.path.isfile(f'{GIT_DIR}/HEAD'):
        with open(f'{GIT_DIR}/HEAD') as f:
            return f.read().strip()

def hash_object(data, type_='blob'):
    obj = type_.encode() + b'\x00' + data
    oid = hashlib.sha1(obj).hexdigest()
    with open(f'{GIT_DIR}/objects/{oid}', 'wb') as out:
        out.write(obj)
    return oid


def get_object(oid, expected='blob'):
    with open(f'{GIT_DIR}/objects/{oid}', 'rb') as f:
        obj = f.read()

    type_, _, content = obj.partition(b'\x00')
    type_ = type_.decode()

    if expected is not None:
        assert type_ == expected, f'Expected {expected!r} object, got {type_!r}'
    return content

def update_ref(ref, oid):
    ref_path = f'{GIT_DIR}/{ref}'
    os.makedirs(os.path.dirname(ref_path), exist_ok=True)
    with open(ref_path, 'w') as f:
        f.write(oid)
    


def get_ref(ref):
    ref_path = f'{GIT_DIR}/{ref}'
    if os.path.isfile(ref_path):
        with open(ref_path) as f:
            return f.read().strip()
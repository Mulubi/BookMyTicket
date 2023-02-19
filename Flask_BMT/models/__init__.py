''' Initializes the models package '''
from os import getenv


storage_type = getenv("BMT_TYPE_STORAGE")

if storage_type == "db":
    from .engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()

from orator import Model, SoftDeletes
from kink import di

Model.set_connection_resolver(di["db"])


class User(Model, SoftDeletes):
    __table__ = "users"
    __hidden__=["hash", 'salt']
    # __primary_key__="id"

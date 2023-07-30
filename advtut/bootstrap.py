from fastapi import Security
import yaml
from kink import di
from orator import DatabaseManager
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer, JwtRefreshBearer
from datetime import timedelta

def bootstrap():

    with open("etc/config.yaml", 'r') as F:
        config = yaml.safe_load(F)
        # print("config: ", config)
        di["config"] = config

        db = DatabaseManager(di["config"]["databases"])
        di["db"] = db 
    
    di["access_security"] = JwtAccessBearer(secret_key=config["SECRET_KEY"],
                                            access_expires_delta=timedelta(minutes=int(config["ACCESS_TOKEN_EXPIRE_MINUTES"])),
                                            auto_error=True)
    di["refresh_security"] = JwtRefreshBearer(
        secret_key=config["SECRET_KEY"],
        refresh_expires_delta=timedelta(minutes=2*int(config["ACCESS_TOKEN_EXPIRE_MINUTES"])),
        auto_error=True
    )

    di["security_access_token"] = Security(di["access_security"])
    di["security_refresh_token"] = Security(di["refresh_security"])


    
    


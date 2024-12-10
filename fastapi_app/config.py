import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="fastapi_app",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="fastapi_app_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from fastapi_app.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export fastapi_app_KEY=value
export fastapi_app_KEY="@int 42"
export fastapi_app_KEY="@jinja {{ this.db.uri }}"
export fastapi_app_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
fastapi_app_ENV=production fastapi_app run
```

Read more on https://dynaconf.com
"""

## Configuration Provider

Provides configuration options to other providers. Implements the principle 'use first, define later'.

```py
import boto3
from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    s3_client_factory = providers.Factory(
        boto3.client,
        "s3",
        aws_access_key_id=config.aws.access_key_id,
        aws_secret_access_key=config.aws.secret_access_key,
    )


if __name__ == "__main__":
    container = Container()
    container.config.from_dict(
        {
            "aws": {
                 "access_key_id": "KEY",
                 "secret_access_key": "SECRET",
             },
        },
    )
    s3_client = container.s3_client_factory()
```

## Loading

Can load from ini, yaml, json, pydantic, env, dict, value

```py
container.config.from_ini("./config.ini")
config = providers.Configuration(ini_files=["./config.ini"])

container.config.from_yaml("./config.yml")
config = providers.Configuration(yaml_files=["./config.yml"])

container.config.from_json("./config.json")
config = providers.Configuration(json_files=["./config.json"])

container.config.from_pydantic(Settings())
config = providers.Configuration(pydantic_settings=[Settings()])

container.config.from_dict(
    {
        "aws": {
                "access_key_id": "KEY",
                "secret_access_key": "SECRET",
            },
    },
)

# from env
container.config.aws.access_key_id.from_env("AWS_ACCESS_KEY_ID")
container.config.aws.secret_access_key.from_env("AWS_SECRET_ACCESS_KEY")
container.config.optional.from_env("UNDEFINED", "default_value")

# use as_ argument for type casting
container.config.api_key.from_env("API_KEY", as_=str, required=True)
container.config.sampling.from_env("SAMPLING_RATIO", as_=float, required=True)
container.config.timeout.from_env("TIMEOUT", as_=int, default=5)

# value
container.config.option1.from_value(date(2022, 3, 13))
```

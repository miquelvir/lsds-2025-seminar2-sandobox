from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/datanodes")
def datanodes():
    return {
        "datanodes": [
            {
                "host": "localhost",
                "port": 8001
            },
            {
                "host": "localhost",
                "port": 8002
            },
            {
                "host": "localhost",
                "port": 8003
            }
        ]
    }


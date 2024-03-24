from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI microservice"}


@app.get("/sample")
async def sampleData():
    return {
            "sub": "tarunkrishacc@gmail.com",
            "iss": "jaykrishco.com",
            "exp": 1708238626,
            "iat": 1708238526,
            "jti": "xyzid"
}

@app.get("/test")
async def sampleData():
    return {
            "sub": "tarunkrishacc@gmail.com",
            "iss": "jaykrishco.com",
            "exp": 1708238626,
            "iat": 1708238526,
            "jti": "xyzid"
}
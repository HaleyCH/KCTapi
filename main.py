from fastapi import FastAPI
import datetime
import argparse

app = FastAPI()


def parse_args():
    parser = argparse.ArgumentParser(description="KCT-api")
    parser.add_argument("--port", type=int, default=4999, help="--port int:port")
    args = parser.parse_args()
    return args


@app.get("/")
async def root():
    if datetime.date.weekday(datetime.date.today()) != 3:
        return {"message": "Not Thursday."}
    return {"message": "KFC Crazy Thursday V50."}


if __name__ == "__main__":
    import uvicorn

    args = parse_args()
    uvicorn.run(app, port=args.port)

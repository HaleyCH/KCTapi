from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/")
async def root():
    if datetime.date.weekday(datetime.date.today()) != 3:
        return {"message": "Not Thursday."}
    return {"message": "KFC Crazy Thursday V50."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)

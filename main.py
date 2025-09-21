from fastapi import FastAPI, Body, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/save-data", status_code=status.HTTP_204_NO_CONTENT)
def save_data(data: str = Body(embed=True)) -> None:
    with open('data.txt', 'a') as file:
        file.write(data+"\n")


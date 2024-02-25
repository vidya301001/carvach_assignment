from fastapi import FastAPI
#add import
import model
from router import router
from config import engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()

#define endpoint
@app.get("/")
async def home():
    return "Welcome Home"

app.include_router(router.router, prefix="/book", tags=["book"])


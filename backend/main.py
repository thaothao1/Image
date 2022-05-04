import uvicorn
from fastapi import FastAPI
from router.api import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug= True)
app.include_router(router)
origins=[
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_methods= ["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0" , port= 8000 , reload= False)
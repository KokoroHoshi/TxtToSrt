from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from io import BytesIO

from utils import split_text, generate_srt

app = FastAPI(title="TXT to SRT API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static/browser", html=True), name="static")

@app.get("/api/test")
def root():
    return {"msg":"HHW"}

@app.post("/api/txt-to-srt", response_class=PlainTextResponse)
async def convert_txt_to_srt(file: UploadFile = File(None), text: str = Form(None)):
    if file:
        content = await file.read()
        text_content = content.decode("utf-8")
    elif text:
        text_content = text
    else:
        return PlainTextResponse("No input provided", status_code=400)
    
    segments = split_text(text_content)
    srt_content = generate_srt(segments)

    return srt_content
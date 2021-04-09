from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def show_overview():
    html_content = """
    <html>
        <head>
            <title>Model Debug Status</title>
        </head>
        <body>
            <h1>Look ma! HTML2!</h1> 
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

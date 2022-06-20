import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})


def create_app():
    app = Starlette(
        debug=True,
        routes=[
            Route("/", homepage)
        ],
    )

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", port=9000, reload=True)

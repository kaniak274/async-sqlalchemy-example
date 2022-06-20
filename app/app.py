import uvicorn
from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from starlette.routing import Route

from .dto import Tutorial
from .service import (
    list_tutorials,
    save_tutorial,
)


class TutorialEndpoints(HTTPEndpoint):
    async def get(self, request):
        tutorials = list_tutorials()
        return JSONResponse([
            {
                "tutorial_id": tutorial.tutorial_id,
                "name": tutorial.name,
            }
            async for tutorial in tutorials
        ])


    async def post(self, request):
        data = await request.json()
        name = data["name"]
        tutorial = await save_tutorial(Tutorial(name=name))

        return JSONResponse({
            "tutorial_id": tutorial.tutorial_id,
            "name": tutorial.name,
        })


def create_app():
    app = Starlette(
        debug=True,
        routes=[
            Route("/", TutorialEndpoints),
        ],
    )

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", port=9000, reload=True)

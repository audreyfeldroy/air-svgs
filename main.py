import air
import importlib
from air_markdown import Markdown
from svgs import Air1ColorLogo, Air3ColorLogo
from fastapi import HTTPException
from fastapi import FastAPI
from pathlib import Path

app = air.Air()
api = FastAPI()

app.mount("/static", air.StaticFiles(directory="static"), name="static")


def nav():
    return air.Nav(
        air.A("Home", href="/"),
        air.A("Usage Policy", href="/usage-policy"),
        _style="border-bottom: 1px solid var(--muted-border-color); padding-bottom: 1rem; margin-bottom: 2rem;"
    )


def footer():
    return air.Footer(
        air.P(
            "© 2025 Feldroy. All rights reserved. ",
            air.A("Air", href="https://air.feldroy.com"),
            " • ",
            air.A("GitHub", href="https://github.com/feldroy/air-svgs")
        ),
        _style="text-align: center; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--muted-border-color); color: var(--muted-color);"
    )


def LogoCard(title: str, preview_component, downloads: list):
    return air.Div(
        air.H3(title, _style="margin-bottom: 1.5rem; font-weight: 500;"),
        preview_component,
        air.Div(
            *downloads,
            _style="display: flex; gap: 0.75rem; justify-content: center; margin-top: 1.5rem; flex-wrap: wrap;"
        ),
        _style="""
            padding: 2rem 1.5rem;
            border: 1px solid var(--muted-border-color);
            border-radius: 0.75rem;
            text-align: center;
            transition: box-shadow 0.2s ease;
            background: var(--card-background-color);
        """,
        _class="logo-card"
    )


@app.page
def index():
    return air.Html(
        air.Head(
            air.Meta(charset="utf-8"),
            air.Meta(name="viewport", content="width=device-width, initial-scale=1"),
            air.Title("Air Logos – SVG Assets"),
            air.Meta(name="description", content="Official SVG assets for the Air web framework. Download logos in various formats."),
            air.Link(href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css", rel="stylesheet"),
            air.Link(href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap", rel="stylesheet"),
            air.Link(href="/static/style.css", rel="stylesheet")
        ),
        air.Body(
            air.Main(
                air.Div(
                    nav(),
                    
                    # Hero Section
                    air.Section(
                        air.H1("Air Logos"),
                        air.P("Official SVG assets for the Air web framework."),
                        _class="hero"
                    ),
                    
                    # Logo Grid Section
                    air.Div(
                        LogoCard(
                            "1-Color",
                            air.Img(src="/static/air-deep-sky-blue.svg", alt="Air logo 1-color", width=200, height=200),
                            [
                                air.A("Download SVG", href="/static/air-deep-sky-blue.svg", download="air-logo-1color.svg", _class="btn-primary"),
                                air.A("Neon Variant", href="/static/air-neon.svg", download="air-logo-neon.svg", _class="secondary outline")
                            ]
                        ),
                        LogoCard(
                            "3-Color",
                            air.Img(src="/static/air-3color.svg", alt="Air logo 3-color", width=200, height=200),
                            [
                                air.A("Download SVG", href="/static/air-3color.svg", download="air-logo-3color.svg", _class="btn-primary")
                            ]
                        ),
                        _class="logo-grid"
                    ),

                    # Air Tag Components Section (kept for backward compatibility)
                    air.Div(
                        air.H3("Component Versions", _style="text-align: center; margin: 2rem 0 1rem 0;"),
                        LogoCard(
                            "1-Color Tag",
                            Air1ColorLogo(),
                            []
                        ),
                        LogoCard(
                            "3-Color Tag", 
                            Air3ColorLogo(),
                            []
                        ),
                        _class="logo-grid"
                    ),

                    # Usage Section
                    air.Section(
                        air.H2("Need something else?"),
                        air.P(
                            "Open an ",
                            air.A("issue on GitHub", href="https://github.com/feldroy/air-svgs/issues/new"),
                            " and we'll take a look."
                        ),
                        _class="usage-section"
                    ),
                    
                    footer(),
                    _class="container"
                )
            )
        )
    )


def layout(request: air.Request, *content):
    if not isinstance(request, air.Request):
        raise Exception('First arg of layout needs to be an air.Request')
    return air.layouts.picocss(
        nav(),
        *content,
        footer()
    )


@app.get('/{slug:path}')
def mdpage(request: air.Request, slug: str):
    path = Path(f"pages/{slug}.md")
    if path.exists():
        text = path.read_text()
        # TODO add fetching of page title from first H1 tag
        return layout(
            request, Markdown(text)
        )
    path = Path(f"pages/{slug}.py")
    if path.exists():
        module_name = f'pages.{slug.replace('/', '.')}'     
        mod = importlib.import_module(module_name)
        return layout(
            request, mod.render(request)
        )
    raise HTTPException(status_code=404)


if __name__ == "__main__":
    print("Run this with fastapi dev")

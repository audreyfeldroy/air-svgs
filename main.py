import air
import importlib
from air_markdown import Markdown
from fastapi import HTTPException
from pathlib import Path

app = air.Air()

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
    class_="logo-card"
    )


@app.page
def index():
    return air.Html(
        air.Head(
            air.Meta(charset="utf-8"),
            air.Meta(name="viewport", content="width=device-width, initial-scale=1"),
            air.Title("Air Logos – SVG Assets"),
            air.Meta(name="description", content="Official SVG assets for the Air web framework. Download logos in various formats."),
            # Minimal styling only — no external CSS framework
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
                        class_="hero"
                    ),
                    
                    # Core Logos Section
                    air.H2("Core Logos", _style="margin-top: 2rem;"),
                    air.Div(
                        LogoCard(
                            "Light Theme",
                            air.Img(src="/static/air.svg", alt="Air logo", width=200),
                            [
                                air.A("Download SVG", href="/static/air.svg", download="air.svg", class_="btn-primary")
                            ]
                        ),
                        LogoCard(
                            "Dark Theme",
                            air.Div(
                                air.Img(src="/static/air-dark.svg", alt="Air logo dark", width=200),
                                _style="background: #1a1a1a; padding: 1rem; border-radius: 0.5rem;"
                            ),
                            [
                                air.A("Download SVG", href="/static/air-dark.svg", download="air-dark.svg", class_="btn-primary")
                            ]
                        ),
                        class_="logo-grid"
                    ),

                    # Style Variants Section
                    air.H2("Style Variants", _style="margin-top: 2rem;"),
                    air.Div(
                        LogoCard(
                            "Gradient",
                            air.Img(src="/static/air-gradient.svg", alt="Air logo gradient", width=200),
                            [
                                air.A("Download", href="/static/air-gradient.svg", download="air-gradient.svg", class_="btn-primary")
                            ]
                        ),
                        LogoCard(
                            "Monochrome",
                            air.Img(src="/static/air-mono.svg", alt="Air logo mono", width=200),
                            [
                                air.A("Download", href="/static/air-mono.svg", download="air-mono.svg", class_="btn-primary")
                            ]
                        ),
                        LogoCard(
                            "Knockout",
                            air.Img(src="/static/air-knockout.svg", alt="Air logo knockout", width=200),
                            [
                                air.A("Download", href="/static/air-knockout.svg", download="air-knockout.svg", class_="btn-primary")
                            ]
                        ),
                        class_="logo-grid"
                    ),

                    # Animated Variants Section
                    air.H2("Animated", _style="margin-top: 2rem;"),
                    air.Div(
                        LogoCard(
                            "Pulse",
                            air.Img(src="/static/air-animated-pulse.svg", alt="Air logo pulse animation", width=200),
                            [
                                air.A("Download", href="/static/air-animated-pulse.svg", download="air-animated-pulse.svg", class_="btn-primary")
                            ]
                        ),
                        LogoCard(
                            "Float",
                            air.Img(src="/static/air-animated-float.svg", alt="Air logo float animation", width=200),
                            [
                                air.A("Download", href="/static/air-animated-float.svg", download="air-animated-float.svg", class_="btn-primary")
                            ]
                        ),
                        LogoCard(
                            "Spinner",
                            air.Img(src="/static/air-animated-spinner.svg", alt="Air logo spinner animation", width=200),
                            [
                                air.A("Download", href="/static/air-animated-spinner.svg", download="air-animated-spinner.svg", class_="btn-primary")
                            ]
                        ),
                        LogoCard(
                            "Shimmer",
                            air.Img(src="/static/air-animated-shimmer.svg", alt="Air logo shimmer animation", width=200),
                            [
                                air.A("Download", href="/static/air-animated-shimmer.svg", download="air-animated-shimmer.svg", class_="btn-primary")
                            ]
                        ),
                        class_="logo-grid"
                    ),

                    # Air Tag Components Section (kept for backward compatibility)
                    # air.Div(
                    #     air.H3("Component Versions", _style="text-align: center; margin: 2rem 0 1rem 0;"),
                    #     LogoCard(
                    #         "1-Color Tag",
                    #         Air1ColorLogo(),
                    #         []
                    #     ),
                    #     LogoCard(
                    #         "3-Color Tag", 
                    #         Air3ColorLogo(),
                    #         []
                    #     ),
                    #     class_="logo-grid"
                    # ),

                    # Usage Section
                    air.Section(
                        air.H2("Need something else?"),
                        air.P(
                            "Open an ",
                            air.A("issue on GitHub", href="https://github.com/feldroy/air-svgs/issues/new"),
                            " and we'll take a look."
                        ),
                        class_="usage-section"
                    ),
                    
                    footer(),
                    class_="container"
                )
            )
        )
    )


def layout(request: air.Request, *content):
    if not isinstance(request, air.Request):
        raise Exception('First arg of layout needs to be an air.Request')
    # Simple, framework-free layout that only includes our styles and font.
    return air.Html(
        air.Head(
            air.Meta(charset="utf-8"),
            air.Meta(name="viewport", content="width=device-width, initial-scale=1"),
            air.Title("Air Logos"),
            air.Link(href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap", rel="stylesheet"),
            air.Link(href="/static/style.css", rel="stylesheet"),
        ),
        air.Body(
            air.Main(
                air.Div(
                    nav(),
                    *content,
                    footer(),
                    class_="container"
                )
            )
        )
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

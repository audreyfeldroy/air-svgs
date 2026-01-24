# AGENTS.md

## Commands

**Development**: `uv run fastapi dev main.py --reload` or `just run`
**Test**: `just test` or `uv run pytest` (single test: `just test path/to/test.py::TestClass::test_method`)
**Format/Lint**: `just qa` (runs ruff format, ruff check, and type checking)
**Coverage**: `just test-coverage` or `just coverage-html` (opens HTML report)

## Architecture

- **Framework**: FastAPI web app using the Air framework (modern Python web components)
- **Structure**: Single-page app serving SVG logo assets for the Air framework
- **Components**: `main.py` (FastAPI app), `svgs.py` (SVG logo components), `pages/` (markdown content)
- **Static**: SVG files served from `/static/` directory
- **Layout**: Uses Air's PicoCSS layout system with custom styling for now, but wanting to move to no CSS framework and minimal styling.
 - **Layout**: Framework-free, minimal styling — the site no longer loads PicoCSS. A small, local stylesheet (`/static/style.css`) provides layout, grid, card, and button styles.

## Code Style

- **Python 3.13** minimum version
- **Imports**: Standard library first, third-party, then local imports
- **Formatting**: Uses Ruff formatter and linter (configured via justfile)
- **Types**: Uses type annotations, checked with `ty check`
- **Components**: Air framework component-based architecture (air.Div, air.H1, etc.)
- **Naming**: Snake_case for functions/variables, PascalCase for components
- **Dependencies**: Managed with uv package manager

## Project Structure

- Main application logic in `main.py` (FastAPI + Air integration)
- SVG components defined in `svgs.py` using Air's SVG models
- Static assets in `static/` directory
- Markdown pages in `pages/` directory, served dynamically via route handler

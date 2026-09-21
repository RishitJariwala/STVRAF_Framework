"""
Custom documentation pages with Vercel Web Analytics integration.
"""
from fastapi.responses import HTMLResponse


def get_swagger_ui_html_with_analytics(
    *,
    openapi_url: str,
    title: str,
    swagger_js_url: str = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
    swagger_css_url: str = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    swagger_favicon_url: str = "https://fastapi.tiangolo.com/img/favicon.png",
) -> HTMLResponse:
    """
    Custom Swagger UI HTML with Vercel Web Analytics injected.
    """
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link type="text/css" rel="stylesheet" href="{swagger_css_url}">
        <link rel="shortcut icon" href="{swagger_favicon_url}">
        <title>{title}</title>
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script src="{swagger_js_url}"></script>
        <script>
        const ui = SwaggerUIBundle({{
            url: '{openapi_url}',
            dom_id: '#swagger-ui',
            presets: [
                SwaggerUIBundle.presets.apis,
                SwaggerUIBundle.SwaggerUIStandalonePreset
            ],
            layout: "BaseLayout",
            deepLinking: true,
            showExtensions: true,
            showCommonExtensions: true,
            persistAuthorization: true
        }})
        </script>
        
        <!-- Vercel Web Analytics -->
        <script>
            window.va = window.va || function () {{ (window.vaq = window.vaq || []).push(arguments); }};
        </script>
        <script defer src="/_vercel/insights/script.js"></script>
    </body>
    </html>
    """
    return HTMLResponse(content=html)


def get_redoc_html_with_analytics(
    *,
    openapi_url: str,
    title: str,
    redoc_js_url: str = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js",
    redoc_favicon_url: str = "https://fastapi.tiangolo.com/img/favicon.png",
) -> HTMLResponse:
    """
    Custom ReDoc HTML with Vercel Web Analytics injected.
    """
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="shortcut icon" href="{redoc_favicon_url}">
        <style>
            body {{
                margin: 0;
                padding: 0;
            }}
        </style>
    </head>
    <body>
        <redoc spec-url="{openapi_url}"></redoc>
        <script src="{redoc_js_url}"></script>
        
        <!-- Vercel Web Analytics -->
        <script>
            window.va = window.va || function () {{ (window.vaq = window.vaq || []).push(arguments); }};
        </script>
        <script defer src="/_vercel/insights/script.js"></script>
    </body>
    </html>
    """
    return HTMLResponse(content=html)

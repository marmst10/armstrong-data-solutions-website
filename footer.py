import dash
from dash import html, dcc


def footer():
    return html.Footer(
        html.Div(
            [
                html.Hr(),
                dcc.Markdown("**Armstrong Data Solutions**"),
                dcc.Markdown("(770) 769-0030"),
                dcc.Markdown("connor@armstrongdatasolutions.com"),
                html.P(
                    [
                        html.Img(src=dash.get_asset_url("GitHub-Mark-32px.png")),
                        html.Span("   "),
                        html.A("GitHub Repository", href="https://github.com/marmst10/armstrong-data-solutions-website", target="_blank"),
                    ]
                ),
            ],
            style={"text-align": "center"},
            className="p-3",
        ),
    )

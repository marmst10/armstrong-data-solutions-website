import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# External stylesheet with custom CSS
# external_stylesheets = [dbc.themes.DARKLY, "/assets/styles.css"]

def footer(external_stylesheets):#
    return html.Div(
        # className="text-center", # <- here if d-flex is present html.hr is too short, if not then the card is on the left.
        className="footer",
        children=[
            html.Hr(style={"width": "100%"}),
            html.Footer(
                html.Div(
                    [
                        
                        dcc.Markdown("**Armstrong Data Solutions**", style={"font-size": "12px"}),
                        # dcc.Markdown("connor@armstrongdatasolutions.com"),
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Img(src=dash.get_asset_url("GitHub-Mark-32px.png"), style={"margin-right": "4px", "transform": "scale(0.6)"}),
                                    html.Span("   "),
                                    html.A("GitHub Repository", href="https://github.com/marmst10/armstrong-data-solutions-website", target="_blank", style={"color": "darkblue"}),
                                ]
                            ),
                            style={"background-color": "lightgray", "width": "fit-content", "padding": "0px", "height": "36px"},  # Set the background color of the card, "height": 30
                            className="d-flex justify-content-center mx-auto",
                        ),

                    ],
                    style={"text-align": "center"},
                    className="p-3",
                ),
            )
        ],
        # Apply the same external_stylesheets as in app.py
        # style={"height": "100%", "margin-top": "auto"},
        # external_stylesheets=external_stylesheets,
    )
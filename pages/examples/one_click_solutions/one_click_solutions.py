import warnings
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from card import card
from dash import html
import os
import dash_gif_component as Gif

warnings.simplefilter(action="ignore", category=FutureWarning)

dash.register_page(
    __name__,
    path="/examples/one-click-solutions",
    title="Armstrong Data Solutions - One-click Solutions",
    name="One-click Solutions",
    description="One-click Solutions Page",
)

text1 = dcc.Markdown(
    """
    This is the one-click solutions page
    """
)

# Create an Img component to display the GIF
gif_component = Gif.GifPlayer(
        gif="/assets/one-click-solutions2.gif",
        still='/assets/still-0.png'
    )
text2 = html.Div(
    dcc.Markdown(
    """
    #### Simple Software Tools
    
    Custom tools for your business can save valuable time and money.  
    """
    )
)
def layout():
    page = dbc.Container(html.Div(
        [
            html.H3("One-Click Solutions"),
            html.Hr(),

            dbc.Container(
            [        
                # dbc.Row(dbc.Col(card(text1, centered=True), width=12), align="center", className="mb-4"),
                dbc.Row(
                    [
                        # Wrap the card in an html.Div with custom CSS to set equal height
                        dbc.Col(dbc.Card(dbc.CardBody(text2),className="mh-100"), width=5,className="align-top"),
                        # Wrap the GifPlayer inside a card to maintain consistent height
                        dbc.Col(dbc.Card(dbc.CardBody(gif_component)), width=7, className = 'align-content-center'),
                    ],
                    justify="top",
                    className="mh-100"
                )
            ],
            class_name="mt-2",
            fluid="md",
            )
        ],
        style={"padding": "20px"}
    ))
    return page

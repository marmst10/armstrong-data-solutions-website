import warnings

import dash
from dash import dash_table, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from card import card
warnings.simplefilter(action="ignore", category=FutureWarning)

dash.register_page(
    __name__,
    path="/",
    title="Armstrong Data Solutions - Home Page",
    name="Home",
    description="Armstrong Data Solutions Website Home Page",
)

text1 = dcc.Markdown(
    """
    Looking for a smart solution? Armstrong Data Solutions can help your business.
    """
)
text2 = dcc.Markdown(
    """
    ##### Custom Software Tools

    - One-click solutions
    - Applications
    - Custom reports & visualizations
    """
)
text3 = dcc.Markdown(
    """
    ##### Automation
    
    - Automate repetitive tasks
    - Increase efficiency & profitability
    """
)
text4 = dcc.Markdown(
    """
    *Got questions? Get in touch for a free consultation*

    """
)

def layout():
    page = dbc.Container(
        [
            dbc.Row(dbc.Col(card(text1, centered=True), width=12), align="center",className="mb-4"),
            dbc.Row([
                dbc.Col(card(text2), width=6),
                dbc.Col(card(text3), width=6), 
                ],
                className="mb-4"
                ),
            dbc.Row(dbc.Col(card(text4, centered=True), width=12), align="center", className="mb-4")
        ],
        class_name="mt-2",
        fluid="md",
    )
    return page

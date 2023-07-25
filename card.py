import dash_bootstrap_components as dbc
from dash import html

def card(text, centered = False):
    if centered:
        card = dbc.Card(
            dbc.CardBody(
                [
                    html.Div(text, className='text-center')
                ]
            ),
            class_name="h-100"
        )
    else:
        card = dbc.Card(
            dbc.CardBody(
                [
                    html.Div(text)
                ]
            ),
            class_name="h-100"
        )
    return card
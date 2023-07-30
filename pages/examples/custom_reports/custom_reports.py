import warnings
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from card import card

warnings.simplefilter(action="ignore", category=FutureWarning)

dash.register_page(
    __name__,
    path="/examples/custom-reports",
    title="Armstrong Data Solutions - Custom Reports",
    name="Custom Reports",
    description="Custom Reports Page",
)

text1 = dcc.Markdown(
    """
    This is the custom reports page
    """
)

def layout():
    page = dbc.Container(
        [
            dbc.Row(dbc.Col(card(text1, centered=True), width=12), align="center",className="mb-4"),

        ],
        class_name="mt-2",
        fluid="md",
    )
    return page

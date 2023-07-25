import warnings
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from card import card

warnings.simplefilter(action="ignore", category=FutureWarning)

dash.register_page(
    __name__,
    path="/solutions/custom-visualizations",
    title="Armstrong Data Solutions - Custom Visualizations",
    name="Custom Visualizations",
    description="Custom Visualizations Page",
)

text1 = dcc.Markdown(
    """
    This is the custom visualizations page.
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

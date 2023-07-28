import warnings
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from card import card

warnings.simplefilter(action="ignore", category=FutureWarning)

dash.register_page(
    __name__,
    path="/contact",
    title="Armstrong Data Solutions - Contact",
    name="Contact",
    description="Contact Page",
)

text1 = dcc.Markdown("Click here to email **connor@armstrongdatasolutions.com**")

# Create the button content with image and text
button_content = dbc.Row(
    [
        dbc.Col(html.Img(src=dash.get_asset_url("mail2.png")), style={"margin": 0}),  # Remove the gutter
        dbc.Col(text1, className='text-nowrap', style={'display': 'flex'}),
    ]
)

# Create the email button with the button content
email_button = dbc.Button(
    button_content,
    href="mailto:connor@armstrongdatasolutions.com",
    style={'height': '40px'},  # Set a fixed height for the button
)

# Create the layout for the page
def layout():
    page = dbc.Container(
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(email_button),
                    className="h-100 d-flex justify-content-center",  # Added justify-content-center class
                ),
                width=12,
            ),
            className="mb-4",
        ),
        className="mt-2 d-flex justify-content-center",  # Added justify-content-center class
        fluid=True,
    )
    return page


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

table = html.Table(
    # Table contents
    [
        html.Tr([html.Td("Phone Number:", style={'text-align': 'right', 'padding': '10px', "font-size": "20px"}), html.Span("   "), html.Th("(770) 769-0030",style={"font-size": "20px"})]),
        html.Tr([html.Td("Email:", style={'text-align': 'right', 'padding': '10px', "font-size": "20px"}), html.Span("   "), html.Th("connor@armstrongdatasolutions.com",style={"font-size": "20px"})]),

    ],
    # Custom CSS styles for the table
    style={
        # 'border': '1px solid #ddd',  # Add a 1px gray border to the entire table
        'border-collapse': 'collapse',  # Collapse borders between cells
        'width': '100%',  # Make the table occupy the full width of the container
    },
)

# Create the layout for the page
def layout():
    page = dbc.Container(
        dbc.Row(
            dbc.Col(
                [
                    dbc.Row(
                        dbc.Card(
                            dbc.CardBody(
                                table
                            ),
                        # Added justify-content-center class
                        # style={'height': '60px'}
                        ), 
                        align="center",
                        className="mt-4 mb-4"
                    ),
                    dbc.Row(
                        dbc.Card(
                            dbc.CardBody(email_button, className="mb-2 mt-2"),
                            className="d-flex justify-content-center",  # Added justify-content-center class
                        ), 
                        align="center",
                        className="mb-4 mt-4"
                    ),


                ],
                width=12,
            ),
            className="mb-4",
        ),
        className="mt-2 d-flex justify-content-center",  # Added justify-content-center class
        fluid=True,
    )
    return page


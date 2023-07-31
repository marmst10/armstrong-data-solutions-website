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

text1 = html.Div(
    [
        dcc.Markdown(
            """
            ###### Does manually crunching data drive you nuts?
            """, 
            style={'text-align': 'center'}, className="mb-3"
        ),
        dcc.Markdown(
            """
            ###### Would you like to automate your data analysis?
            """, 
            style={'text-align': 'center'}, className="mb-3"
        ),
        dcc.Markdown(
            """
            ###### Would you like to outsource your data analysis?
            """, 
            style={'text-align': 'center'}, className="mb-4"
        ),
        dcc.Markdown(
            """
            ##### If any of these apply to you, **Armstrong Data Solutions** can help your business.
            """, 
            style={'text-align': 'center'}
        )
    ]
)

text2 = dcc.Markdown(
    """
    ##### **Custom Software Tools**

    Applications  
    Custom reports & visualizations  
    One-click solutions  
    """
)

text5 = dcc.Markdown(
    """
    ##### **Services**
    
    Outsource your Data Analysis  
    Automate repetitive tasks  
    Process Optimization  
    Experimental Design
    """
)
text4 = dcc.Markdown(                            
    """
        *Got questions? [Get in touch](/contact) for a free consultation*
    """, style={'text-align': 'center'}
)

def generate_card(content):
    homecard = dbc.Row(
        [
            dbc.Col(
                card(content, centered=True), 
                width={"size": 12, "offset": 0}, 
                xs=10, sm=10, md=6, lg=4, xl=4
            )
        ],
        justify="center",
        className="mb-5",
    )
    return homecard

def layout():
    page = html.Div(
        [
            dbc.Container(
                [
                    dbc.Row(dbc.Col(text1, align="center"), className="mb-4 mt-4"),
                ],
                class_name="mt-2",
                fluid="md",
                style={"padding": "0"},  # Add this style to remove container padding
            ),

            html.Hr(style={"width": "100%"}, className="mb-5"),

            dbc.Container(
                [
                    generate_card(text5),
                    generate_card(text2),
                ],
                fluid="md",
                style={"padding": "0"},  # Add this style to remove container padding
            ),

            html.Hr(style={"width": "100%"}, className="mt-5"),

            dbc.Container(
                [
                    dbc.Row(dbc.Col(text4, align="center"), style={"margin-bottom": "20"}),
                ],
                # class_name="mt-5",
                fluid="md",
                style={"padding": "0"},  # Add this style to remove container padding
            )
        ]
    )

    # # Add custom CSS to adjust the card width on mobile devices
    # custom_css = """
    # @media (max-width: 768px) {
    #     .custom-card-col {
    #         flex-basis: calc(100% - 20px) !important;
    #         max-width: calc(100% - 20px) !important;
    #     }
    # }
    # """
    # page = html.Div([page, html.Style(custom_css)])
    return page

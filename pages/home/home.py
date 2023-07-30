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
    ##### Looking for a smart solution? **Armstrong Data Solutions** can help your business.
    """, style={'text-align': 'center'}
)
text2 = dcc.Markdown(
    """
    ##### **Custom Software Tools**

    Applications  
    Custom reports & visualizations  
    One-click solutions  
    """
)
text3 = dcc.Markdown(
    """
    ##### **Automation**
    
    Automate repetitive tasks  
    Increase efficiency & profitability
    """
)
text5 = dcc.Markdown(
    """
    ##### **Services**
    
    Outsource your Data Analysis  
    Process Optimization  
    Experimental Design
    """
)
text4 = dcc.Markdown(                            
    """
        *Got questions? [Get in touch](/contact) for a free consultation*
    """, style={'text-align': 'center'}
)
# ,
    # 
def layout():
    page = dbc.Container(
        [
            dbc.Row(dbc.Col(text1, align="center"),className="mb-4 mt-4"),
            dbc.Row(dbc.Col(card(text2, centered=True), width=4), justify="center", className="mb-4"),
            dbc.Row(dbc.Col(card(text3, centered=True), width=4), justify="center", className="mb-4"),
            dbc.Row(dbc.Col(card(text5, centered=True), width=4), justify="center", className="mb-4"),
            dbc.Row(dbc.Col(text4, align="center"),style={"margin-bottom":"20"}),
        ],
        
        class_name="mt-2",
        fluid="md",
    )
    return page

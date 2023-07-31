import dash
import dash_bootstrap_components as dbc
from dash import html
links = dbc.Row(
    dbc.Col(
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Home", href="/", id='home-link',), style={"padding-right":"10px"}),
                dbc.NavItem(dbc.NavLink("Contact", href="/contact", id='contact-link'), style={"padding-right":"10px"}),
                # dbc.NavItem(dbc.NavLink("Solutions", href="/solutions", id='solutions-link')),
                
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("One-click Solutions", href="/examples/one-click-solutions", id='one-click-solutions-link'),
                        # dbc.DropdownMenuItem("Applications", href="/examples/applications", id='applications-link'),
                        # dbc.DropdownMenuItem("Custom Reports", href="/examples/custom-reports", id='custom-reports-link'),
                        # dbc.DropdownMenuItem("Custom Visualizations", href="/examples/custom-visualizations", id='custom-visualizations-link'),
                        # dbc.DropdownMenuItem("Task Automation", href="/examples/task-automation", id='task-automation-link'),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Examples",
                )
            ],
            navbar=True,
        ),
        width=True
    )
)
              
def create_navbar(external_stylesheets):
    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src="/assets/icon5.png", height="40px"), style={"padding-right":"5px"}),
                            dbc.Col(dbc.NavbarBrand("Armstrong Data Solutions", className="ms-2"), style={"padding-right":"10px"}),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="/",
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    links,
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ]
        ),
        color="dark",
        dark=True,
    )
    return navbar
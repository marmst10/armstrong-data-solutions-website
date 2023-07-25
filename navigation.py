import dash
import dash_bootstrap_components as dbc
from dash import html
links = dbc.Row(
    dbc.Col(
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Home", href="/", id='home-link')),
                dbc.NavItem(dbc.NavLink("Contact", href="/contact", id='contact-link')),
                # dbc.NavItem(dbc.NavLink("Solutions", href="/solutions", id='solutions-link')),
                
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("One-click Solutions", href="/solutions/one-click-solutions", id='one-click-solutions-link'),
                        dbc.DropdownMenuItem("Applications", href="/solutions/applications", id='applications-link'),
                        dbc.DropdownMenuItem("Custom Reports", href="/solutions/custom-reports", id='custom-reports-link'),
                        dbc.DropdownMenuItem("Custom Visualizations", href="/solutions/custom-visualizations", id='custom-visualizations-link'),
                        dbc.DropdownMenuItem("Task Automation", href="/solutions/task-automation", id='task-automation-link'),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Solutions",
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
                            dbc.Col(html.Img(src="/assets/icon5.png", height="50px")),
                            dbc.Col(dbc.NavbarBrand("Armstrong Data Solutions", className="ms-2")),
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

# navbar = dbc.NavbarSimple(
#     children=[
#         dbc.Row(
#             [
#                 dbc.Col(
#                     html.Span(
#                         [html.Img(src="/assets/icon.png", height="30px", className="mr-2"), "Armstrong Data Solutions"],
#                         className="navbar-brand"
#                     ),
#                     width = "auto"
#                 ),
#                 dbc.Col(
#                     dbc.Nav(
#                         [
#                             dbc.NavItem(dbc.NavLink("Home", href="/")),
#                             dbc.NavItem(dbc.NavLink("Solutions", href="/solutions")),
#                             dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
#                             dbc.DropdownMenu(
#                                 children=[
#                                     dbc.DropdownMenuItem("Example 1", href="/examples/example1"),
#                                     dbc.DropdownMenuItem("Example 2", href="/examples/example2"),
#                                 ],
#                                 nav=True,
#                                 in_navbar=True,
#                                 label="Examples",
#                             )
#                         ],
#                         navbar=True,
#                     ),
#                     width=True
#                 ),
#             ],
#             align="center",  # Align the content of the row to the center
#         ),
#     ],
#     brand_href="/",
#     color="primary",
#     dark=True,
# )
import warnings

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import plotly.io as pio

import footer
from navigation import create_navbar

warnings.simplefilter(action="ignore", category=FutureWarning)

pio.templates.default = "plotly_dark"

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
external_stylesheets=[dbc.themes.DARKLY, "/assets/styles.css"]
app = dash.Dash(
    __name__,
    use_pages=True,
    update_title="Loading website ...",
    external_stylesheets=external_stylesheets,
    # suppress_callback_exceptions=True
)
server = app.server
navbar = create_navbar(external_stylesheets)

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        dcc.Store(id="store"), 
        navbar, 
        dash.page_container, 
        footer.footer(),
        html.Div(id='page-content'),
    ]
)

# Callback to update the active link based on the current URL
@app.callback(
    Output('home-link', 'active'),
    Output('contact-link', 'active'),
    Output('one-click-solutions-link', 'active'),
    Output('applications-link', 'active'),
    Output('custom-reports-link', 'active'),
    Output('custom-visualizations-link', 'active'),
    Output('task-automation-link', 'active'),
    Input('url', 'pathname')
)
def update_active_links(pathname):
    home_active = False
    contact_active = False
    one_click_solutions_active = False
    applications_active = False
    custom_reports_active = False
    custom_visualizations_active = False
    task_automation_active = False

    if pathname == '/':
        home_active = True
    elif pathname == '/contact':
        contact_active = True
    elif pathname == '/solutions/one-click-solutions':
        one_click_solutions_active = True
    elif pathname == '/solutions/applications':
        applications_active = True
    elif pathname == '/solutions/custom-reports':
        custom_reports_active = True
    elif pathname == '/solutions/custom-visualizations':
        custom_visualizations_active = True
    elif pathname == '/solutions/task-automation':
        task_automation_active = True

    return home_active, contact_active, one_click_solutions_active, applications_active, custom_reports_active, custom_visualizations_active, task_automation_active

app.clientside_callback(
    """
    function(trigger) {
        //  can use any prop to trigger this callback - we just want to store the info on startup
        const inner_width  = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
        const inner_height = window.innerHeight|| document.documentElement.clientHeight|| document.body.clientHeight;
        const screenInfo = {height :screen.height, width: screen.width, in_width: inner_width, in_height: inner_height};

        return screenInfo
    }
    """,
    Output("store", "data"),
    Input("store", "data"),
)


if __name__ == "__main__":
    app.run_server(debug=True, port=8040)
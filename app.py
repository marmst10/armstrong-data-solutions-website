import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.io as pio
import footer
from navigation import create_navbar

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
        html.Div(
            [
                dcc.Location(id='url', refresh=False),
                # dcc.Store(id="store"), 
                navbar, 
                dash.page_container, 
                # html.Div(id='content'),
                # external_stylesheets
                
                # html.Div(id='dummy', style={'display': 'none'})
            ]#, className="h-100"
            # id="global"#, 
            
        ),
        html.Div(
            footer.footer(external_stylesheets)
        )
    ], className="h-100"#style={"min-height": "100vh"}
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
    elif pathname == '/examples/one-click-solutions':
        one_click_solutions_active = True
    elif pathname == '/examples/applications':
        applications_active = True
    elif pathname == '/examples/custom-reports':
        custom_reports_active = True
    elif pathname == '/examples/custom-visualizations':
        custom_visualizations_active = True
    elif pathname == '/examples/task-automation':
        task_automation_active = True

    return home_active, contact_active, one_click_solutions_active, applications_active, custom_reports_active, custom_visualizations_active, task_automation_active

# Define the callback to update the encrypted phone number
@app.callback(Output('encrypted-phone', 'children'), [Input('phone-store', 'data')])
def update_encrypted_phone(encrypted_phone):
    return encrypted_phone


if __name__ == "__main__":
    # app.run_server(debug=True, port=8040)
    app.run_server(debug=False, host="0.0.0.0", port=8080)
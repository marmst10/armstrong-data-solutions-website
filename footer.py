# import dash
from dash import html, dcc
# import dash_bootstrap_components as dbc

def footer(external_stylesheets):
    return html.Footer(
        dcc.Markdown(
            
            "**Armstrong Data Solutions**",
            className="footer",
            style={
                "font-size": "12px", 
                "margin":"0", 
                "padding-bottom":"30", 
                "background-color":"#383434", 
                "text-align": "center"
                }
        )
    )

#     html.Hr(style={"width": "100%"}),
#     dbc.Card(
#         dbc.CardBody(
#             [
#                 html.Img(src=dash.get_asset_url("GitHub-Mark-32px.png"), style={"margin-right": "4px", "transform": "scale(0.6)"}),
#                 html.Span("   "),
#                 html.A("GitHub Repository", href="https://github.com/marmst10/armstrong-data-solutions-website", target="_blank", style={"color": "darkblue"}),
#             ]
#         ),
#         style={"background-color": "lightgray", "width": "fit-content", "padding": "0px", "height": "36px"},
#         className="d-flex justify-content-center mx-auto",
#     ),
# ],

                
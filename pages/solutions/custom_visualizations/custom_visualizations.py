import warnings
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from card import card
from dash import html
import plotly.express as px
import pandas as pd

warnings.simplefilter(action="ignore", category=FutureWarning)

dash.register_page(
    __name__,
    path="/solutions/custom-visualizations",
    title="Armstrong Data Solutions - Custom Visualizations",
    name="Custom Visualizations",
    description="Custom Visualizations Page",
)

# Sample data for the timeline
timeline_data = pd.DataFrame({
    'Event': ['Event 1', 'Event 2', 'Event 3'],
    'Start': ['2023-07-01', '2023-08-15', '2023-09-20'],
    'End': ['2023-08-15', '2023-09-20', '2023-10-20']
})

# Create the timeline chart using Plotly Express
timeline_chart = dcc.Graph(
    figure=px.timeline(timeline_data, x_start='Start', x_end='End', y='Event', title='Timeline Visualization')
)

# Sample data for the scatter plot
data = px.data.iris()

# text1 = dcc.Markdown(
#     """
#     This is the custom visualizations page.
#     """
# )

# Create the scatter plot using Plotly Express
scatter_plot = dcc.Graph(
    figure=px.scatter(data, x="sepal_width", y="sepal_length", color="species",
                      title="Scatter Plot of Sepal Width vs. Sepal Length")
)

# Sample data for the bar chart
bar_data = px.data.tips()

# Define the order of days for the bar chart
days_order = ['thur', 'fri', 'sat', 'sun']

# Convert the 'day' values to lowercase for consistency
bar_data['day'] = bar_data['day'].str.lower()

# Set the 'day' column as ordered categorical with specified categories
bar_data['day'] = pd.Categorical(bar_data['day'], categories=days_order, ordered=True)

# Group the data by 'day' and calculate the sum of 'total_bill' for each group
grouped_data = bar_data.groupby(['day', 'sex']).agg({'total_bill': 'sum'}).reset_index()

# Create the bar chart using Plotly Express with the aggregated data
bar_chart = dcc.Graph(
    figure=px.bar(grouped_data, x="day", y="total_bill", color='sex', barmode='group',
                  title="Bar Chart of Total Bill by Day", category_orders={"day": days_order})
)

# Define the layout for the "Custom Visualizations" page
custom_visualizations_layout = html.Div(
    [
        html.H3("Example Custom Visualizations"),

        html.Hr(),

        html.H4("Scatter Plot"),
        scatter_plot,  # This is the scatter plot we defined before

        # Add spacing and a horizontal line between the charts
        html.Div(style={'height': '20px'}),  # This will add 20px of spacing
        html.Hr(),  # This will add a horizontal line

        html.H4("Timeline Chart"),
        timeline_chart,  # This is the timeline visualization we created

        # Add spacing and a horizontal line before the bar chart
        html.Div(style={'height': '20px'}),  # This will add 20px of spacing
        html.Hr(),  # This will add a horizontal line

        html.H4("Bar Chart"),
        bar_chart,
    ],
    style={"padding": "20px"}
)

def layout():
    page = dbc.Container(
        [
            # dbc.Row(dbc.Col(card(text1, centered=True), width=12), align="center",className="mb-4"),
            custom_visualizations_layout

        ],
        class_name="mt-2",
        fluid="md",
    )
    return page

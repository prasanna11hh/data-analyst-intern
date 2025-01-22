import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample supply chain data
data = {
    "Product": ["A", "B", "C", "D"],
    "Inventory Level": [100, 200, 150, 90],
    "Demand": [80, 150, 100, 70],
    "Lead Time": [3, 5, 2, 4]
}
df = pd.DataFrame(data)

# Create Dash App
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Simple Supply Chain Dashboard", style={"textAlign": "center"}),
    
    # Dropdown for product selection
    dcc.Dropdown(
        id='product-dropdown',
        options=[{'label': product, 'value': product} for product in df['Product']],
        value='A',
        style={'width': '50%', 'margin': '0 auto'}
    ),
    
    # Output section for product details
    html.Div(id='product-details', style={'textAlign': 'center', 'marginTop': 20}),
    
    # Graph for inventory vs demand
    dcc.Graph(id='inventory-demand-graph', style={'marginTop': 20})
])

@app.callback(
    [Output('product-details', 'children'),
     Output('inventory-demand-graph', 'figure')],
    [Input('product-dropdown', 'value')]
)
def update_dashboard(selected_product):
    # Filter data for selected product
    product_data = df[df['Product'] == selected_product].iloc[0]
    details = (
        f"Product: {selected_product} | "
        f"Inventory: {product_data['Inventory Level']} units | "
        f"Demand: {product_data['Demand']} units | "
        f"Lead Time: {product_data['Lead Time']} days"
    )
    
    # Create bar chart
    fig = px.bar(
        x=['Inventory', 'Demand'],
        y=[product_data['Inventory Level'], product_data['Demand']],
        labels={'x': 'Metric', 'y': 'Quantity'},
        title=f"Inventory vs Demand for Product {selected_product}"
    )
    
    return details, fig

if __name__ == '__main__':
    app.run_server(debug=True)

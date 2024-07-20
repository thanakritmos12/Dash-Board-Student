import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load student data
student_data = pd.read_csv('student.csv')

# Prepare province coordinates
province_coords = {
    "กระบี่": [8.0863, 98.9063],
    "กรุงเทพมหานคร": [13.7563, 100.5018],
    "กาญจนบุรี": [14.0228, 99.5328],
    "กาฬสินธุ์": [16.4322, 103.5061],
    "กำแพงเพชร": [16.4828, 99.5228],
    "ขอนแก่น": [16.4419, 102.8356],
    "จันทบุรี": [12.6096, 102.1045],
    "ฉะเชิงเทรา": [13.6904, 101.0766],
    "ชลบุรี": [13.3611, 100.9847],
    "ชัยนาท": [15.1860, 100.1253],
    "ชัยภูมิ": [15.8064, 102.0311],
    "ชุมพร": [10.4930, 99.1800],
    "ตรัง": [7.5590, 99.6111],
    "ตราด": [12.2420, 102.5175],
    "ตาก": [16.8790, 99.1254],
    "นครนายก": [14.2069, 101.2131],
    "นครปฐม": [13.8199, 100.0622],
    "นครพนม": [17.4108, 104.7784],
    "นครราชสีมา": [14.9799, 102.0978],
    "นครศรีธรรมราช": [8.4324, 99.9631],
    "นครสวรรค์": [15.7047, 100.1372],
    "นนทบุรี": [13.8591, 100.5217],
    "นราธิวาส": [6.4260, 101.8250],
    "น่าน": [18.7835, 100.7712],
    "บึงกาฬ": [18.3607, 103.6437],
    "บุรีรัมย์": [14.9930, 103.1029],
    "ปทุมธานี": [14.0208, 100.5250],
    "ประจวบคีรีขันธ์": [11.8129, 99.7972],
    "ปราจีนบุรี": [14.0496, 101.3692],
    "ปัตตานี": [6.8688, 101.2505],
    "พระนครศรีอยุธยา": [14.3532, 100.5680],
    "พะเยา": [19.1637, 99.9996],
    "พังงา": [8.4509, 98.5267],
    "พัทลุง": [7.6167, 100.0796],
    "พิจิตร": [16.4387, 100.3498],
    "พิษณุโลก": [16.8214, 100.2659],
    "ภูเก็ต": [7.8804, 98.3923],
    "มหาสารคาม": [16.1868, 103.2980],
    "มุกดาหาร": [16.5405, 104.7222],
    "ยะลา": [6.5425, 101.2817],
    "ยโสธร": [15.7928, 104.1454],
    "ระนอง": [9.7777, 98.6160],
    "ระยอง": [12.6833, 101.2789],
    "ราชบุรี": [13.5283, 99.8134],
    "ร้อยเอ็ด": [16.0568, 103.6531],
    "ลพบุรี": [14.7995, 100.6534],
    "ลำปาง": [18.2888, 99.4908],
    "ลำพูน": [18.5789, 99.0087],
    "ศรีสะเกษ": [15.1180, 104.3228],
    "สกลนคร": [17.1558, 104.1455],
    "สงขลา": [7.1890, 100.5953],
    "สตูล": [6.6238, 100.0674],
    "สมุทรปราการ": [13.5991, 100.5994],
    "สมุทรสงคราม": [13.4090, 100.0021],
    "สมุทรสาคร": [13.5471, 100.2744],
    "สระบุรี": [14.5299, 100.9109],
    "สระแก้ว": [13.8250, 102.3484],
    "สิงห์บุรี": [14.8901, 100.3987],
    "สุพรรณบุรี": [14.4745, 100.1200],
    "สุราษฎร์ธานี": [9.1382, 99.3214],
    "สุรินทร์": [14.8818, 103.4936],
    "สุโขทัย": [17.0060, 99.8265],
    "หนองคาย": [17.8783, 102.7421],
    "หนองบัวลำภู": [17.2046, 102.4410],
    "อำนาจเจริญ": [15.8463, 104.6353],
    "อุดรธานี": [17.4075, 102.7931],
    "อุตรดิตถ์": [17.6200, 100.0993],
    "อุทัยธานี": [15.3816, 100.0244],
    "อุบลราชธานี": [15.2287, 104.8570],
    "อ่างทอง": [14.5896, 100.4557],
    "เชียงราย": [19.9072, 99.8327],
    "เชียงใหม่": [18.7883, 98.9853],
    "เพชรบุรี": [13.1117, 99.9447],
    "เพชรบูรณ์": [16.4182, 101.1606],
    "เลย": [17.4855, 101.7223],
    "แพร่": [18.1445, 100.1408],
    "แม่ฮ่องสอน": [19.3020, 97.9685]
}

# Convert province coordinates to DataFrame
coords_df = pd.DataFrame(province_coords).T.reset_index()
coords_df.columns = ['Province', 'Latitude', 'Longitude']

# Merge student data with coordinates
merged_data = pd.merge(student_data, coords_df, left_on='schools_province', right_on='Province')

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Thailand Student Data Dashboard"

# Define the layout
# Define the layout
app.layout = html.Div([
    html.Header([
        html.H1("Thailand Student Data Dashboard", style={'text-align': 'center', 'color': '#fff'}),
        html.P("An interactive dashboard to explore student data across different provinces in Thailand.", 
               style={'text-align': 'center', 'font-size': '18px', 'color': '#ccc'})
    ], style={'background-color': '#333', 'padding': '10px', 'margin-bottom': '20px'}),
    
    html.Div([
        html.Div([
            dcc.Graph(id='map-graph')
        ], style={'width': '100%', 'margin-bottom': '20px'})  # Map graph with bottom margin
    ], style={'width': '80%', 'margin': 'auto'}),
    
    html.Div([
        dcc.Dropdown(
            id='province-dropdown',
            options=[{'label': province, 'value': province} for province in coords_df['Province']],
            value='กรุงเทพมหานคร',
            style={'width': '60%', 'padding': '5spx', 'margin': 'auto', 'color': '#000000', 'backgroundColor': '#FFFF00'}
        )
    ], style={'width': '60%', 'margin': 'auto', 'margin-bottom': '20px'}),  # Centered Dropdown

    html.Div([
        html.Div([
            dcc.Graph(id='bar-graph', style={'width': '50%'}),  # Bar graph with adjusted width
            dcc.Graph(id='pie-graph', style={'width': '50%'})  # Pie chart with adjusted width
        ], style={'display': 'flex', 'justify-content': 'space-between', 'width': '90%', 'margin': 'auto'})
    ], style={'width': '80%', 'margin': 'auto'}),
    
    html.Div([
        dash_table.DataTable(
            id='data-table',
            columns=[{"name": i, "id": i} for i in merged_data.columns],
            data=merged_data.to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={
                'height': 'auto',
                'minWidth': '80px', 'width': '80px', 'maxWidth': '80px',
                'whiteSpace': 'normal',
                'color': '#fff',
                'backgroundColor': '#444'
            },
        )
    ], style={'margin-top': '20px'}),
    
    html.Footer([
        html.P("Created by Thanakrit Chimplipak.",
               style={'text-align': 'center', 'font-size': '14px', 'color': '#888'})
    ], style={'background-color': '#333', 'padding': '10px', 'margin-top': '20px'})
], style={'background-color': '#222', 'color': '#fff'})

# Map graph callback
@app.callback(
    Output('map-graph', 'figure'),
    [Input('province-dropdown', 'value')]
)
def update_map(selected_province):
    # Create the scatter mapbox figure
    fig = px.scatter_mapbox(
        merged_data,
        lat='Latitude',
        lon='Longitude',
        hover_name='Province',  # Ensure this is in English in your data
        color='totalstd',
        size='totalstd',
        color_continuous_scale=px.colors.sequential.Plasma,
        size_max=30,
        zoom=5,
        title="Student Distribution by Province in Thailand"  # English title
    )

    # Update layout for better design
    fig.update_layout(
        mapbox_style="open-street-map",  # Or another style that suits your needs
        mapbox_zoom=5,
        mapbox_center={"lat": 15.87, "lon": 100.9925},
        margin={"r":0, "t":50, "l":0, "b":0},
        title={
            'text': "Student Distribution by Province",  # English title
            'x':0.5,
            'font_color': '#ffffff',
            'font_size': 24
        },
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    # Add annotations in English
    for i in range(len(merged_data)):
        fig.add_annotation(
            x=merged_data.loc[i, 'Longitude'],
            y=merged_data.loc[i, 'Latitude'],
            text=merged_data.loc[i, 'Province'],  # Ensure this is in English in your data
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-40,
            font=dict(size=10, color='#ffffff')
        )

    return fig

# Bar graph callback
@app.callback(
    Output('bar-graph', 'figure'),
    [Input('province-dropdown', 'value')]
)
def update_bar(selected_province):
    filtered_data = merged_data[merged_data['schools_province'] == selected_province]
    fig = px.bar(filtered_data, x='level', y=['totalmale', 'totalfemale'], barmode='group',
                 title=f"Total Male and Female Students in {selected_province}",
                 labels={'value': 'Number of Students', 'level': 'Education Level'},
                 color_discrete_map={'totalmale': '#1f77b4', 'totalfemale': '#ff7f0e'})
    fig.update_layout(title={'x':0.5, 'font_color': '#fff'}, template='plotly_dark', xaxis_title='', yaxis_title='Number of Students')
    fig.update_xaxes(tickangle=-45)  # Rotate x-axis labels for better readability
    return fig

# Pie chart callback
@app.callback(
    Output('pie-graph', 'figure'),
    [Input('province-dropdown', 'value')]
)
def update_pie(selected_province):
    filtered_data = merged_data[merged_data['schools_province'] == selected_province]
    total_male = filtered_data['totalmale'].sum()
    total_female = filtered_data['totalfemale'].sum()

    fig = px.pie(names=['Total Male Students', 'Total Female Students'],
                 values=[total_male, total_female],
                 title=f"Distribution of Male and Female Students in {selected_province}")
    fig.update_layout(title={'x':0.5, 'font_color': '#fff'}, template='plotly_dark')
    return fig

# Data table callback
@app.callback(
    Output('data-table', 'data'),
    [Input('province-dropdown', 'value')]
)
def update_table(selected_province):
    filtered_data = merged_data[merged_data['schools_province'] == selected_province]
    return filtered_data.to_dict('records')

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
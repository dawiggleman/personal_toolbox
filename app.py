from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_daq as daq
from os import listdir
from os.path import isfile, join

#Test Script Global Variables
test_scripts_path = './test_scripts'
test_scripts_list = [f for f in listdir(test_scripts_path) if isfile(join(test_scripts_path, f))] #gets all test scripts in folder
selected_test_script = None

########################## App layout and implementation #########################

##App Layout##

#CSS Styling
#external_stylesheet=['./assets/01_spacex.css']
external_stylesheet=['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets= external_stylesheet)

green_button_style = {'background-color': 'green',
                    'color': 'white',
                    'height': '50px',
                    'width': '100px',
                    'margin-top': '50px',
                    'margin-left': '50px'}

red_button_style = {'background-color': 'red',
                    'color': 'white',
                    'height': '50px',
                    'width': '100px',
                    'margin-top': '50px',
                    'margin-left': '50px'}

#Main Style layout
app.layout = html.Div([ 
    html.H1(children="Control Dashboard", className='content'),

    #Script Selection Dropdown
    html.Div(
        style={'width': '20%'},
        children =[ 
            html.H2('Select which test file to run:'),
            dcc.Dropdown(
                test_scripts_list,
                value = test_scripts_list[0],
                id = 'script_selection_dropdown'
            ),
            html.Div(id = 'dropdown_output'),
        ]
    ),

    #Run and Stop Script Buttons

    html.Div(
        children = [
            html.Div(html.Button('Start script', id='start_test_script', n_clicks=0)),
            html.Div(html.Button('Stop script', id='stop_test_script', n_clicks=0 ))
        ]
    ),

    #Power Buttons
    html.Div(style={
            #'align-items':'left',
            'display': 'flex',
            'justify-content':'left'
        },
        children=[
        daq.PowerButton(
            style = {'color':'black'},
            id = 'powerButton1',
            on = False),
        daq.PowerButton(
            id = 'powerButton2',
            on = False)
    ]
    ),
    html.Div(id='powerButton1_result')
])

###### Callbacks to add functionality ######
    #Callback is a function that runs in response to an input event
        #Takes the input from an event as its input argument
        #Returns an output that updates web application

#Power Button 1 Callback
@app.callback( 
    Output('powerButton1_result', 'children'),
    Input('powerButton1','on')#input to function that callback is associated with
)
def update_button1_div(on):
    return f'The button is {on}.'

#Script Selection Dropdown callback
@app.callback(
    Output('dropdown_output', 'children'),
    Input('script_selection_dropdown','value')
)
def update_selected_script(value):
    selected_test_script = value 

#Run Program
if __name__ == '__main__':
    app.run_server(debug= True)



from dash import Dash, html, dcc

external_stylesheet=['/assets/01_spacex.css']
app = Dash(__name__, external_stylesheets= external_stylesheet)

app.layout = html.Div(children =[ 
    html.H1(children="Control Dashboard", className='content')
])


if __name__ == '__main__':
    app.run_server(debug= True)
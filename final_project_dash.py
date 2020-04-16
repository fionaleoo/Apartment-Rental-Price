import pickle
import plotly
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import dash_table
from dash.dependencies import Input, Output, State

def generate_table(dataframe, page_size=10, room_val = '', space_val = '', state_val = '', year_val = '', type_val = '', position_val = '',
                    build_val = '', heat_val = '', energy_val = '', condition_val = '', int_val = '', kitchen_val = '', balcony_val = '',
                    lift_val = '', pets_val = '', garden_val = '', cellar_val = '', parking_val = '', firing_val = '', upload_val = '',
                    tv_val = '', ad_val = ''):
    if room_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['noRooms'] == room_val)]
    if space_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['livingSpace'] == space_val)]
    if state_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['state'] == state_val)]
    if year_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['yearConstructedRange'] == year_val)]
    if type_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['typeOfFlat'] == type_val)]
    if position_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['position'] == position_val)]
    if build_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['buildingType'] == build_val)]
    if heat_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['heatingType'] == heat_val)]
    if energy_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['energyEfficiencyClass'] == energy_val)]
    if condition_val == '':
        dataframe = dataframe
    elif condition_val == 1:
        dataframe = dataframe[(dataframe['goodCondition'] == True)]
    else:
        dataframe = dataframe[(dataframe['goodCondition'] == False)]
    if int_val == '':
        dataframe = dataframe
    elif int_val == 1:
        dataframe = dataframe[(dataframe['niceInterior'] == True)]
    else:
        dataframe = dataframe[(dataframe['niceInterior'] == False)]
    if kitchen_val == '':
        dataframe = dataframe
    elif kitchen_val == 1:
        dataframe = dataframe[(dataframe['hasKitchen'] == True)]
    else:
        dataframe = dataframe[(dataframe['hasKitchen'] == False)]
    if balcony_val == '':
        dataframe = dataframe
    elif balcony_val == 1:
        dataframe = dataframe[(dataframe['balcony'] == True)]
    else:
        dataframe = dataframe[(dataframe['balcony'] == False)]
    if lift_val == '':
        dataframe = dataframe
    elif lift_val == 1:
        dataframe = dataframe[(dataframe['lift'] == True)]
    else:
        dataframe = dataframe[(dataframe['lift'] == False)]
    if pets_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['petsAllowed'] == pets_val)]
    if garden_val == '':
        dataframe = dataframe
    elif garden_val == 1:
        dataframe = dataframe[(dataframe['garden'] == True)]
    else:
        dataframe = dataframe[(dataframe['garden'] == False)]
    if cellar_val == '':
        dataframe = dataframe
    elif cellar_val == 1:
        dataframe = dataframe[(dataframe['cellar'] == True)]
    else:
        dataframe = dataframe[(dataframe['cellar'] == False)]
    if parking_val == '':
        dataframe = dataframe
    elif parking_val == 1:
        dataframe = dataframe[(dataframe['parkSpace'] == True)]
    else:
        dataframe = dataframe[(dataframe['parkSpace'] == False)]
    if firing_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['firingTypes'] == upload_val)]
    if upload_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['telekomUploadSpeed'] == upload_val)]
    if tv_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['telekomTvOffer'] == tv_val)]
    if ad_val == '':
        dataframe = dataframe
    else:
        dataframe = dataframe[(dataframe['year'] == ad_val)]

    table = dash_table.DataTable(
        id='dataTable',
        columns=[{
            'name' : i,
            'id' : i
        } for i in dataframe.columns],
        data=dataframe.to_dict('records'),
        page_action='native',
        page_current = 0,
        page_size = page_size,
        style_table={'overflowX': 'scroll'}
    )

    if len(dataframe) == 0:
        return 'No Data Found'
    else:
        return table


price_pred = pickle.load(open('rentpredict_model_final.sav', 'rb'))

def predict_price(pred_room_val, pred_space_val, pred_state_val, pred_year_val, pred_type_val, pred_position_val, pred_build_val,
                    pred_heat_val, pred_energy_val, pred_condition_val, pred_int_val, pred_kitchen_val, pred_balcony_val,
                    pred_lift_val, pred_pets_val, pred_garden_val, pred_cellar_val, pred_parking_val, pred_firing_val, 
                    pred_upload_val, pred_tv_val, pred_ad_val):
    global cols
    global df
    df_pred = pd.DataFrame(columns = cols)
    if pred_state_val == 'Baden_Württemberg':
        pass
    else:
        for i in df['state'].unique():
            if pred_state_val == i:
                x = 'state_{}'.format(i)
                df_pred[x] = [1]
    if pred_year_val == '1951_1960':
        pass
    else:
        for i in df['year'].unique():
            if pred_year_val == i:
                x = 'yearConstructedRange_{}'.format(i)
                df_pred[x] = [1]
    if pred_type_val == 'apartment':
        pass
    else:
        for i in df['typeOfFlat'].unique():
            if pred_type_val == i:
                x = 'typeOfFlat_{}'.format(i)
                df_pred[x] = [1]
    if pred_position_val == 'basement':
        pass
    else:
        for i in df['position'].unique():
            if pred_position_val == i:
                x = 'position_{}'.format(i)
                df_pred[x] = [1]
    if pred_build_val == 'high_rise':
        pass
    else:
        for i in df['buildingType'].unique():
            if pred_build_val == i:
                x = 'buildingType_{}'.format(i)
                df_pred[x] = [1]
    if pred_heat_val == 'central_heating':
        pass
    else:
        for i in df['heatingType'].unique():
            if pred_heat_val == i:
                x = 'heatingType_{}'.format(i)
                df_pred[x] = [1]
    if pred_energy_val == 'A':
        pass
    else:
        for i in df['energyEfficiencyClass'].unique():
            if pred_energy_val == i:
                x = 'energyEfficiencyClass_{}'.format(i)
                df_pred[x] = [1]
    if pred_tv_val == 'NONE':
        pass
    else:
        for i in df['telekomTvOffer'].unique():
            if pred_tv_val == i:
                x = 'telekomTvOffer_{}'.format(i)
                df_pred[x] = [1]
    if pred_upload_val == '0.0':
        pass
    else:
        for i in df['telekomUploadSpeed'].unique():
            if pred_upload_val == i:
                x = 'telekomUploadSpeed_{}'.format(i)
                df_pred[x] = [1]
    if pred_firing_val == 'bio_energy':
        for i in df['firingTypes'].unique():
            if pred_firing_val == i:
                x = 'firingTypes_{}'.format(i)
                df_pred[x] = [1]
    if pred_pets_val == 'negotiable':
        pass
    else:
        for i in df['petsAllowed'].unique():
            if pred_pets_val == i:
                x = 'petsAllowed_{}'.format(i)
                df_pred[x] = [1]
    if pred_ad_val == '2018':
        pass
    else:
        for i in df['year'].unique():
            if pred_ad_val == i:
                x = 'year_{}'.format(i)
                df_pred[x] = [1]

    if pred_int_val == 1:
        df_pred['niceInterior_True'] = [True]
    if pred_kitchen_val == 1:
        df_pred['hasKitchen_True'] = [True]
    if pred_cellar_val == 1:
        df_pred['cellar_True'] = [True]
    if pred_kitchen_val == 1:
        df_pred['balcony_True'] = [True]
    if pred_lift_val == 1:
        df_pred['lift_True'] = [True]
    if pred_condition_val == 1:
        df_pred['goodCondition_True'] = [True]
    if pred_int_val == 1:
        df_pred['niceInterior_True'] = [True]
    if pred_parking_val == 1:
        df_pred['parkSpace_True'] = [True]
    if pred_garden_val == 1:
        df_pred['garden_True'] = [True]

    df_pred['livingSpace'] = [pred_space_val]
    df_pred['noRooms'] = [pred_room_val]

    df_pred.fillna(value = 0, inplace = True)

    prediction = price_pred.predict(df_pred)
    return prediction

df = pd.read_csv('cleaned_final.csv')
external_stylesheets = ['https://codepen.io/chiddyp/pen/bWLwP.css']

df['year'] = df['year'].astype('str')
df['telekomUploadSpeed'] = df['telekomUploadSpeed'].astype('str')
cat_cols = df.drop(['baseRent', 'serviceCharge', 'heatingCosts', 'pricetrend', 'totalRent'], axis = 1).describe(exclude = 'number').columns
cols = pd.get_dummies(df.drop(['baseRent', 'serviceCharge', 'heatingCosts', 'pricetrend', 'totalRent'], axis = 1), columns = cat_cols, drop_first = True).columns


app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

app.layout = html.Div(children=[
        html.H1('Immoscout'),

        html.Div(children='''
             Apartment Rental Price.
    '''),
    dcc.Tabs(children = [
        dcc.Tab(value = 'Tab 1', label = 'Data Frame', children = [
            html.Div([
            html.Div([
                html.P('Number of Rooms'),
                dcc.Input(id='filter-room', type='number', value=2, min = 1)
            ],
                className='col-3'),
            html.Div([
                html.P('Living Space (m2)'),
                dcc.Input(id='filter-space', type='number', value=25, min = 1)
            ],
                className='col-3'),
            html.Div([
                html.P('State'),
                dcc.Dropdown(id = 'filter-state', options = [{'label': i, 'value': i} for i in df['state'].unique()], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Year Constructed Range'),
                dcc.Dropdown(id = 'filter-year', options = [
                                                                {'label': '2011 - 2020', 'value': '2011_2020'},
                                                                {'label': '2001 - 2010', 'value': '2001_2010'},
                                                                {'label': '1991 - 2000', 'value': '1991_2000'},
                                                                {'label': '1981 - 1990', 'value': '1981_1990'},
                                                                {'label': '1971 - 1980', 'value': '1971_1980'},
                                                                {'label': '1961 - 1970', 'value': '1961_1970'},
                                                                {'label': '1951 - 1960', 'value': '1951_1960'},
                                                                {'label': 'Before 1950', 'value': 'before_1950'},
                                                                {'label': 'None', 'value': ''},], 
                value = '')
            ],
                className='col-3'),
        ],
                className='row'),
            
            html.Br(),

            html.Div([
            html.Div([
                html.P('Type of Flat'),
                dcc.Dropdown(id = 'filter-type', options = [{'label': i, 'value': i} for i in df['typeOfFlat'].unique() if i != 'other'], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Position'),
                dcc.Dropdown(id = 'filter-position', options = [{'label': i, 'value': i} for i in df['position'].unique() if i != 'unknown'], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Building Type'),
                dcc.Dropdown(id = 'filter-build', options = [
                                                                {'label': 'Low Rise', 'value': 'low_rise'},
                                                                {'label': 'Mid Rise', 'value': 'mid_rise'},
                                                                {'label': 'High Rise', 'value': 'high_rise'},
                                                                {'label': 'None', 'value': ''}], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Heating Type'),
                dcc.Dropdown(id = 'filter-heat', options = [{'label': i, 'value': i} for i in df['heatingType'].unique() if i != 'unknown'], 
                value = '')
            ],
                className='col-3'),
        ],
                className='row'),
            
            html.Br(),

            html.Div([
            html.Div([
                html.P('Energy Efficiency Class'),
                dcc.Dropdown(id = 'filter-energy', options = [
                                                                {'label': 'A_PLUS', 'value': 'A PLUS'},
                                                                {'label': 'A', 'value': 'A'},
                                                                {'label': 'B', 'value': 'B'},
                                                                {'label': 'C', 'value': 'C'},
                                                                {'label': 'D', 'value': 'D'},
                                                                {'label': 'E', 'value': 'E'},
                                                                {'label': 'F', 'value': 'F'},
                                                                {'label': 'G', 'value': 'G'},
                                                                {'label': 'H', 'value': 'H'},
                                                                {'label': 'None', 'value': ''},
                                                                ], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Good Condition'),
                dcc.Dropdown(id = 'filter-condition', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                                {'label': 'None', 'value': ''}], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Nice Interior'),
                dcc.Dropdown(id = 'filter-int', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                                {'label': 'None', 'value': ''}], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Kitchen'),
                dcc.Dropdown(id = 'filter-kitchen', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                                {'label': 'None', 'value': ''}], 
                value = '')
            ],
                className='col-3')
        ],
                className='row'),

            html.Br(),

            html.Div([
            html.Div([
                html.P('Balcony'),
                dcc.Dropdown(id = 'filter-balcony', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                                {'label': 'None', 'value': ''}], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Lift'),
                dcc.Dropdown(id = 'filter-lift', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                                {'label': 'None', 'value': ''}], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Pets Allowed'),
                dcc.Dropdown(id = 'filter-pets', options = [{'label': i, 'value': i} for i in df['petsAllowed'].unique()], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Garden'),
                dcc.Dropdown(id = 'filter-garden', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                                {'label': 'None', 'value': ''}], 
                value = '')
            ],
                className='col-3'),
        ],
                className='row'),

            html.Br(),

            html.Div([   
            html.Div([
                html.P('Cellar'),
                dcc.Dropdown(id = 'filter-cellar', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                                {'label': 'None', 'value': ''}], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Parking Space'),
                dcc.Dropdown(id = 'filter-parking', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                                {'label': 'None', 'value': ''}], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Firing Types'),
                dcc.Dropdown(id = 'filter-firing', options = [{'label': i, 'value': i} for i in df['firingTypes'].unique()], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Telekom Upload Speed'),
                dcc.Dropdown(id = 'filter-upload', options = [{'label': i, 'value': i} for i in df['telekomUploadSpeed'].unique()], 
                value = '')
            ],
                className='col-3'),
        ],
                className='row'),

            html.Br(),

            html.Div([
            html.Div([
                html.P('Telekom Tv Offer'),
                dcc.Dropdown(id = 'filter-tv', options = [{'label': i, 'value': i} for i in df['telekomTvOffer'].unique()], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Year Posted'),
                dcc.Dropdown(id = 'filter-ad', options = [{'label': i, 'value': i} for i in df['year'].unique()], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Max Rows'),
                dcc.Input(id='filter-row', type='number', value=10),
                html.Br(),
                html.Button('Search', id='filter')
            ],
                className = 'col-3'),
        ],
                className='row'),

            html.Br(),

            html.Div(id = 'div-table', children = [generate_table(df)]
            )
        ]),
    
    dcc.Tab(value = 'Tab 2', label = 'Data Visualization', children =[

            html.Div([
            html.Div([
                html.P('Feature'),
                dcc.Dropdown(id = 'x-axis', options = [{'label': i, 'value': i} for i in df.drop('totalRent', axis = 1).columns], 
                value = 'state')
            ],
                className='col-3'),
            html.Div([
                html.P('Prices'),
                dcc.Dropdown(id = 'y-axis', options = [{'label': i, 'value': i} for i in ['totalRent', 'baseRent', 'serviceCharge', 'heatingCosts', 'pricetrend']], 
                value = 'totalRent')
            ],
                className='col-3'),
            ],
                className='row'
            ),

            html.Br(),

            html.Div(children = dcc.Graph(
                id = 'graph-scatter',
                figure = {
                    'data' : [
                        go.Scatter(
                            x = df['state'],
                            y = df['totalRent'],
                            mode = 'markers',
                        )
                    ], 
                    'layout':go.Layout(
                            xaxis = {'title' : 'state'},
                            yaxis = {'title' : 'totalRent'},
                            title = 'state and totalRent',
                            hovermode = 'closest'
                    )
                    }
            ))

        ]),

    dcc.Tab(value = 'Tab 3', label = 'Predicting Total Rent', children =[
            html.Div([
            html.Div([
                html.P('Number of Rooms'),
                dcc.Input(id='pred-room', type='number', value=1)
            ],
                className='col-3'),
            html.Div([
                html.P('Living Space (m2)'),
                dcc.Input(id='pred-space', type='number', value=1)
            ],
                className='col-3'),
            html.Div([
                html.P('State'),
                dcc.Dropdown(id = 'pred-state', options = [{'label': i, 'value': i} for i in df['state'].unique()], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Year Constructed Range'),
                dcc.Dropdown(id = 'pred-year', options = [
                                                                {'label': '2011 - 2020', 'value': '2011_2020'},
                                                                {'label': '2001 - 2010', 'value': '2001_2010'},
                                                                {'label': '1991 - 2000', 'value': '1991_2000'},
                                                                {'label': '1981 - 1990', 'value': '1981_1990'},
                                                                {'label': '1971 - 1980', 'value': '1971_1980'},
                                                                {'label': '1961 - 1970', 'value': '1961_1970'},
                                                                {'label': '1951 - 1960', 'value': '1951_1960'},
                                                                {'label': 'Before 1950', 'value': 'before_1950'},
                                                        ], 
                value = '')
            ],
                className='col-3'),
        ],
                className='row'),
            
            html.Br(),

            html.Div([
            html.Div([
                html.P('Type of Flat'),
                dcc.Dropdown(id = 'pred-type', options = [{'label': i, 'value': i} for i in df['typeOfFlat'].unique() if i != 'other'], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Position'),
                dcc.Dropdown(id = 'pred-position', options = [{'label': i, 'value': i} for i in df['position'].unique() if i != 'unknown'], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Building Type'),
                dcc.Dropdown(id = 'pred-build', options = [
                                                                {'label': 'Low Rise', 'value': 'low_rise'},
                                                                {'label': 'Mid Rise', 'value': 'mid_rise'},
                                                                {'label': 'High Rise', 'value': 'high_rise'},
                                                            ], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Heating Type'),
                dcc.Dropdown(id = 'pred-heat', options = [{'label': i, 'value': i} for i in df['heatingType'].unique() if i != 'unknown'], 
                value = '')
            ],
                className='col-3'),
        ],
                className='row'),
            
            html.Br(),

            html.Div([
            html.Div([
                html.P('Energy Efficiency Class'),
                dcc.Dropdown(id = 'pred-energy', options = [
                                                                {'label': 'A_PLUS', 'value': 'A_PLUS'},
                                                                {'label': 'A', 'value': 'A'},
                                                                {'label': 'B', 'value': 'B'},
                                                                {'label': 'C', 'value': 'C'},
                                                                {'label': 'D', 'value': 'D'},
                                                                {'label': 'E', 'value': 'E'},
                                                                {'label': 'F', 'value': 'F'},
                                                                {'label': 'G', 'value': 'G'},
                                                                {'label': 'H', 'value': 'H'}
                                                                ], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Good Condition'),
                dcc.Dropdown(id = 'pred-condition', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                            ], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Nice Interior'),
                dcc.Dropdown(id = 'pred-int', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                            ], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Kitchen'),
                dcc.Dropdown(id = 'pred-kitchen', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                            ], 
                value = '')
            ],
                className='col-3')
        ],
                className='row'),

            html.Br(),

            html.Div([
            html.Div([
                html.P('Balcony'),
                dcc.Dropdown(id = 'pred-balcony', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                            ], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Lift'),
                dcc.Dropdown(id = 'pred-lift', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                            ], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Pets Allowed'),
                dcc.Dropdown(id = 'pred-pets', options = [{'label': i, 'value': i} for i in df['petsAllowed'].unique() if i != 'unknown'], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Garden'),
                dcc.Dropdown(id = 'pred-garden', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                            ], 
                value = '')
            ],
                className='col-3'),
        ],
                className='row'),

            html.Br(),

            html.Div([   
            html.Div([
                html.P('Cellar'),
                dcc.Dropdown(id = 'pred-cellar', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                            ], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Parking Space'),
                dcc.Dropdown(id = 'pred-parking', options = [
                                                                {'label': 'Yes', 'value': 1},
                                                                {'label': 'No', 'value': 0},
                                                            ], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Firing Types'),
                dcc.Dropdown(id = 'pred-firing', options = [{'label': i, 'value': i} for i in df['firingTypes'].unique() if i != 'unknown'], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Telekom Upload Speed'),
                dcc.Dropdown(id = 'pred-upload', options = [{'label': i, 'value': i} for i in df['telekomUploadSpeed'].unique()], 
                value = '')
            ],
                className='col-3'),
        ],
                className='row'),

            html.Br(),

            html.Div([
            html.Div([
                html.P('Telekom Tv Offer'),
                dcc.Dropdown(id = 'pred-tv', options = [{'label': i, 'value': i} for i in df['telekomTvOffer'].unique()], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Year Posted'),
                dcc.Dropdown(id = 'pred-ad', options = [{'label': i, 'value': i} for i in df['year'].unique()], 
                value = '')
            ],
                className='col-3'),
            html.Div([
                html.P('Predict'),
                html.Button('Predict', id='pred')
            ],
                className = 'col-3'),
                html.Div([
                html.P('Rent Price Prediction : '),
                html.Div(id = 'div-pred', children = [0]),
              ],
                className = 'col-3')
        ],
                className='row'),
    ])
    ],
    content_style = {
            'fontFamily' : 'Arial',
            'borderBottom' : '1px solid #d6d6d6',
            'borderLeft' : '1px solid #d6d6d6',
            'borderRight' : '1px solid #d6d6d6',
            'padding' : '44px'
        }
    )
],
style = {
        'maxwidth' : '1200px',
        'margin' : '0 auto'
    }
)

@app.callback(
    Output(component_id = 'div-table', component_property='children'),
    [Input(component_id = 'filter', component_property='n_clicks')],
    [State(component_id = 'filter-row', component_property='value'),
    State(component_id = 'filter-room', component_property='value'),
    State(component_id = 'filter-space', component_property='value'),
    State(component_id = 'filter-state', component_property='value'),
    State(component_id = 'filter-year', component_property='value'),
    State(component_id = 'filter-type', component_property='value'),
    State(component_id = 'filter-position', component_property='value'),
    State(component_id = 'filter-build', component_property='value'),
    State(component_id = 'filter-heat', component_property='value'),
    State(component_id = 'filter-energy', component_property='value'),
    State(component_id = 'filter-condition', component_property='value'),
    State(component_id = 'filter-int', component_property='value'),
    State(component_id = 'filter-kitchen', component_property='value'),
    State(component_id = 'filter-balcony', component_property='value'),
    State(component_id = 'filter-lift', component_property='value'),
    State(component_id = 'filter-pets', component_property='value'),
    State(component_id = 'filter-garden', component_property='value'),
    State(component_id = 'filter-cellar', component_property='value'),
    State(component_id = 'filter-parking', component_property='value'),
    State(component_id = 'filter-firing', component_property='value'),
    State(component_id = 'filter-upload', component_property='value'),
    State(component_id = 'filter-tv', component_property='value'),
    State(component_id = 'filter-ad', component_property='value')
    ]
)

def update_table(n_clicks, row, room_val, space_val, state_val, year_val, type_val, position_val, build_val, heat_val, 
                energy_val, condition_val, int_val, kitchen_val, balcony_val, lift_val, pets_val, garden_val, cellar_val, parking_val,
                firing_val, upload_val, tv_val, ad_val):
    children = [generate_table(df, page_size = row, room_val = room_val, space_val = space_val, state_val = state_val,
                year_val = year_val, type_val = type_val, position_val = position_val, build_val = build_val,
                heat_val = heat_val, energy_val = energy_val, condition_val = condition_val, int_val = int_val,
                kitchen_val = kitchen_val, balcony_val = balcony_val, lift_val = lift_val, pets_val = pets_val,
                garden_val = garden_val, cellar_val = cellar_val, parking_val = parking_val, upload_val = upload_val,
                tv_val = tv_val, firing_val = firing_val, ad_val = ad_val)]
    return children

@app.callback(
    Output(component_id = 'graph-scatter', component_property='figure'),
    [Input(component_id = 'x-axis', component_property='value'),
    Input(component_id = 'y-axis', component_property='value')],
)

def create_scatter(x_val, y_val):
    figure = {
                    'data' : [
                        go.Scatter(
                            x = df[x_val],
                            y = df[y_val],
                            mode = 'markers',
                        )
                    ], 
                    'layout':go.Layout(
                            xaxis = {'title' : x_val},
                            yaxis = {'title' : y_val},
                            title = '{} and {}'.format(x_val, y_val),
                            hovermode = 'closest'
                    )
                    }
    return figure


@app.callback(
    Output(component_id = 'div-pred', component_property='children'),
    [Input(component_id = 'pred', component_property='n_clicks')],
    [State(component_id = 'pred-room', component_property='value'),
    State(component_id = 'pred-space', component_property='value'),
    State(component_id = 'pred-state', component_property='value'),
    State(component_id = 'pred-year', component_property='value'),
    State(component_id = 'pred-type', component_property='value'),
    State(component_id = 'pred-position', component_property='value'),
    State(component_id = 'pred-build', component_property='value'),
    State(component_id = 'pred-heat', component_property='value'),
    State(component_id = 'pred-energy', component_property='value'),
    State(component_id = 'pred-condition', component_property='value'),
    State(component_id = 'pred-int', component_property='value'),
    State(component_id = 'pred-kitchen', component_property='value'),
    State(component_id = 'pred-balcony', component_property='value'),
    State(component_id = 'pred-lift', component_property='value'),
    State(component_id = 'pred-pets', component_property='value'),
    State(component_id = 'pred-garden', component_property='value'),
    State(component_id = 'pred-cellar', component_property='value'),
    State(component_id = 'pred-parking', component_property='value'),
    State(component_id = 'pred-firing', component_property='value'),
    State(component_id = 'pred-upload', component_property='value'),
    State(component_id = 'pred-tv', component_property='value'),
    State(component_id = 'pred-ad', component_property='value')
    ]
)

def update_pred(n_clicks, pred_room_val, pred_space_val, pred_state_val, pred_year_val, pred_type_val, pred_position_val, pred_build_val,
                    pred_heat_val, pred_energy_val, pred_condition_val, pred_int_val, pred_kitchen_val, pred_balcony_val,
                    pred_lift_val, pred_pets_val, pred_garden_val, pred_cellar_val, pred_parking_val, pred_firing_val, 
                    pred_upload_val, pred_tv_val, pred_ad_val):
    if (pred_room_val == 0) | (pred_space_val == 0):
        children = [0]
    if (pred_state_val == '') | (pred_year_val == '') | (pred_type_val == ''):
        children = [0]
    if (pred_position_val == '' )| (pred_build_val == '') | (pred_heat_val == '') | (pred_energy_val == '') | (pred_condition_val == ''):
        children = [0]
    if (pred_int_val == '') | (pred_kitchen_val == '') | (pred_balcony_val == '') | (pred_lift_val == '')| (pred_pets_val == ''):
        children = [0]
    if (pred_garden_val == '') | (pred_cellar_val == '') | (pred_parking_val == '') | (pred_firing_val == '') | (pred_upload_val == ''):
        children = [0]
    if (pred_tv_val == '') | (pred_ad_val == ''):
        children = [0]
    else:
        children = [predict_price(pred_room_val = pred_room_val, pred_space_val = pred_space_val, pred_state_val = pred_state_val,
                    pred_year_val = pred_year_val, pred_type_val = pred_type_val, pred_position_val = pred_position_val,
                    pred_build_val = pred_build_val, pred_heat_val = pred_heat_val, pred_energy_val = pred_energy_val,
                    pred_condition_val = pred_condition_val, pred_int_val = pred_int_val, pred_kitchen_val = pred_kitchen_val,
                    pred_balcony_val = pred_balcony_val, pred_lift_val = pred_lift_val, pred_pets_val = pred_pets_val,
                    pred_garden_val = pred_garden_val, pred_cellar_val = pred_cellar_val, pred_parking_val = pred_parking_val,
                    pred_firing_val = pred_firing_val, pred_upload_val = pred_upload_val, pred_tv_val = pred_tv_val, pred_ad_val = pred_ad_val)]
    return children[0]

if __name__ == '__main__':
    app.run_server(debug=True)
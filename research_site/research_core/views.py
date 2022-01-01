# Importing default django methods:
from django.shortcuts import render

# Importing plotly methods:
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Importing data manipulation packages:
import numpy as np

# Importing date methods:
import datetime

# Renders main site - largely static content:
def site_index(request):
    context = {}
    return render(request, "research_core/website_index.html", context=context)

# Research Homepage view:
def research_main_page(request):
    """The main page for displaying the research dashboard. This is used not only
    to display recent Sources objects but also allows for the querying of specific 
    types of Source searches.

    """
    # Creating a context to be populated:
    context = {}

    # Internal function for generating calendar heatmaps:
    def display_year(z,
        year: int = None,
        month_lines: bool = True, 
        fig=None, 
        row: int = None):
        """The method that renders a calendar heatmap showing the number of sources per day given 
        an array of Source counts. This method can either be called on its own to generate a calendar
        heatmap for a single year or it can be 'recursively' called by the display_years function to
        generate a heatmap across multiple years. 

        Args:
            z (np.array): A dataset containing the daily counts of all Sources read per day stored in a 
                1-D numpy array.

            year (int): The year that the calendar heatmap will be rendered for. It creates a subplot of
                the calendar heatmap with this specific year as a label.

            month_lines (Bool): A boolean which determines if lines will be used to seperate each month
                on the heatmap.

            fig (go.Figure): The figure object that the subplot the method generates will be appended too.
                This is necessary as this method is recursively called via the display_years() method.

            row (int): The row of the sublot that is used for labeling and the transforming the dataset.

        """
        if year is None:
            year = datetime.datetime.now().year
        
        data = np.ones(365) * 0
        data[:len(z)] = z
        
        d1 = datetime.date(year, 1, 1)
        d2 = datetime.date(year, 12, 31)

        delta = d2 - d1
        
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month_days =   [31,    28,    31,     30,    31,     30,    31,    31,    30,    31,    30,    31]
        month_positions = (np.cumsum(month_days) - 15)/7

        dates_in_year = [d1 + datetime.timedelta(i) for i in range(delta.days+1)] #gives me a list with datetimes for each day a year
        weekdays_in_year = [i.weekday() for i in dates_in_year] #gives [0,1,2,3,4,5,6,0,1,2,3,4,5,6,…] (ticktext in xaxis dict translates this to weekdays
        
        weeknumber_of_dates = [int(i.strftime("%V")) if not (int(i.strftime("%V")) == 1 and i.month == 12) else 53
                            for i in dates_in_year] #gives [1,1,1,1,1,1,1,2,2,2,2,2,2,2,…] name is self-explanatory
        
        # Creating the text labels for each of the points:
        counter = 0 
        text = []
        for date in dates_in_year:
             #TODO: PROBLEM HERE
            element = f"{z[counter]} Sources Read On {date_obj}"
            text.append(element)

        text = [str(i.strftime()) for i in dates_in_year]
        
        #4cc417 green #347c17 dark green
        colorscale=[[False, '#eeeeee'], [True, '#76cf63']]
        
        # handle end of year
        data = [
            go.Heatmap(
                x=weeknumber_of_dates,
                y=weekdays_in_year,
                z=data,
                text=text,
                hoverinfo='text',
                xgap=3, # this
                ygap=3, # and this is used to make the grid-like apperance
                showscale=False,
                colorscale=colorscale
            )
        ]
        
            
        if month_lines:
            kwargs = dict(
                mode='lines',
                line=dict(
                    color='#9e9e9e',
                    width=1
                ),
                hoverinfo='skip'
                
            )
            for date, dow, wkn in zip(dates_in_year,
                                    weekdays_in_year,
                                    weeknumber_of_dates):
                if date.day == 1:
                    data += [
                        go.Scatter(
                            x=[wkn-.5, wkn-.5],
                            y=[dow-.5, 6.5],
                            **kwargs
                        )
                    ]
                    if dow:
                        data += [
                        go.Scatter(
                            x=[wkn-.5, wkn+.5],
                            y=[dow-.5, dow - .5],
                            **kwargs
                        ),
                        go.Scatter(
                            x=[wkn+.5, wkn+.5],
                            y=[dow-.5, -.5],
                            **kwargs
                        )
                    ]
                        
                        
        layout = go.Layout(
            title='activity chart',
            height=250,
            yaxis=dict(
                showline=False, showgrid=False, zeroline=False,
                tickmode='array',
                ticktext=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                tickvals=[0, 1, 2, 3, 4, 5, 6],
                autorange="reversed"
            ),
            xaxis=dict(
                showline=False, showgrid=False, zeroline=False,
                tickmode='array',
                ticktext=month_names,
                tickvals=month_positions
            ),
            font={'size':10, 'color':'#9e9e9e'},
            plot_bgcolor=('#fff'),
            margin = dict(t=40),
            showlegend=False
        )

        if fig is None:
            fig = go.Figure(data=data, layout=layout)
        else:
            fig.add_traces(data, rows=[(row+1)]*len(data), cols=[1]*len(data))
            fig.update_layout(layout)
            fig.update_xaxes(layout['xaxis'])
            fig.update_yaxes(layout['yaxis'])

    
        return fig

    def display_years(z, years):
        """The method that makes use of the display_year() method to create and
        modify the calendar heatmap of Sources read. 

        Args:
            z (np.array): The dataset of Sources read per year stored as a 1-D array of integers.

            years (tuple): The relevant years of the dataset stored as a tuple which determines
                which subplots are generated eg: (2019, 2020).

        Returns:
            go.Figure: The fully rendered calendar heatmap ready to be passed onto the template.

        """
        fig = make_subplots(rows=len(years), cols=1, subplot_titles=years)
        for i, year in enumerate(years):
            data = z[i*365 : (i+1)*365]
            display_year(data, year=year, fig=fig, row=i)
            fig.update_layout(height=250*len(years))
        return fig


    # Creating the calendar heatmap via internal functions and converting it to html: 
    z = np.random.randint(3, size=(200,))
    calendar_heatmap = display_year(z).to_html(full_html=False)
    context["calendar_heatmap"] = calendar_heatmap

    return render(request, "research_core/research_index.html", context=context)
# Importing Data
import pandas as pd

data = pd.read_excel('rdata.xlsx')
data.columns
africa_data = data[data['Continent'] == 'AF']
latin_america_data = data[data['Continent'] == 'LAT']

fertility = data['fertility']
female_literacy = data['female literacy']

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(fertility, female_literacy)

# Call the output_file() function and specify the name of the file
output_file('fert_lit.html')

# Display the plot
show(p)


# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
# Add a circle glyph to the figure p
p.circle(latin_america_data['fertility'], latin_america_data['female literacy'], color='blue', size=10, alpha=0.8)

# Add an x glyph to the figure p
p.x(africa_data['fertility'], africa_data['female literacy'], color='red', size=10, alpha=0.8)

# Specify the name of the file
output_file('fert_lit_separate.html')

# Display the plot
show(p)




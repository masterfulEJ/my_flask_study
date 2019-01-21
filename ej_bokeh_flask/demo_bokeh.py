from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from bokeh import palettes
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

# Load the Iris Data Set
iris_df = pd.read_csv("data/iris.data", 
    names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
feature_names = iris_df.columns[0:-1].values.tolist()

# Create the main plot
def create_figure(current_feature_name, bins):
    df = iris_df.groupby('Species')[current_feature_name].apply(
        lambda x: np.histogram(x, bins=10))

    p = figure(width=600, height=400)
    colors = palettes.Category10[len(feature_names)]
    for i, (nm, (hist, edges)) in enumerate(df.iteritems()):
        p.quad(
            top=hist, bottom=0,
            fill_color=colors[i], fill_alpha=0.4,
            left=edges[:-1], right=edges[1:],
            legend=nm
        )
    p.xaxis.axis_label = current_feature_name
    p.yaxis.axis_label = 'Count'
    return p

# Index page
@app.route('/')
def index():
    # Determine the selected feature
    current_feature_name = request.args.get("feature_name")
    if current_feature_name == None:
        current_feature_name = "Sepal Length"

    # Create the plot
    plot = create_figure(current_feature_name, 10)
        
    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    return render_template("bokeh_test.html", script=script, div=div,
        feature_names=feature_names,  current_feature_name=current_feature_name)

# With debug=True, Flask server will auto-reload 
# when there are code changes
if __name__ == '__main__':
	app.run(port=5000, debug=True)
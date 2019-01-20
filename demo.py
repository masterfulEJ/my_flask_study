from io import BytesIO
from flask import Flask, render_template, request, send_file, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')


app = Flask(__name__)

@app.route("/")
def index():
    age = {"Sam": 20, "Ken": 30, "Grace": 23, "Peter": 29}
    return render_template("index.html", ages=age)


@app.route('/data_analysis')
def data_analysis():
    x = pd.DataFrame(np.random.randn(5, 6), columns=list('ABCDEF'))
    return render_template("data_analysis.html",  data=x.to_html())


@app.route('/data_frame_analysis')
def data_frame_analysis():
    data = [['Peter',22,3.2,63.2],['John',21,4.6,67.8],['Steve',25,5.2,81.9],['Jane',20,4.4,73.2],['Paige',27,4.1,70.5]]
    df=pd.DataFrame(data,columns=['Name','Age','Height','Weight'])
    desc=df.describe(include='all')
    return render_template("data_frame_analysis.html",  data_frame=df.to_html(), stat=desc.to_html())


@app.route('/external_data_frame_analysis')
def external_data_frame_analysis():
    df = pd.read_csv("train.csv")
    return render_template("external_data_frame_analysis.html",  data=df.head(5).to_html())


@app.route('/donut_pie_chart/')
def donut_pie_chart():
    courses = 'Computer Science', 'Statisics', 'Physics', 'Economics','Calculus'
    students = [48, 43, 37, 83,45]
    pie_color = ("red", "green", "orange", "cyan", "blue")
    explode = (0.05,0.05,0.05,0.05,0.05)
    fig, ax = plt.subplots()
    ax.pie(students, colors = pie_color, labels=courses, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)
    inner_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(inner_circle)
    ax.axis('equal')
    ax.set_title("Course Attendance\n",fontsize=24)
    plt.tight_layout()
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/data_frame_visualization/')
def data_frame_visualization():
    fig, ax = plt.subplots()
    df=pd.read_csv("gasprice.csv")
    time=df['time']
    gasprice=df['value']
    plt.plot(time,gasprice, color='orange')
    plt.xlabel("Time (Year)")
    plt.ylabel("Gas Price")
    plt.title("Time Series of US Gasoline Prices ")
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/data_frame_analysis2')
def data_frame_analysis2():
    return render_template("data_frame_analysis2.html")


if __name__ == "__main__":
    app.run()

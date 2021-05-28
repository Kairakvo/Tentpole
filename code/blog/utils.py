#import plotly.express as xp
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    #plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(month,income, exp):
    # plt.switch_backend('AGG')
    # plt.figure(figsize=(8,8))
    # plt.title("Income and expenditure over the 12 months")
    # plt.plot(month,income)
    # plt.xticks(rotation=45)
    # plt.xlabel("Months")
    # plt.ylabel("Amount in Rands")
    # plt.tight_layout()
    graph = get_graph()
    return graph
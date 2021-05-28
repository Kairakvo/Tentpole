from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
from .models import Post
from .models import Customer
from .forms import MyForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import openpyxl
from . utils import get_plot
 
def my_form(request):
  data=[]
  if request.method == "POST":
    form = MyForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      file = request.FILES["file"]
      wb = openpyxl.load_workbook(file,data_only=True)
      worksheet = wb["Sheet1"]
      print(worksheet)
      excel_data = list()
      for col in worksheet.iter_cols():
        col_data = list()
        for cell in col:
          col_data.append(cell.value)
        excel_data.append(col_data)
      month = excel_data[0][1:]
      print("Months: ", month)
      income = excel_data[1][1:]
      print("Income: ",income)
      exp = excel_data[2][1:]
      print("Expenditure: ", exp)
      chart = get_plot(month, income, exp)
      data.append(month)
      data.append(income)
      data.append(exp)
      request.session['data'] = data
      return HttpResponseRedirect(reverse("blog:welcome"))
  else:
      form = MyForm()
      plot_div = MyForm()
  
  return render(request, 'cv-form.html', {'form': form})

def welcome(request):
    data = request.session.get('data')
    month =data[0]
    income =data[1]
    exp =data[2]
    fig = make_subplots(shared_xaxes=True)
    fig.add_trace(go.Scatter(x=month, y=income,
                        mode='lines', name='income',
                        opacity=0.8, marker_color='green'))
    fig.add_trace(go.Scatter(x=month, y=exp,
                        mode='lines', name='expendinture',
                        opacity=0.8, marker_color='green'))
    plot_div = plot(fig,output_type='div')
    return render(request,"response.html",{'plot_div':plot_div})

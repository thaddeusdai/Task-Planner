from django.contrib import messages
from accounts.models import Account
from .models import DataDb
import os
import random as rd
import matplotlib.pyplot as plt
from django.shortcuts import render
import datetime
import matplotlib
from io import BytesIO
import base64
matplotlib.use('Agg')

# Create your views here.


def make_graph(x, y):
    img = BytesIO()
    # img_file = "staticfiles/data_img/data.cf64bd57e027.png"
    # if os.path.isfile(img_file):
    #     os.remove(img_file)

    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
              7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

    plt.figure(figsize=(9, 4.5))
    plt.plot(x, y)
    plt.ylim(0, None)
    plt.xlim(0, None)
    plt.ylabel('Number of Task Done')
    plt.xlabel('Days')
    plt.title(
        f"Number of Task(s) done in {months[datetime.datetime.today().month]}")
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url


def get_data(request, _username):
    user = Account.objects.get(username=_username)

    # makes sure the user has a datatable
    today = datetime.datetime.today().day
    if not user.datadb_set.filter(day=today):
        create_datatable(user)
    user_data = user.datadb_set.all()

# gets the data from the beginning of the month to the current day
    y = []
    x = [i for i in range(1+datetime.datetime.today().day)]
    for data in user_data.order_by('day'):
        y.append(data.num_of_task)

# makes the graph using the x,y values
    plt = make_graph(x, y[:1+datetime.datetime.today().day])

    return render(request, 'view_data.html', {'plot_url': plt})


def create_datatable(user):

    # creates all the values for DataDb
    # used 32 since there are a maximum of 31 days in a month
    for i in range(32):
        data = DataDb(account=user, num_of_task=0, day=int(i))
        data.save()
    return

from django.shortcuts import render
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random as rd
import os
from .models import DataDb
from accounts.models import Account
from django.contrib import messages

# Create your views here.
def make_graph(x,y):
    img_file = "./accounts/static/data_img/data.jpg"
    if os.path.isfile(img_file):
        os.remove(img_file)   
    
    months = {1: "January", 2:"February", 3:"March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
        
    plt.figure(figsize=(9,4.5))
    plt.plot(x,y)
    plt.ylim(0, None)
    plt.xlim(0, None)
    plt.ylabel('Number of Task Done')
    plt.xlabel('Days')
    plt.title(f"Number of Task(s) done in {months[datetime.datetime.today().month]}")
    plt.savefig('accounts/static/data_img/data.jpg')
    plt.close()

def get_data(request, _username):
    user = Account.objects.get(username=_username)
    
    # makes sure the user has a datatable
    today = datetime.datetime.today().day
    if not user.datadb_set.filter(day=today):
        create_datatable(user)
    user_data = user.datadb_set.all()

# gets the data from the beginning of the month to the current day
    y = []
    x = [i for i in range (1+datetime.datetime.today().day)]
    for data in user_data:
        y.append(data.num_of_task)

# makes the graph using the x,y values  
    make_graph(x,y[:1+datetime.datetime.today().day])

    return render(request, 'view_data.html')

def create_datatable(user):

# creates all the values for DataDb
# used 32 since there are a maximum of 31 days in a month 
    for i in range(32):
        data = DataDb(account=user, num_of_task = 0, day = int(i))
        data.save()
    return
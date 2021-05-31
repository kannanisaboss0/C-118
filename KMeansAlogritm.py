#-----------------------------------------KMeansAlgoritm.py-----------------------------------------#
'''
Importing modules:
-KMeans :-sklearn.cluster
-numpy (np)
-plotly.epxress (px)
-seaborn (sns)
-pandas (pd)
-matplotlib.pyplot (plt)
-random (rd)
-time (tm)
'''
from sklearn.cluster import KMeans
import numpy as np
import plotly.express as px
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
import time as tm


#Defining a function to return a random hexadecimal color
def ChooseRandomColor():
  hexadecimal_string_final="#"
  hexadecimal_string="0123456ABCDEF"

  for inter_loop in range(6):
    rd_index=rd.randint(0,(len(hexadecimal_string)-1))
    hexadecimal_string_final=hexadecimal_string_final+hexadecimal_string[rd_index]

  return hexadecimal_string_final

#Defining a function to display an independent cluster
def ShowIndependentGroup(k_y_arg,df_iloc_arg,max_arg,x_label_arg,y_label_arg,x_column_arg,y_column_arg):
    
      plt.figure(figsize=(10,5))
      input_param=int(input("Enter group number:"))

      #Verifying whetehr the cluster desired to indpendently view is lesser than the total number of clusters requested
      #Case-1
      if(input_param<=max_arg and input_param>=1):
        input_graph_param=input_param-1
        color_param=ChooseRandomColor()
        sns.scatterplot(df_iloc_arg[k_y_arg==input_graph_param,x_column_arg],df_iloc_arg[k_y_arg==input_graph_param,y_column_arg],color=color_param,s=50,label="Group-{} ({})".format(input_param,color_param))
        plt.xlabel(x_label_arg)
        plt.ylabel(y_label_arg)
        plt.grid(False)
        plt.title("Group-{}".format(input_param))
        plt.show()
      
        continue_segregation=input("Show another group?")

        #Verifying whether the user wants to view anotehr cluster
        #Case-1
        if(continue_segregation=="Yes" or continue_segregation=="yes"):
          ShowIndependentGroup(k_y_arg,df_iloc_arg,max_arg,x_label_arg,y_label_arg,x_column_arg,y_column_arg)

        #Case-2  
        else:
          print("Request Accpeted")
          
          #Printing the ending message
          print("Thank You for using KMeansAlgoritm.py")  

      #Case-2    
      else:
        print("Request Terminated.")
        print("Invalid Input.")
        print("The group number should be within the 1 and total number of groups specified")
        
        #Printing the ending message
        print("Thank You for using KMeansAlgoritm.py")  


#Defining a function to segregate the datapoints using the KMeans-Method
def CreateKMeansGroupingPlot(df_iloc_arg):
  value_int_param=int(input("Please enter number of clusters to be made:"))

  #Verifying whether the number of clusters specified is below 10 and above 1
  #Case-1
  if(value_int_param<=10 and value_int_param>=1 ):
    kmeans_param=KMeans(n_clusters=value_int_param,init="k-means++",random_state=42)
    kmeans_param_y=kmeans_param.fit_predict(df_iloc_arg)

    plt.figure(figsize=(10,5))

    x_column=int(0)
    y_column=int(1)

    x_label="Size"
    y_label="Light"

    axis_list=["Unusable_Element","Size","Light"]  
    axis_count=0

    for axis in axis_list[1:]:
      axis_count+=1
      print("{}:{}".format(axis_count,axis))

    axis_input_param=int(input("Please enter the index of the field desired to be the x-axis"))  
    axis_choice=axis_list[axis_input_param]

    #Assessing the user's choice on the field representing the x-axis
    #Case-1
    if(axis_input_param==1):
      x_column=0
      y_column=1

      x_label="Size"
      y_label="Light"

    #Case-2
    elif(axis_input_param==2):
      x_column=1
      y_column=0

      x_label="Light"
      y_label="Size"

    for plot_loop in range(0,value_int_param):
      label_value_param=plot_loop+1
    
      color_param=ChooseRandomColor()

      sns.scatterplot(df_iloc_arg[kmeans_param_y==plot_loop,x_column],df_iloc_arg[kmeans_param_y==plot_loop,y_column],color=color_param,label="Group-{} ({})".format(label_value_param,color_param))

    sns.scatterplot(kmeans_param.cluster_centers_[:,x_column],kmeans_param.cluster_centers_[:,y_column],color="silver",s=75,marker=",",label="Centroid")
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.grid(False)

    plt.title("{} and {} Groups:-Method-KMeans".format(x_label,y_label))

    plt.show()

    show_independent_param=input("Display a single group seperately?")
    #Assessing the user's choice on viewing a graph independently
    #Case-1
    if(show_independent_param=="Yes" or show_independent_param=="yes"):
      ShowIndependentGroup(kmeans_param_y,df_iloc_arg,value_int_param,x_label,y_label,x_column,y_column)

    #Case-2  
    else:
      print("Request Accpeted")
      print("Thank You for using KMeansAlgoritm.py")

  #Case-2
  else:
    print("Request Terminated")    
    print("Invalid Input.")
    print("The total number of groups should be within the range of 1 and 10.")

    #Printing the ending message
    print("Thank You for using KMeansAlgoritm.py")  


#Reading data from the fle
df=pd.read_csv("data.csv")

print("Welcome to KMeansAlogritm.py. We provide cluster segregation through them K-Means method.")

view_information=input("Do not know what the K-Means method is?(:- I Don't Know or I Know)")

#Verifying the user's choice whether they have pre-requisiste knowledge of Logisitic Regression
#Case-1
if(view_information=="I Don't Know" or view_information=="i don't know" or view_information=="I don't know" or view_information=="I Don't know" or view_information=="I don't Know"):
  print("What is the K-Means method?")
  tm.sleep(2.3)
  print("The K-Means method is method of data segregation, where a number of datapoints,e0 e1...en, are categroised into clusters,k0,k1...kv")
  tm.sleep(2.1)
  print("Each cluster has a mean assigned to it. The closest mean to the datapoints are then categorised into cluster of the mean.")
  tm.sleep(1.2)
  print("The mean values are called -centroids-")
  tm.sleep(1.1)
  print("It is hypothetically proposed that a datapoint, immaterial to size or dispersion,can only possess 10 well-defined clusters using the K-Means method.")
  tm.sleep(2.3)
  print("The K-Means methods is used in several areas of segregation such as:")
  tm.sleep(1.3)
  print("1. Accurate division of human capabilities into groups.")
  tm.sleep(1.0)
  print("2. Categorisation of organisms into several genuses and species, using physical statistics, by biologists.")
  tm.sleep(1.9)
  print("3. Divison of grade scores into letters such as 'A+','D-'")
  tm.sleep(2.3)
  print("To know more, visit: 'https://en.wikipedia.org/wiki/K-means_clustering'")
  tm.sleep(3.4)

#Case-2  
else:
  print("Request Accepted.")  
  tm.sleep(0.5)

print("Loading Data...")
tm.sleep(2.3)

df_iloc=df.iloc[:,[0,1]].values

scatter_plot=px.scatter(df,x="Size",y="Light",color="Light",title="Size and Light:-Scatter Graph (Original Data)")

scatter_plot.show()

WCSS=[]

for loop_value in range(1,11):

  kmeans=KMeans(n_clusters=loop_value,init="k-means++",random_state=42)
  kmeans.fit(df_iloc)

  value_intertia=kmeans.inertia_
  WCSS.append(value_intertia)

plt.figure(figsize=(10,5))

sns.lineplot(range(1,11),WCSS,marker="o",color="purple")

plt.xlabel("Number Of Clusters")
plt.ylabel("WCSS")

plt.title("Elbow-Method")

plt.show()

CreateKMeansGroupingPlot(df_iloc)
#-----------------------------------------KMeansAlgoritm.py-----------------------------------------#
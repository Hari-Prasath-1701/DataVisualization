from flask import Flask

from flask import Flask, render_template, Response, request, redirect, url_for
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

def pie_charts():
	mydb = mysql.connector.connect(host="ur host",port="ur port",user="username",passwd="urpassword",database="dbname",)

	mycursor = mydb.cursor()
	# 1)
	sql = "select distinct status,count(status) from chart group by status"
	mycursor.execute(sql)
	records=mycursor.fetchall()

	lang=[]
	stud=[]

	for row,n in records:
		lang.append(row)
		stud.append(n)

	fig = plt.figure()
	ax = fig.add_axes([0,0,1,1])
	ax.axis('equal')

	plt.title("Statistics On Parts Created")
	ax.pie(stud, labels = lang,autopct='%1.2f%%')
	plt.savefig("G:/FlaskCopy/static/PieChart.png")
	mycursor.close()




def bar_charts():
	mydb = mysql.connector.connect(host="ur host",port="ur port",user="username",passwd="urpassword",database="dbname",)

	mycursor = mydb.cursor()
	# 1)
	sql = "select distinct status,count(status) from chart group by status"
	sqll="select distinct CreatedBy,count(CreatedBy) from chart group by CreatedBy"
	sqlll = "select distinct Approver,count(Approver) from chart group by Approver"
	mycursor.execute(sql)
	records=mycursor.fetchall()

	lang=[]
	stud=[]

	for row,n in records:
		lang.append(row)
		stud.append(n)



	#1)BarChart----------------
	print(lang)
	print(stud)
	f = plt.figure(1)
	y_pos=np.arange(len(lang))
	plt.barh(y_pos,stud,align='center',alpha=0.5,color=(0.2,0.4,0.6,0.8))
	plt.yticks(y_pos,lang)
	plt.title("Statics on Part Status")
	plt.xlabel("Count of Part Number")
	for index, value in enumerate(stud):
		plt.text(value, index, str(value))
	f.savefig("G:/FlaskCopy/static/BarChart.png", bbox_inches='tight')

	#2) BarChart2-----------------
	g = plt.figure(2)
	mycursor.execute(sqll)
	recordss=mycursor.fetchall()
	langg=[]
	studd=[]
	for row,n in recordss:
		langg.append(row)
		studd.append(n)
	y_pos=np.arange(len(langg))
	plt.barh(y_pos,studd,align='center',alpha=0.5,color=(0.2,0.4,0.6,0.8))
	plt.yticks(y_pos,langg)
	plt.title("Statics on Parts Created By")
	plt.xlabel("Total")
	for index, value in enumerate(studd):
		plt.text(value, index, str(value))
	g.savefig("G:/FlaskCopy/static/BarChart1.png", bbox_inches='tight')



	#3) BarChart3 --------
	h = plt.figure(3)
	mycursor.execute(sqlll)
	recordss=mycursor.fetchall()
	langgg=[]
	studdd=[]
	for row,n in recordss:
		langgg.append(row)
		studdd.append(n)
	y_pos=np.arange(len(langgg))
	plt.barh(y_pos,studdd,align='center',alpha=0.5,color=(0.2,0.4,0.6,0.8))

	plt.yticks(y_pos,langgg)
	plt.title("Statics on Parts Approved By")
	plt.xlabel("Count")
	for index, value in enumerate(studdd):
		plt.text(value, index, str(value))
	h.savefig("G:/FlaskCopy/static/BarChart2.png", bbox_inches='tight')

	mycursor.close()


@app.route('/')
def hello_world():
	bar_charts()
	return  render_template('index.html')


@app.route('/move')
def move():
    return render_template('DV.html')

@app.route('/home')
def home():
	return  render_template('index.html')





@app.route('/db')
def db():
	mydb = mysql.connector.connect(host="localhost",port="3308",user="root",passwd="root",database="swissrank",)
	mycursor = mydb.cursor()
	sql = "select * from partdetails order by trackerid DESC"
	mycursor.execute(sql)
	records=mycursor.fetchall()
	#return render_template("viewdb.html", value=records)

	mydb = mysql.connector.connect(host="localhost",port="3308",user="root",passwd="root",database="swissrank",)
	mycursor = mydb.cursor()
	sql = "select * from partstatustracker"
	mycursor.execute(sql)
	records1=mycursor.fetchall()
	return render_template("viewdb.html", values=records,values1=records1)

	




if __name__ == '__main__':
   app.run(debug=True)


from function import *
from dataClass import *


data = Data()
window = Tk()
window.title('Mathematical statistics')
window.geometry("1200x500")
myFont = font.Font(family='Courier', size=10, weight='bold')

lb = Label(window, text='Enter the path to the text file: ', background="#585858", foreground="#FF8000")
lb.grid(row=0, column=0)

fileName_inp = Entry(window)
fileName_inp.grid(row=1, column=0)


def fileInput():
    fileName = fileName_inp.get()
    data.lst = readFromFile(fileName)


textfile_bt = Button(window, text='Use file', command=fileInput, background="#585858", foreground="#FF8000")
textfile_bt.grid(row=2, column=0)

def generateList():
    mn = float(border_left_entry.get())
    mx = float(border_right_entry.get())
    cnt = int(count_entry.get())
    data.lst = generate(mn, mx, cnt)

button = Button(window, text='Generate', command=generateList, background="#585858", foreground="#FF8000")
button.grid(row=4, column=2)

lb = Label(window, text='Enter your data: ', background="#585858", foreground="#FF8000")
lb.grid(row=0, column=2)

lb_border_left = Label(window, text='Min value: ')
lb_border_left.grid(row=1, column=1)

border_left_entry = Entry(window)
border_left_entry.grid(row=1, column=2)

lb_border_right = Label(window, text='Max value: ')
lb_border_right.grid(row=2, column=1)

border_right_entry = Entry(window)
border_right_entry.grid(row=2, column=2)

lb_count = Label(window, text='Count: ')
lb_count.grid(row=3, column=1)

count_entry = Entry(window)
count_entry.grid(row=3, column=2)


def Dia_chastot():
    show_bar(data.lst)


dia_chastot_but = Button(window, text='Diagram frequency', command=Dia_chastot, foreground="#F7D358")
dia_chastot_but.grid(row=8, column=2)


def Pol_chastot():
    show_plot(data.lst)


pol_chastot_but = Button(window, text='Ground frequency ', command=Pol_chastot,  foreground="#F7D358")
pol_chastot_but.grid(row=9, column=2)


def His_chastot():
    show_hist(data.lst)


his_chastot_but = Button(window, text='Histogram frequency ', command=His_chastot, foreground="#F7D358")
his_chastot_but.grid(row=10, column=2)


def Tables():

    arr = getCntNew(data.lst)
    headers = [["Xi", "Ni"]]
    headers.extend(arr)
    generateWindowWithInfo(headers)


table_but = Button(window, text='Tables', command=Tables, foreground="#F7D358")
table_but.grid(row=7, column=0)


def Interval_Tables():
    arr = getIntervalCntNew(data.lst)
    headers = [["[Zi, Zi+1]", "Z", "Ni"]]
    headers.extend(arr)
    generateWindowWithInfo(headers)


table_but = Button(window, text='Interval tables', command=Interval_Tables, foreground="#F7D358")
table_but.grid(row=7, column=1)


def generateWindowWithInfo(arr):
    output_window = Tk()
    output_window.title('Info')
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            Label(output_window, text=str(arr[i][j])).grid(row=i, column=j)


def info():
    inf = getInfo(data.lst)
    for i in range(len(inf)):
        inf[i][1] = round(float(inf[i][1]), 2)
    generateWindowWithInfo(inf)


discrete_info_but = Button(window, text='Characteristics', command=info,  foreground="#F7D358")
discrete_info_but.grid(row = 8, column = 0)

def interval_info():

    inf = getIntervalInfo(getIntervalCntNew(data.lst))
    for i in range(len(inf)):
        inf[i][1] = round(float(inf[i][1]), 2)
    generateWindowWithInfo(inf)

interval_info_but = Button(window, text = 'Interval Characteristics', command = interval_info, foreground="#F7D358")
interval_info_but.grid(row = 8, column = 1)

def emp():
    show_emp(data.lst)


emp_but = Button(window, text='Empirical distribution function interval', command=emp, foreground="#F7D358")
emp_but.grid(row=11, column=1)

def emp2():
    show_emp2(data.lst)
emp_but2 = Button(window, text='Empirical distribution function discrete', command=emp2, foreground="#F7D358")
emp_but2.grid(row=11, column=0)


################
def generateUniformDistr(elemCnt, n):
	lst = []
	for i in range(n):
		lst.append([str(round(n/elemCnt,2)), str(round(elemCnt / n,2))])
	return lst

def discr_uniform():
	arr = getCntNew(data.lst)
	ind = 0
	r = len(arr)-1
	for elem in generateUniformDistr(len(data.lst), len(arr)):
		arr[ind].append(elem[0])
		arr[ind].append(elem[1])
		ind += 1
	headers = [["x_i", "m_i", "p_i", "n*p_i"]]
	headers.extend(arr)
	x2_emp = 0
	for i in range(1, len(arr)):
		x2_emp += ((float(arr[i][1])-float(arr[i][3]))**2) / float(arr[i][3])

	headers.append(["X2_emp","","",str(round(x2_emp, 2))])
	alpha = list(open("table.txt").readlines())
	x2_crit = float(alpha[r].replace(",", "."))
	headers.append(["X2_crit","","",str(alpha[r])])
	headers.append(["Result:","","", ("Hipothesis is right" if x2_emp <= x2_crit else "Hipothesis is wrong")])
	generateWindowWithInfo(headers)

def generateUniformDistrInterval(elemCnt, n):
	lst = []
	for i in range(n):
		lst.append([str(round(1/n,2)), str(round(elemCnt / n,2))])
	return lst

def interval_uniform():
	arr = getIntervalCntNew(data.lst)
	for elem in arr:
		elem[0] = str(elem[0])
		elem.pop(1)
	ind = 0
	r = len(arr)-1
	for elem in generateUniformDistrInterval(len(data.lst), len(arr)):
		arr[ind].append(elem[0])
		arr[ind].append(elem[1])
		ind += 1
	headers = [["[l, r]", "m_i", "p_i", "n*p_i"]]
	headers.extend(arr)
	x2_emp = 0
	for i in range(1, len(arr)):
		x2_emp += ((float(arr[i][1])-float(arr[i][3]))**2) / float(arr[i][3])

	headers.append(["X2_emp","","",str(round(x2_emp, 2))])
	alpha = list(open("table.txt").readlines())
	x2_crit = float(alpha[r].replace(",", "."))
	headers.append(["X2_crit","","",str(alpha[r])])
	headers.append(["Result:","","", ("Hipothesis is right" if x2_emp <= x2_crit else "Hipothesis is wrong")])
	generateWindowWithInfo(headers)

discr_uniform_but = Button(window, text='Discrete exponential distribution', command=discr_uniform,  foreground="#F7D358")
discr_uniform_but.grid(row=9, column=0)

interv_uniform_but = Button(window, text='Interval exponential distribution', command=interval_uniform,  foreground="#F7D358")
interv_uniform_but.grid(row=9, column=1)


def C(n, k):
	return (math.factorial(n) / (math.factorial(k)*math.factorial(n-k)))


def getBin(n, k, p):
	return (p**k)*((1-p)**(n-k))*C(n, k)

def generateBinDistr(elemCnt, n):
	lst = []
	for i in range(n):
		lst.append([str(round(getBin(n, i, 0.5),2)), str(round(elemCnt * getBin(n, i, 0.5),2))])
	return lst

def discr_bin():
	arr = getCntNew(data.lst)
	ind = 0
	r = len(arr)-1
	for elem in generateBinDistr(len(data.lst), len(arr)):
		arr[ind].append(elem[0])
		arr[ind].append(elem[1])
		ind += 1
	headers = [["x_i", "m_i", "p_i", "n*p_i"]]
	headers.extend(arr)
	x2_emp = 0
	for i in range(1, len(arr)):
		x2_emp += ((float(arr[i][1])-float(arr[i][3]))**2) / float(arr[i][3])

	headers.append(["X2_emp","","",str(round(x2_emp, 2))])
	alpha = list(open("table.txt").readlines())
	x2_crit = float(alpha[r].replace(",", "."))
	headers.append(["X2_crit","","",str(alpha[r])])
	headers.append(["Result:","","", ("Hypothesis is right" if x2_emp <= x2_crit else "Hypothesis is wrong")])
	generateWindowWithInfo(headers)

def generateBinInterval(elemCnt, n):
	lst = []
	for i in range(n):
		lst.append([str(round(getBin(n, i, 0.5),2)), str(round(elemCnt * getBin(n, i, 0.5),2))])
	return lst

def interval_bin():
	arr = getIntervalCntNew(data.lst)
	for elem in arr:
		elem[0] = str(elem[0])
		elem.pop(1)
	ind = 0
	r = len(arr)-1
	for elem in generateBinInterval(len(data.lst), len(arr)):
		arr[ind].append(elem[0])
		arr[ind].append(elem[1])
		ind += 1
	headers = [["[l, r]", "m_i", "p_i", "n*p_i"]]
	headers.extend(arr)
	x2_emp = 0
	for i in range(1, len(arr)):
		x2_emp += ((float(arr[i][1])-float(arr[i][3]))**2) / float(arr[i][3])

	headers.append(["X2_emp","","",str(round(x2_emp, 2))])
	alpha = list(open("table.txt").readlines())
	x2_crit = float(alpha[r].replace(",", "."))
	headers.append(["X2_crit","","",str(alpha[r])])
	headers.append(["Result:","","", ("Hypothesis is right" if x2_emp <= x2_crit else "Hypothesis is wrong")])
	generateWindowWithInfo(headers)

discr_bin_but = Button(window, text='Discrete Binomial Distribution', command=discr_bin, foreground="#F7D358")
discr_bin_but.grid(row=10, column=0)

interv_bin_but = Button(window, text='Interval Binomial Distribution', command=interval_bin, foreground="#F7D358")
interv_bin_but.grid(row=10, column=1)
window.geometry("800x300")
window.mainloop()
{}
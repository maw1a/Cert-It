from PIL import Image, ImageDraw, ImageFont
import pandas as pd


import zipfile
import os
from os.path import basename

from datetime import datetime

df = pd.read_csv('data_1.csv')
df = df.applymap(str)

im = Image.open("Template7_TBD.png")

d = ImageDraw.Draw(im)



def paste(cordinates ,text_color, font , font_size ,string):
	
	f_font = ImageFont.truetype(font,font_size)

	d.text(cordinates, string , align='center',fill =text_color, font = f_font)


def paste_bold(cordinates ,text_color, font , font_size ,string):
	
	f_font = ImageFont.truetype(font,font_size)

	new_x = cordinates[0] + 1
	new_y = cordinates[1] + 1
	new_xx = cordinates[0] - 1
	new_yy = cordinates[1] -1

	up = (new_x , new_y)
	down = (new_xx , new_yy)

	d.text(cordinates, string , fill =text_color, font = f_font)
	d.text(up, string , fill =text_color, font = f_font)
	d.text(down, string , fill =text_color, font = f_font)



def center_align(name):

	f_font = ImageFont.truetype(oswald,110)
	bounding_box = [580,540 , 1500 , 790]
	x1, y1, x2, y2 = bounding_box  

	w, h = d.textsize(name, font=f_font)

	x = (x2 - x1 - w)/2 + x1
	y = (y2 - y1 - h)/2 + y1

	d.text((x, y), name,      fill =(0,0,139), align='center', font=f_font)
	d.text((x+2, y+2),name ,  fill =(0,0,139), align='center', font=f_font)
	d.text((x-2, y-2), name,  fill =(0,0,139), align='center', font=f_font)


def create_data(df):

	for index, rows in df.iterrows(): 

	    my_list = [rows.Name, rows.Company_Name, rows.Certificate,rows.Certifier1 , rows.Certifier_Position1,
	    			rows.Certifier2, rows.Certifier_Position2, rows.Date] 
	       
	    rows_list.append(my_list)


def convert_date(string):

	date_time_obj = datetime.strptime(string, '%d/%m/%Y')

	month_format = date_time_obj.strftime("%e/%B/%Y")

	month_format = str(month_format)

	new_format = month_format.replace("/", " ")
	string_list = new_format.split()

	if string_list[0] == '1' or string_list[0] == '11' or string_list[0] == '21' or string_list[0] == '31':

		string_list[0] += 'st'

	elif string_list[0] == '2' or string_list[0] == '12' or string_list[0] == '22':

		string_list[0] += 'nd'

	elif string_list[0] == '3' or string_list[0] == '13' or string_list[0] == '23':

		string_list[0] += 'rd'
	else:
		string_list[0] = string_list[0] + 'th'

	string = ' '.join(string_list)

	return string




georgia = 'georgia.ttf'
arial = 'arial.ttf'
oswald = r'C:\Users\ROSHAN\Certificate Maker\Fonts\Oswald-Bold.ttf'
oswald_light = r'C:\Users\ROSHAN\Certificate Maker\Fonts\Oswald-Light.ttf'

rows_list = [] 

create_data(df)

for rows in rows_list:
	
	paste_bold((810,200) , 	(218,165,32), oswald_light, 90 ,rows[1])	

	paste_bold((500,320) , 	(218,165,32), oswald_light, 110 ,rows[2])

	paste((810,480) , (0,0,128), oswald_light, 80 , 'is presented to')

	if len(rows[0]) > 15:

		new_name = rows[0].replace(" ", "\n")
		center_align(new_name)
	
	else:
		center_align(rows[0])

	paste((810,770) , (218,165,32),oswald_light, 50 , 'On '  + convert_date(rows[-1]))

	paste((510,850) , 	(0,0,128),oswald_light , 60 , 'For potraying examplary skills and completing')
	paste((510,915) , 	(0,0,128),oswald_light , 60 , 'all assigned tasks')

	paste_bold((480, 1075) , (218,165,32), georgia ,60 , rows[3])
	paste((530, 1175), (0,0,128) , oswald_light , 40 , rows[4])

	paste_bold((1200,1075), (218,165,32) ,georgia , 60 , rows[5])
	paste((1200 , 1175), (0,0,128) , oswald_light , 40 , rows[6])

	d.line([(500, 460), (1460,460)] , fill ="darkblue", width = 7) 

	im.save('Certificate_' + rows[0] + '.png')

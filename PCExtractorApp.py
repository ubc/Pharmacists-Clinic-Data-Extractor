#############################################################################################################################################
#  Copyright (c) 2019. The Pharmacists Clinic, Faculty of Pharmaceutical Sciences, University of British Columbia. All Rights Reserved.
#  This software is published under the GPL GNU General Public License.
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation, either version 3
#  of the License, or (at your option) any later version.
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, <https://www.gnu.org/licenses/>.
#
#  This software was written for
#    The Pharmacists Clinic 
#    Faculty of Pharmaceutical Sciences
#    University of British Columbia
#    Vancouver, British Columbia, Canada
#############################################################################################################################################

#################################################################################
#
#	The Pharmacists Clinic (PC) Data Extractor 
#		Enables custom query development for the PC OSCAR EMR
# 
#################################################################################

import tkinter as tk
# from tkinter import messagebox
from tkinter import filedialog
import os
import csv

LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)
MEASUREMENTS_FILE_NAME = "measurements.in"
TABLE_SCHEMA_NAME = "oscar.csv"
STANDARD_SIZE = "384x620"
MED_SIZE = "568x620"
LARGE_SIZE = "570x640"
global DATABASESCHEMA 
DATABASESCHEMA = dict()

class PCExtractorApp(tk.Tk):
	# this will always run when you initialize, args variables, kwargs are dictionaries
	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		self.title("Pharmacists Clinic Data Extractor")
		self.geometry(STANDARD_SIZE)

		# photoFrame = tk.Frame(self, height=500, width=450)
		# photoFrame = tk.Frame(self)
		# photoFrame.grid(row=0, column=0, sticky="NSEW")

		# photo = tk.PhotoImage(file="test4.gif")
		photo = tk.PhotoImage(data=b'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')
		# photoLabel= tk.Label(photoFrame, image=photo)
		photoLabel= tk.Label(self, image=photo, font=SMALL_FONT)
		photoLabel.image = photo
		photoLabel.grid(row=0, column=0, sticky="W")

		container = tk.Frame(self)

		container.grid(row=1,column=0, sticky="NSEW")

		acknowledgements = tk.Label(self, text="Built by Jamil Devsi. Supervised by Jason Min.", font=SMALL_FONT, fg="black")
		acknowledgements.grid(row=2,column=0, sticky="NSEW")
		# container.grid_rowconfigure(0, weight=1)
		# container.grid_columnconfigure (0, weight=1)

		self.frames = {}

		# for f in (StartPage, MeasurementsModule, HealthCareTeamModule, DemographicsModule):
		for f in (StartPage, MeasurementsModule, DemographicsModule):
			frame= f(container, self)
			self.frames[f] = frame
			frame.grid(row=1, column=0, sticky="NSEW")

		self.show_frame(StartPage, STANDARD_SIZE)

		# Class bindings for common functions
		self.bind_class("Text", "<Control-a>", self.select_all)
		self.bind_class("Text", "<Command-a>", self.select_all)
		self.bind_class("Text", "<Control-c>", self.copy)
		self.bind_class("Text", "<Command-c>", self.copy)
		self.bind_class("Text", "<Control-v>", self.paste)

		# self.bind_class("Entry", "<Control-a>", self.select_all)
		# self.bind_class("Entry", "<Command-a>", self.select_all)
		self.bind_class("Entry", "<Control-c>", self.copy)
		self.bind_class("Entry", "<Command-c>", self.copy)
		self.bind_class("Entry", "<Control-v>", self.paste)
		# self.bind_class("Text", "Button-3", self.rClicker)
		# container.bind('<Button-3>', self.rClicker, add='')

		self.cmenu= tk.Menu(self)
		self.cmenu.add_command(label="Copy", command=self.copy)
		self.cmenu.add_command(label="Paste", command=lambda: self.paste(self))
		# self.cmenu.add_command(label="Paste", command=lambda: tk.Entry.event_generate(self, self.paste))
		self.bind_class("Text", "<Button-2><ButtonRelease-2>", self.popup)
		self.bind_class("Entry", "<Button-2><ButtonRelease-2>", self.popup)
		# self.bind("<Button-3><ButtonRelease-3>", self.popup)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		# self.grid_columnconfigure(1, weight=1)
		# self.grid_columnconfigure(2, weight=1)
		# self.grid_columnconfigure(3, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=1)
		self.grid_rowconfigure(2, weight=0)


	def popup(self, event):
		self.cmenu.post(event.x_root, event.y_root)	
		
	def show_frame(self, cont, size):
		
		frame = self.frames[cont] # container frame.
		
		frame.tkraise()
		self.geometry(size)


	def displayMessage(self, title, messsage):
		tk.messagebox.showinfo(title, messsage)

	def select_all(self, event):
		event.widget.tag_add("sel", "1.0", "end")
	
	def copy(self, event=None):
		self.clipboard_clear()
		text= self.selection_get()
		self.clipboard_append(text)

	def popupBox(title, message, size, wrap, side):
		popup = tk.Tk()
		popup.wm_title(title)
		label = tk.Label(popup, text=message, font=SMALL_FONT, wraplength=wrap, justify = side)
		label.pack(side="top", fill="x", pady=10)
		# label.grid(row=0,column=0, sticky="E")
		button = tk.Button(popup, text="Okay", font=SMALL_FONT,command = popup.destroy)
		button.pack()
		# button.grid(row=1, column=0)
		popup.geometry(size)
		popup.mainloop()
	
	def paste(self, event):
		text = self.selection_get(selection='CLIPBOARD')
		try:
			print(text)
			event.widget.insert("insert", text) # inserts at the end of the listbox.
		# self.insert('insert', text)
		except:
			# print("error could not paste")
			e = event.tk_focusNext().tk_focusNext().tk_focusNext()
			e.focus_get().insert("insert", text)
			# print(e)	

class StartPage(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label=tk.Label(self, text="Welcome to the Pharmacists Clinic Data Extractor Query Builder", font=LARGE_FONT)
		

		measurementsButton = tk.Button(self, text="Measurements Query Builder", font=SMALL_FONT,
			command=lambda: controller.show_frame(MeasurementsModule, MED_SIZE))
		

		# healthCareTeamButton = tk.Button(self, text="Health Care Team", font=SMALL_FONT,
		# 	command=lambda: controller.show_frame(HealthCareTeamModule, STANDARD_SIZE))
		
		# uncomment when beta no longer needed
		# demographicsButton = tk.Button(self, text="Demographics Query Builder", font=SMALL_FONT,
		# 	command=lambda: controller.show_frame(DemographicsModule, LARGE_SIZE))
		demographicsButton = tk.Button(self, text="Demographics Query Builder [beta]", font=SMALL_FONT,
			command=lambda: self.displayBeta(controller, DemographicsModule, LARGE_SIZE))

		disclaimer=tk.Label(self, text="This software is made available to you as is. Use this application at your own risk.", font=SMALL_FONT, wraplength=300)
		# release=tk.Label(self, text="Demo release not for distribution.", font=SMALL_FONT, wraplength=300)

		disclaimerButton =  tk.Button(self, text="Legal Notices", font=SMALL_FONT,
			command=lambda: PCExtractorApp.popupBox("Legal Notices", "The Pharmacists Clinic, Faculty of Pharmaceutical Sciences at the University of British Columbia or its representatives cannot be held liable for improper use of this software. The software is provided with no warranty and is subject to the terms of the GPL License found in the source code. It is not recommended to pull too much data from your electronic medical record at once.\n\n Copyright (c) 2019. The Pharmacists Clinic, Faculty of Pharmaceutical Sciences, University of British Columbia. All Rights Reserved. ", "420x175", 400, "center"))

		label.grid(row=0, column=0, sticky="NSEW")	
		measurementsButton.grid(row=1, column=0, sticky="NSEW")
		# healthCareTeamButton.grid(row=2, column=0, sticky="NSEW")
		# demographicsButton.grid(row = 3, column=0, sticky="NSEW")
		demographicsButton.grid(row = 2, column=0, sticky="NSEW")
		disclaimer.grid(row = 3, column = 0, sticky= "NSEW", padx=10, pady=10)
		disclaimerButton.grid(row =4, column=0)
		# release.grid(row = 5, column = 0, sticky= "NSEW", padx=10, pady=10)

		self.grid_columnconfigure(0, weight = 0)
		# self.grid_columnconfigure(0, weight = 1)
		self.grid_rowconfigure(0, weight = 0)
		self.grid_rowconfigure(1, weight = 0)
		self.grid_rowconfigure(2, weight = 0)
		self.grid_rowconfigure(3, weight = 0)
		self.grid_rowconfigure(4, weight = 0)
		self.grid_rowconfigure(5, weight = 0)

	
	# Handle beta note - remove once beta no longer required
	def displayBeta(self, controller, module, size):
		controller.show_frame(module, size)
		PCExtractorApp.popupBox("Notification", "This is a beta release with limited functionality. Please click \"Help\" for more information on how to use this module.", "300x100", 250, "center")


## Class reponsible for building the Measurements Module Query Builder
class MeasurementsModule(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label=tk.Label(self, text="Measurements Module Query Builder", font=LARGE_FONT)


		mTypesLabel = tk.Label(self,text="Measurement Types", font=SMALL_FONT)
		sTypesLabel = tk.Label(self,text="Selected Types", font=SMALL_FONT)

		options_listbox = tk.Listbox(self, selectmode="SINGLE", font=SMALL_FONT)
		selection_listbox = tk.Listbox(self, selectmode="SINGLE", font=SMALL_FONT)


		displayMessage = tk.Text(self, font=SMALL_FONT)

		reVar = tk.IntVar()
		researchButton = tk.Checkbutton(self, text="Anonymize", font=SMALL_FONT
			, variable=reVar, anchor="w")
		researchButton.var= reVar

		#Button Frames
		buttonFrame = tk.Frame(self)
		addButton = tk.Button(buttonFrame, text="Add", font=SMALL_FONT,
			command=lambda: self.updateListbox(options_listbox.get("active"), selection_listbox))
		addButton.pack(side="top", fill="both")
		removeButton = tk.Button(buttonFrame, text="Remove", font=SMALL_FONT,
			command=lambda: selection_listbox.delete(selection_listbox.curselection(),selection_listbox.curselection()))
			# command=lambda: selection_listbox.delete(selection_listbox.curselection()))
		removeButton.pack(fill="both")


		# addAllButton = tk.Button(buttonFrame, text="Add All", font=SMALL_FONT,
		# 	command="")
		# addAllButton.pack(fill="both")

		removeAllButton = tk.Button(buttonFrame, text="Remove All", font=SMALL_FONT,
			command=lambda: selection_listbox.delete(0,'end'))
		removeAllButton.pack(side="bottom",fill="both")	

		generateButton = tk.Button(self, text="Generate", font=SMALL_FONT,
			# command= lambda: self.runQuery(selection_listbox, fromDate, toDate, displayMessage))
			command= lambda: self.buildMeasurementsQuery(selection_listbox.get("0","end"), displayMessage, reVar))

		returnButton = tk.Button(self, text="Back", font=SMALL_FONT,
			command=lambda: controller.show_frame(StartPage, STANDARD_SIZE))
		clearButton = tk.Button(self, text="Clear", font=SMALL_FONT,
			command=lambda: displayMessage.delete('1.0', "end")) 

		uploadMeasurementButton = tk.Button(self, text="Upload Measurement Types", font=SMALL_FONT, 
			command= lambda: self.loadMeasurementTypes(displayMessage, options_listbox))

		#### Search Box ####
		# searchFrame = tk.Frame(self) #if button may need the frame, if no button then dont need the frame.
		searchVar = tk.StringVar()
		searchBox = tk.Entry(self, textvariable=searchVar,font=SMALL_FONT)
		# searchBox = tk.Entry(searchFrame, textvariable=searchVar,font=SMALL_FONT)
		# searchBox.pack()
		searchVar.set("Type here to search")
		searchVar.trace("w", lambda x, y, z: self.parseMeasurementsFile(options_listbox, searchVar.get()))
		######################

		# +---------|---------|---------+
		# |         |         |         |
		label.grid(row=0,column=0, columnspan=3)
		mTypesLabel.grid(row=1,column=0)
		sTypesLabel.grid(row=1,column=2)
		options_listbox.grid(row=2, column=0)
		selection_listbox.grid(row=2, column=2)
		buttonFrame.grid(row=2, column=1)
		generateButton.grid(row=3, column=1)
		researchButton.grid(row=3, column=2)
		searchBox.grid(row=3, column=0)
		# searchFrame.grid(row=3, column=0)
		
		displayMessage.grid(row=4, column=0, columnspan=3)
		returnButton.grid(row=5, column=0, sticky="W")
		clearButton.grid(row=5, column=2, sticky="E")
		uploadMeasurementButton.grid (row=5, column=1)


		self.parseMeasurementsFile(options_listbox, '')

		# self.grid_columnconfigure(0, weight = 0)
		# self.grid_columnconfigure(1, weight = 0)
		# self.grid_columnconfigure(2, weight = 0)
		# self.grid_rowconfigure(0, weight = 0)
		# self.grid_rowconfigure(1, weight = 0)
		# self.grid_rowconfigure(2, weight = 0)
		# self.grid_rowconfigure(3, weight = 0)
		# self.grid_rowconfigure(4, weight = 0)
		# self.grid_rowconfigure(5, weight = 0)
		# self.grid_rowconfigure(6, weight = 0)
		# displayMessage.bind('<Control-a>', PCExtractorApp.select_all(self, displayMessage))


		# print (self.uploadMeasurementTypes())			

	# Builds the final measurements query that will be copied and pasted into OSCAR Reports to pull data.
	# 	Input: 
	#		- measurements: a string array of measurements in the form of {"HT, WT, ..."} that will be included in the query. I.e the list of measurement we are interested in.
	#       - fromDate: the date from which we are pulling data
	#       - toDate: the date to we are pulling data.
	#	Output: Query String 
	def buildMeasurementsQuery(self, measurements, display, reVar):
		display.delete('1.0', "end") # clear the display if there is something alredy there
		xmlHeader = "<report title=\"PC Extractor Built Query - Measurements\" description=\"Custom Query Developed by the PC Extractor\" active=\"1\"><query> "
		query_select = "SELECT d.demographic_no AS \'Pt. ID\', CONCAT(d.last_name, \", \", d.first_name) AS \'Patient (Last, First)\', d.sex AS \'Sex\', CONCAT(d.year_of_birth, \"-\", d.month_of_birth, \"-\", d.date_of_birth) AS \'DOB (y-m-d)\', DATEDIFF(CURDATE(), CONCAT(d.year_of_birth, \"-\", d.month_of_birth, \"-\", d.date_of_birth))/365 AS \'Age\', a.appointment_date AS \'Appt. Day (y-m-d)\', CONCAT(pa.last_name, \", \", pa.first_name, \" (\", pa.specialty, \")\" ) AS \'Appt. Pharmacist\', a.`type`AS \'Appointment Type\', "
		query_select_res="SELECT d.demographic_no AS \'Pt. ID\', d.sex AS \'Sex\', DATEDIFF(CURDATE(), CONCAT(d.year_of_birth, \"-\", d.month_of_birth, \"-\", d.date_of_birth))/365 AS \'Age\', a.appointment_date AS \'Appt. Day (y-m-d)\', CONCAT(pa.last_name, \", \", pa.first_name, \" (\", pa.specialty, \")\" ) AS \'Appt. Pharmacist\', a.`type`AS \'Appointment Type\'," 
		#query_ifNull = "IFNULL("+queryCode+".dataField, \'\') AS \'"+ queryCode+"\'," #would need "," of more than one
		query_from = "FROM demographic d JOIN appointment a ON (a.demographic_no = d.demographic_no AND DATE(a.appointment_date) BETWEEN \'{apt_date_from}\' AND \'{apt_date_to}\')"
		#query_leftJoin = "LEFT JOIN measurements " + queryCode + " ON (" + queryCode +".demographicNo = d.demographic_no AND " + queryCode + ".type LIKE \"%" + queryCode +"%\" AND date_format(a.appointment_date, \'%Y-%m-%d\') = date_format(" + queryCode + ".dateObserved, \'%Y-%m-%d\')) "
		query_provider_join = "JOIN provider pa ON (pa.provider_no = a.provider_no) "
		query_where = "WHERE a.provider_no LIKE \'{provider}\' AND ( d.last_name NOT LIKE \'%TEST%\' AND d.last_name NOT LIKE \'%BOOP%\' ) AND d.patient_status LIKE \"%ac%\" AND ( a.status NOT LIKE \"%c%\" AND a.status NOT LIKE \"%n%\" AND a.status NOT LIKE \"%cs%\" AND a.status NOT LIKE \"%ns%\" ) AND a.`type` LIKE \'{aType}\' GROUP BY  d.demographic_no, a.appointment_date HAVING COUNT(a.appointment_date) > -1 ORDER BY a.appointment_date; </query>"
		params = "<param id=\"apt_date_from\" type=\"date\" description=\"From (Appt Date):\" /> <param id=\"apt_date_to\" type=\"date\" description=\"To (Appt Date):\" /> <param id=\"provider\" type=\"list\" description=\"Pharmacist (Choose Team A):\"> <choice id=\"%\">- All -</choice> <param-query> SELECT pr.provider_no, CONCAT(pr.last_name, \', \', pr.first_name, \' (\', pr.specialty, \')\') FROM provider pr WHERE pr.provider_no IS NOT NULL AND pr.provider_no != \'\' AND pr.status = 1 ORDER BY pr.last_name ASC; </param-query> </param> <param id=\"aType\" type=\"list\" description=\"Appointment Type (Select BOps or THF):\"> <choice id=\"%\">- All -</choice> <param-query> SELECT name, name FROM appointmentType  ORDER BY name ASC; </param-query> </param> </report>"
		query_ifNull_built = ""
		query_leftJoin_built = ""

		for code in measurements:
			queryCode = code.split(' ')[0]
			query_ifNull_built += "IFNULL("+queryCode+".dataField, \'\') AS \'"+ queryCode+"\', "
			query_leftJoin_built += "LEFT JOIN measurements " + queryCode + " ON (" + queryCode +".demographicNo = d.demographic_no AND " + queryCode + ".type LIKE \"%" + queryCode +"%\" AND date_format(a.appointment_date, \'%Y-%m-%d\') = date_format(" + queryCode + ".dateObserved, \'%Y-%m-%d\')) "

		if reVar.get() == 0:
			display.insert("end", xmlHeader+ query_select + query_ifNull_built[:-2]+ ' ' + query_from + query_leftJoin_built + query_provider_join + query_where + params)
		else:
			display.insert("end", xmlHeader+ query_select_res + query_ifNull_built[:-2]+ ' ' + query_from + query_leftJoin_built + query_provider_join + query_where + params)


	# UI element to update display on user selection.
	# Input:
	# 	- types: an array of measurement types that have been selected
	# 	- listbox: the listbox object to update
	# Output: nothing. Screen GUI updated.
	def updateListbox(self, types, listbox):
		print(types)
		print (listbox.get("active", "end"))
		#for item in types:
		if types in ["FILE ACCESS ERROR", "Please click the", "\'Upload Measurement", "Types\' button below"]:
			return
		if types not in listbox.get("0","end"):  #********** was previously active to end?
			listbox.insert("end", types)

	# Attempts to open the measurements file and upload measurements data to the user interface.
	# Input:
	# 	- listbox: the listbox UI element to which we are uploading the data
	# 	- listbox: the listbox object to update
	# Output: nothing. Screen GUI updated.		
	def parseMeasurementsFile(self, listbox, searchTerm):
		try:
			mfile=open(MEASUREMENTS_FILE_NAME, "r")
			types = mfile.readlines()
			types = [x[:-1] for x in types]
			mfile.close()
		except:
			types = ["FILE ACCESS ERROR", "Please click the", "\'Upload Measurement" , "Types\' button below"]
			# PCExtractorApp.displayMessage(self,"File Access Error", "Check"+ MEASUREMENTS_FILE_NAME+" or upload a new measurements list")

		# types = self.parseMeasurementsFile()	
		
		listbox.delete(0, 'end')

		for items in types:
			searchTerm = searchTerm.lower()
			i = items.lower()
			if searchTerm in i:
				listbox.insert("end", items)

	# Function involved in creating the user instructions for the user to upload the measurement types. Will create a button that will allow the user to upload the measurement types as well as execute the upload to the application.
	# Input:
	#   - display: pointer to the display object to be updated. In this case, this is the main display of the program
	#   - listbox: the list box that should be updated once the data is loaded.	
	# Output: nothing. GUI will be updated with new data from user input.	
	def loadMeasurementTypes(self, display, listbox):
		display.delete('1.0', "end")
		# query = "<report title=\"PC Extractor Built Query - Measurements\" description=\"Custom Query Developed by the PC Extractor\" active=\"1\"> <query> SELECT `type` AS \'Type\' FROM measurementType ORDER BY `type` ASC; </query> </report>"
		query = "<report title=\"PC Extractor Built Query - Measurements\" description=\"Custom Query Developed by the PC Extractor\" active=\"1\"> <query> SELECT `type` AS \'Type\', typeDescription AS \'Description\' FROM measurementType ORDER BY `type` ASC; </query> </report>"
		# display.insert("end", "Instructions\n 1. Copy query below and paste it into OSCAR report\n 2. Run report and copy data from below \'Type\' and \'Description\' \n 3. Press \'Clear\' to delete the content of this box\n 4. Paste data\n 5. Click \'Upload\'\n\n" + query)
		display.insert("end", "Read all instructions before proceeding. To redisplay the instructions click the \"Upload Measurements Types\" button\nInstructions\n 1. Go to OSCAR Report Tab (from the home page/calendar display click \"Report\")\n 2. Scroll Down to number 23 and click \"Report by Template\" \n 3. Scroll Down and click report 44\n 4. Click \"Show/Hide Options\" at the bottom (under Generate Query)\n 5. Click \"Edit Template\"\n 6. Delete the current query in the OSCAR query template\n 7. Copy the query from the extractor application below (scroll down in this box)\n 8. Paste the copied query into the OSCAR query template\n 9. Click \"Save\"\n 10. Click \"Done\"\n 11. Run query in OSCAR by clicking \"Run Query\"\n 12. Copy data from the table that is displayed (copy everything except the headings \"Type\" and \"Description\") using\n 13. Press “Clear” on the data extractor application (button below right)\n 14. Paste data into the extractor application using\n 15. Click \"Upload\" (note this button only appears when the \"Upload Measurement Types button\" is clicked and disappears when \"Upload\" is clicked)\n 16. Once the above steps are complete, you should no longer see an error and the extractor has been updated with OSCAR Measurement Types\n 17. You may now proceed to create a query by selecting types and clicking \"Generate\"\n\n" +query)
		uploadButton =tk.Button(self, text="Upload", font=SMALL_FONT, 
			command=lambda: self.createMeasurementsFile(display.get("1.0","end"),listbox, uploadButton, display))
		uploadButton.grid(row=6, column=1) # uploadButton.grid_forget

	
	# Responsible for creating application data file that can be re-read by the application upon start up for persistent memory. This could later be developed to interact with a SQL type of database. For not this will suffice.
	# Input:
	#   - types: the measurement types added by the user (that were extracted from OSCAR EMR)
	#   - listbox: The listbox to which the new data needs to be uploaded to
	#   - button: a pointer to the button object that triggered this function. This is to remove the "Upload" button from the GUI after the uploading complete
	# Output: nothing. New measurements types data file created and can be reused by the application for memory upon start up.
	def createMeasurementsFile(self, types, listbox, button, display):
		try:
			os.remove(MEASUREMENTS_FILE_NAME)
			print ("Removing old measurements data")
			mfile=open(MEASUREMENTS_FILE_NAME, "w+")
			print ("Creating new measurements.in")
		except:
			mfile=open(MEASUREMENTS_FILE_NAME, "w+")
			print ("Creating new measurements.in")
			
		# mfile.seek(0)  -> might work with this method because didnt realize bug before. If we use this then we do not need to import OS (less dependencies)
		# mfile.truncate()
		mfile.write(types)
		mfile.close()
		self.parseMeasurementsFile(listbox,'')
		button.grid_forget()
		display.delete('1.0', "end")

# Defines the page that will create queries pertaining to the Healthcare Team Module
class HealthCareTeamModule(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label=tk.Label(self, text="Health Care Team Module Query Builder", font=LARGE_FONT)
		label.grid(row=0,column=0, columnspan=3)	

		returnButton = tk.Button(self, text="Back", font=SMALL_FONT,
			command=lambda: controller.show_frame(StartPage, STANDARD_SIZE))
		returnButton.grid(row=5, column=0, sticky="W")	


# General page to retrieve data from OSCAR EMR
class DemographicsModule(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label=tk.Label(self, text="Demographics Dynamic Query Builder", font=LARGE_FONT)

		global DATABASESCHEMA

		tLable = tk.Label(self,text="Table", font=SMALL_FONT)
		mTypesLabel = tk.Label(self,text="Fields", font=SMALL_FONT)
		sTypesLabel = tk.Label(self,text="Selected Fields", font=SMALL_FONT)

		options_listbox = tk.Listbox(self, selectmode="SINGLE", font=SMALL_FONT)
		selection_listbox = tk.Listbox(self, selectmode="SINGLE", font=SMALL_FONT)
		table_listbox = tk.Listbox(self, selectmode="SINGLE", font=SMALL_FONT)
		table_listbox.bind("<<ListboxSelect>>", lambda x: self.displayTableContents(table_listbox.get("active"), options_listbox))


		displayMessage = tk.Text(self, font=SMALL_FONT)

		# reVar = tk.IntVar()
		# researchButton = tk.Checkbutton(self, text="Trim for Research", font=SMALL_FONT
		# 	, variable=reVar, anchor="w")
		# researchButton.var= reVar

		toggleVar=tk.StringVar()
		toggleVar.set("Demographics Only")
		toggleButton = tk.Button(self, textvariable=toggleVar, font=SMALL_FONT, 
			command=lambda: self.toggleTableTypes(toggleVar, table_listbox))

		#Button Frames
		buttonFrame = tk.Frame(self)
		addButton = tk.Button(buttonFrame, text="Add", font=SMALL_FONT,
			command=lambda: MeasurementsModule.updateListbox(DemographicsModule,options_listbox.get("active"), selection_listbox))
		addButton.pack(side="top", fill="both")

		removeButton = tk.Button(buttonFrame, text="Remove", font=SMALL_FONT,
			command=lambda: selection_listbox.delete(selection_listbox.curselection(),selection_listbox.curselection()))
			# command=lambda: selection_listbox.delete(selection_listbox.curselection()))
		removeButton.pack(fill="both")	
		

		addAllButton = tk.Button(buttonFrame, text="Add All", font=SMALL_FONT,
			command= lambda: self.addAll(options_listbox.get(0,'end'), selection_listbox, selection_listbox.get(0,'end')))
		addAllButton.pack(fill="both")


		removeAllButton = tk.Button(buttonFrame, text="Remove All", font=SMALL_FONT,
			command=lambda: selection_listbox.delete(0,'end'))
		removeAllButton.pack(fill="both")


		generateButton = tk.Button(self, text="Generate", font=SMALL_FONT,
			# command= lambda: self.runQuery(selection_listbox, fromDate, toDate, displayMessage))
			command= lambda: self.buildQuery(selection_listbox.get("0","end"), displayMessage, appointmentVar, numberLimit))	
		

		returnButton = tk.Button(self, text="Back", font=SMALL_FONT,
			command=lambda: controller.show_frame(StartPage, STANDARD_SIZE))

		clearButton = tk.Button(self, text="Clear", font=SMALL_FONT,
			command=lambda: displayMessage.delete('1.0', "end")) 

		uploadButton = tk.Button(self, text="Upload Table Schema", font=SMALL_FONT, 
			command= lambda: self.loadSchema(displayMessage, options_listbox, table_listbox))


		# reVar = tk.IntVar()u
		# researchButton = tk.Checkbutton(self, text="Trim for Research", font=SMALL_FONT
		# 	, variable=reVar, anchor="w")
		# researchButton.var= reVar

		appointmentVar = tk.IntVar()
		appointmentVar.set(1) #by default the appointment limit will be on
		appointmentLimit = tk.Checkbutton(self, text="Limit by Appointment Date", font=SMALL_FONT,
			variable=appointmentVar)

		limitLabel = tk.Label(self, text="Limit by Number:", font=SMALL_FONT)
		# numLimitVar = tk.StringVar()
		numberLimit = tk.Entry(self,font=SMALL_FONT)
		numberLimit.insert("end",1000)

		#### Search Box ####
		searchFrame = tk.Frame(self) #if button may need the frame, if no button then dont need the frame.
		searchVar = tk.StringVar()
		searchBox = tk.Entry(searchFrame, textvariable=searchVar,font=SMALL_FONT)
		searchBox.pack()
		searchVar.set("Type here to search")
		searchVar.trace("w", lambda x, y, z: self.searchSchema(searchVar.get(), table_listbox, toggleVar))
		######################

		helpButton = tk.Button(self, text="Help", font=SMALL_FONT, 
			command= lambda: PCExtractorApp.popupBox("Help", "General Overview\n\nPatient data is linked in OSCAR EMR through the demographic number. This module uses this assumption and links patient data through this demographic number. To use, select a table and double click to expand fields (fields box will be populated with information on the contents of the OSCAR table selected). Select the fields of interest and click \"Add\" to add to the list of selected fields. It is recommended to limit by appointment (by selecting the appropriate box) and limit by number or records retrieved. Please note: OSCAR EMR can crash if too much data is retrieved at once. Click \"Generate\" and you have a query that you can copy into the OSCAR EMR Reports by Template module.\n\n\nProposed Use\n\n1. Click the \"Demographics Only\" button (the button will switch from \"Demographics Only\" to \"Full Schema\") to display compatible tables (Full Schema for advanced users)\n\n2.Select the \"demographic\" table and choose the fields of interest (ex. first_name, last_name, etc.)\n\n3. Choose a table you want to merge on (ex. allergies) and select fields of interest\n\n4. Select another table to merge on and repeat step 2 (optional). Note: the more tables you merge on the more data you will generate.\n\n5. Select \"Limit by Appointment Date\" and put a number in the \"Limit by Number\" box (suggested 1000)\n\n6. Click \"Generate\"\n\n\nBuilt-in Functionality\n\nCurrently the generator will merge on the following tables automatically if a field from the table is selected (in development). This will allow you to filter based on the respective dictionaries in OSCAR EMR Report by Template.\n  -\"appointment\"\n  -\"DrugTherapyProblem\"\n  -\"dxresearch\"\n  -\"Internal Provider\"","525x545", 500, "left"))

		# +---------|---------|---------|---------+
		label.grid(row=0,column=0, columnspan=4)
		tLable.grid(row=1, column=0)
		mTypesLabel.grid(row=1,column=1)
		sTypesLabel.grid(row=1,column=3)
		options_listbox.grid(row=2, column=1)
		selection_listbox.grid(row=2, column=3)
		table_listbox.grid(row=2, column=0)
		buttonFrame.grid(row=2, column=2)

		generateButton.grid(row=4, column=1, columnspan=2)
		searchFrame.grid(row=4, column=0)
		# researchButton.grid(row=3, column=0)
		helpButton.grid(row=4, column=3)
		toggleButton.grid(row=3, column=0, sticky="NSEW")
		appointmentLimit.grid(row=3, column=1)
		limitLabel.grid(row=3, column=2)
		numberLimit.grid(row=3, column=3)
		
		displayMessage.grid(row=5, column=0, columnspan=4)
		returnButton.grid(row=6, column=0, sticky="W")
		clearButton.grid(row=6, column=3, sticky="E")
		uploadButton.grid(row=6, column=1, columnspan=2)


		DATABASESCHEMA = self.importOSCARSchemaData()

		self.loadDisplay(DATABASESCHEMA.keys(), table_listbox)

	# Adds all table fields, does not allow for duplicates
	# Input:
	# Output: Updates the GUI with selected table columns 
	def addAll(self, items, listbox, comparelist):
		toLoad = list()
		for item in items:
			if item not in comparelist:
				toLoad.append(item)	
		self.loadDisplay(toLoad, listbox)			
	
	# Builds the SQL query to be pasted into OSCAR EMR Reports Module
	# Input:
	#   - fields: a list of fields selected by the user to be incorporated into the query
	#   - display: the display GUI element that the query will be displayed in
	# Output: nothing. The query is created and displayed in the display message box for the user to use.
	def buildQuery(self, fields, display, appointmentVar, numberLimit):
		global DATABASESCHEMA
		display.delete('1.0', "end")
		query_string = ""
		SELECT = "SELECT "
		FROM = "FROM "
		WHERE = "WHERE "
		limit_by_appointment = ""
		parameters = ""
		parameter_table = list()

		# 1. Determine which table the field data is coming from
		tables = list() # list of tables that the fields have been selected from
		for field in fields:
			if field.split('.')[0] not in tables:
				tables.append(field.split('.')[0])	

		# 2. Build the SELECT portion of the Query (the data of interest to the user)
		for field in fields:
			SELECT = SELECT + field.split('.')[0][:-3] + '.' + field.split('.')[1] + ', '	

		# 3. Build FROM with Inner Joins
		index = tables[0]
		for table in tables:
			if table == index:
				FROM = FROM + index + ' ' + index[:-3] + ' '
			else:
				FROM = FROM + "INNER JOIN " + table + " " + table[:-3] + " ON ("+ index[:-3] + '.' +self.determineDemographic(index)+ " = " + table[:-3] + '.' + self.determineDemographic(table) + ") "

		# 4. Build in parameter searches based on dictionary tables included
		if "appointment" in tables:
			parameters = parameters + "<param id=\"apt_type\" type=\"list\" description=\"Appointment Type\"> <param-query> (SELECT DISTINCT a.type AS \'type_id\', IF(a.type=\' \',\'-All blanks-\',a.type) AS \'type_list\' FROM appointment a) UNION (SELECT \'%\', \'-All types-\') ORDER BY \'type_list\' ASC; </param-query> </param> "
			SELECT = SELECT + "appointm.type, "
			# FROM = FROM + "INNER JOIN appointmentType appointmentT ON (" + "appointment"[:-3]+ ".type" + " = appointmentT.id) "
			WHERE = WHERE + "appointment"[:-3]+".type LIKE \'{apt_type}\' AND "

		# if "allergies" in tables: systems key, not in Oscar dictionary table
		# Build in the DTP module queries if DrugTherapyProblems Table Selected
		# drugTherapyProblemComment, lu_drugTherapyProblemIssue, lu_drugTherapyProblemPharmacistAction, lu_drugTherapyProblemPriority, lu_drugTherapyProblemProbability, lu_drugTherapyProblemSeverity, lu_drugTherapyProblemStatus
		if "DrugTherapyProblem" in tables:
			SELECT = SELECT + "lu_drugTherapyProblemIs.name AS \'DTP\', drugTherapyProblemComm.comment AS \'Comment\', lu_drugTherapyProblemProbabil.name AS \'Probability\', lu_drugTherapyProblemPrior.name AS \'Priority Level\', lu_drugTherapyProblemSever.name AS \'Severity\', lu_drugTherapyProblemPharmacistAct.name AS \'Pharm Action\', lu_drugTherapyProblemSta.name AS \'DTP Status\', "
			FROM = FROM + " INNER JOIN lu_drugTherapyProblemIssue lu_drugTherapyProblemIs ON (DrugTherapyProb.issue_id = lu_drugTherapyProblemIs.id) INNER JOIN drugTherapyProblemComment drugTherapyProblemComm ON (DrugTherapyProb.comment_id = drugTherapyProblemComm.id) INNER JOIN lu_drugTherapyProblemProbability lu_drugTherapyProblemProbabil ON (DrugTherapyProb.probability_id = lu_drugTherapyProblemProbabil.id) INNER JOIN lu_drugTherapyProblemPriority lu_drugTherapyProblemPrior ON (DrugTherapyProb.priority_id = lu_drugTherapyProblemPrior.id) INNER JOIN lu_drugTherapyProblemSeverity lu_drugTherapyProblemSever ON (DrugTherapyProb.probability_id = lu_drugTherapyProblemSever.id) INNER JOIN lu_drugTherapyProblemPharmacistAction lu_drugTherapyProblemPharmacistAct ON (DrugTherapyProb.pharmacist_action_id = lu_drugTherapyProblemPharmacistAct.id) INNER JOIN lu_drugTherapyProblemStatus lu_drugTherapyProblemSta ON (DrugTherapyProb.status_id = lu_drugTherapyProblemSta.id) " 
			# FROM = "FROM DrugTherapyProblem " + "DrugTherapyProblem"[:-3] +", " + FROM[4:] + "INNER JOIN lu_drugTherapyProblemIssue lu_drugTherapyProblemIs ON (DrugTherapyProb.issue_id = lu_drugTherapyProblemIs.id) INNER JOIN drugTherapyProblemComment drugTherapyProblemComm ON (DrugTherapyProb.comment_id = drugTherapyProblemComm.id) INNER JOIN lu_drugTherapyProblemProbability lu_drugTherapyProblemProbabil ON (DrugTherapyProb.probability_id = lu_drugTherapyProblemProbabil.id) INNER JOIN lu_drugTherapyProblemPriority lu_drugTherapyProblemPrior ON (DrugTherapyProb.priority_id = lu_drugTherapyProblemPrior.id) INNER JOIN lu_drugTherapyProblemSeverity lu_drugTherapyProblemSever ON (DrugTherapyProb.probability_id = lu_drugTherapyProblemSever.id) INNER JOIN lu_drugTherapyProblemPharmacistAction lu_drugTherapyProblemPharmacistAct ON (DrugTherapyProb.pharmacist_action_id = lu_drugTherapyProblemPharmacistAct.id) INNER JOIN lu_drugTherapyProblemStatus lu_drugTherapyProblemSta ON (DrugTherapyProb.status_id = lu_drugTherapyProblemSta.id) " 
			# FROM = FROM + ", DrugTherapyProblem " + "DrugTherapyProblem"[:-3] + "INNER JOIN lu_drugTherapyProblemIssue lu_drugTherapyProblemIs ON (DrugTherapyProb.issue_id = lu_drugTherapyProblemIs.id) INNER JOIN drugTherapyProblemComment drugTherapyProblemComm ON (DrugTherapyProb.comment_id = drugTherapyProblemComm.id) INNER JOIN lu_drugTherapyProblemProbability lu_drugTherapyProblemProbabil ON (DrugTherapyProb.probability_id = lu_drugTherapyProblemProbabil) INNER JOIN lu_drugTherapyProblemPriority lu_drugTherapyProblemPrior ON (DrugTherapyProb.priority_id = lu_drugTherapyProblemPrior.id) INNER JOIN lu_drugTherapyProblemSeverity lu_drugTherapyProblemSever ON (DrugTherapyProb.probability_id = lu_drugTherapyProblemSever.id) INNER JOIN lu_drugTherapyProblemPharmacistAction lu_drugTherapyProblemPharmacistAct ON (DrugTherapyProb.pharmacist_action_id = lu_drugTherapyProblemPharmacistAct.id) INNER JOIN lu_drugTherapyProblemStatus lu_drugTherapyProblemSta ON (DrugTherapyProb.status_id = lu_drugTherapyProblemSta.id) " 
			WHERE = WHERE + "lu_drugTherapyProblemIs.id LIKE \'{dtpType}\' AND lu_drugTherapyProblemProbabil.id LIKE \'{dtpProbability}\' AND lu_drugTherapyProblemPrior.id LIKE \'{dtpPriorityLevel}\' AND lu_drugTherapyProblemSever.id LIKE \'{dtpSeverity}\' AND lu_drugTherapyProblemPharmacistAct.id LIKE \'{pharmAction}\' AND lu_drugTherapyProblemSta.id LIKE \'{dtpStatus}\' AND "
			parameters = parameters + "<param id=\"dtpType\" type=\"list\" description=\"DTP Type:\"> <param-query> (SELECT \'%\', \'-All Types-\') UNION (SELECT id, name FROM lu_drugTherapyProblemIssue); </param-query> </param> <param id=\"dtpProbability\" type=\"list\" description=\"Probability:\"> <param-query> (SELECT \'%\', \'-All Types-\') UNION (SELECT id, name FROM lu_drugTherapyProblemProbability); </param-query> </param> <param id=\"dtpPriorityLevel\" type=\"list\" description=\"Priority:\"> <param-query> (SELECT \'%\', \'-All Types-\') UNION (SELECT id, name FROM lu_drugTherapyProblemPriority); </param-query> </param> <param id=\"dtpSeverity\" type=\"list\" description=\"Severity:\"> <param-query> (SELECT \'%\', \'-All Types-\') UNION (SELECT id, name FROM lu_drugTherapyProblemSeverity); </param-query> </param> <param id=\"pharmAction\" type=\"list\" description=\"Pharm Action:\"> <param-query> (SELECT \'%\', \'-All Types-\') UNION (SELECT id, name FROM lu_drugTherapyProblemPharmacistAction); </param-query> </param> <param id=\"dtpStatus\" type=\"list\" description=\"Status:\"> <param-query> (SELECT '%', ' -All Types-') UNION (SELECT id, name FROM lu_drugTherapyProblemStatus); </param-query> </param> "


		if "dxresearch" in tables:
			SELECT = SELECT + "i.description, "
			FROM = FROM + "INNER JOIN icd9 i ON (i.icd9 = dxresea.dxresearch_code) "
			WHERE = WHERE + "dxresearch"[:-3] + ".dxresearch_code LIKE \'{icd9}\' AND "
			parameters = parameters + "<param id=\"icd9\" type=\"list\" description=\"ICD9 code:\"> <param-query> (SELECT '%', '-All Types-') UNION (SELECT icd9, description FROM icd9); </param-query> </param> "

		# Include internal provider if provider_no or providerNo is included in the list of fields
		providerAddedFlag = "0" # this is to prevent more than one provider number from being added if two tables have the provider number field in it
		for field in fields:
			if ("provider_no" in DATABASESCHEMA[field.split(".")[0]].split(",") or "providerNo" in DATABASESCHEMA[field.split(".")[0]].split(",")) and field.split(".")[0] != "demographic" and field.split(".")[0] != "allergies" and field.split(".")[0] != "dxresearch":
				if providerAddedFlag != "*":
					providerAddedFlag = "*"
					SELECT = SELECT + "CONCAT(provi.last_name, \", \", provi.first_name) AS \"Provider\", "
					# FROM = FROM + "INNER JOIN " + field.split(".")[0] + " " +field.split(".")[0][:-3] + " ON (" + field.split(".")[0][:-3] +"."+ self.determineProvider(field) + "= provi.provider_no) "
					FROM = FROM + "INNER JOIN provider provi ON (provi.provider_no = " + field.split(".")[0][:-3] + "." + self.determineProvider(field)+ ") "
					WHERE = WHERE + " " + field.split(".")[0][:-3] + "." + self.determineProvider(field) +" LIKE \'{provider}\' AND "
					parameters = parameters + "<param id=\"provider\" type=\"list\" description=\"Clinician:\"> <param-query> (SELECT '%', '-All clinicians-') UNION (SELECT p.provider_no, CONCAT(p.last_name, \", \", p.first_name) AS \"Provider Name\" FROM provider p WHERE p.status = 1 AND p.provider_type != \'admin\') ORDER BY \"Provider Name\" ASC; </param-query> </param> "


		# 5. Put it all together
		if appointmentVar.get()==0:
			display.insert("end", "<report title=\"PC Extractor Built Query - Dynamic Builder\" description=\"Custom Query Developed by the PC Extractor\" active=\"1\"> <query> " + SELECT[:-2] + ' ' + FROM[:-1] + self.determineWhere(WHERE)[:-4]+self.addNumLimit(numberLimit)+  ';' + "</query> " +parameters+ " </report>")
		else:
			if self.determineWhere(WHERE) == " ":
				display.insert("end", "<report title=\"PC Extractor Built Query - Dynamic Builder\" description=\"Custom Query Developed by the PC Extractor\" active=\"1\"> <query> " + self.determineAppointment(SELECT) + ' ' + self.determineFrom(FROM, index) +' WHERE appointm.appointment_date BETWEEN \'{apt_date_from}\' AND \'{apt_date_to}\''+ self.addNumLimit(numberLimit)+'; </query> <param id=\"apt_date_from\" type=\"date\" description=\"Appointments from (YYYY-MM-DD):\"> </param> <param id=\"apt_date_to\" type=\"date\" description=\"Appointments to (YYYY-MM-DD):\"> </param> ' +parameters+ ' </report>')
			else:
				display.insert("end", "<report title=\"PC Extractor Built Query - Dynamic Builder\" description=\"Custom Query Developed by the PC Extractor\" active=\"1\"> <query> " + self.determineAppointment(SELECT) + ' ' + self.determineFrom(FROM, index) +' '+ WHERE[:-4] + ' AND appointm.appointment_date BETWEEN \'{apt_date_from}\' AND \'{apt_date_to}\''+ self.addNumLimit(numberLimit)+'; </query> <param id=\"apt_date_from\" type=\"date\" description=\"Appointments from (YYYY-MM-DD):\"> </param> <param id=\"apt_date_to\" type=\"date\" description=\"Appointments to (YYYY-MM-DD):\"> </param> '+parameters+' </report>')

			
	##################### Helper Functions for Query Builder #####################

	def determineDemographic(self, table):
		global DATABASESCHEMA
		if "demographic_no" in DATABASESCHEMA[table].split(','):
			return "demographic_no"
		else:
			return "demographicNo"	

	def determineAppointment(self, string):
		if "appointment" in string:
			return string[:-2]
		else:
			return string + "appointm.appointment_date"

	def determineFrom(self, string, index):
		if "appointm" in string:
			return string[:-1]
		else:
			return string + "INNER JOIN appointment appointm ON (" + index[:-3] + '.' + self.determineDemographic(index) + "=" + "appointm." + self.determineDemographic("appointment") + ") " 

	def addNumLimit(self, numberLimit):
		try:
			int(numberLimit.get())
			return " LIMIT " + numberLimit.get()
		except:
			return ""
	def determineWhere(self, where):
		if where == "WHERE ":
			return " "
		else:
			return ' '+ where
	def determineProvider(self, table):
		global DATABASESCHEMA
		check =  DATABASESCHEMA[table.split(".")[0]].split(",")

		if "provider_no" in check:
			return "provider_no"
		else:
			return "providerNo"	

	##############################################################################

	# Function responsible for loading the GUI listboxes with data
	# Input: 
	#   - items: a list of items to upload (could be table names or field names)
	#   - listbox: the respective listbox to load the data to (could be tables listbox or options listbox)
	# Output: nothing. GUI is updated with respective data.
	def loadDisplay(self, items, listbox):
		for i in items:
			listbox.insert("end", i)

	# Function that displays the tables fields from the DATABASE SCHEMA disctionary previously created.
	# Input:
	#   - table: the table name, whose contents need to be displayed
	#   - listbox: a pointer to the listbox that will show the data.
	# Output: nothing. Load display function is called to display data to the user.
	def displayTableContents(self, table, listbox):
		# demographics = {'demographics', 'demographic_no', 'title', 'last_name', 'first_name', 'address', 'city','province','postal','phone','phone2','email','myOscarUserName','year_of_birth','month_of_birth','date_of_birth','hin','ver','roster_status','roster_date','roster_termination_date','roster_termination_reason','patient_status','patient_status_date','date_joined','chart_no','official_lang','spoken_lang','provider_no','sex','end_date','eff_date','pcn_indicator','hc_type','hc_renew_date','family_doctor','alias','previousAddress','children','sourceOfIncome','citizenship','sin','country_of_origin','newsletter','anonymous','lastUpdateUser','lastUpdateDate'}
		listbox.delete(0,'end')
		global DATABASESCHEMA
		# if table == "demographics":
		# 	self.loadDisplay(demographics, listbox)
		# elif table == "test":
		# 	self.loadDisplay("hi", listbox)	
		# else:
		# 	self.loadDisplay("wo", listbox)
		# print(DATABASESCHEMA)
		self.loadDisplay((table +"."+ field for field in (DATABASESCHEMA[table].split(','))), listbox)

	# Import the OSCAR table structure from a CSV file created by the user
	# Input: nothing.
	# Output:
	#   - mydict: a pointer to a dictionary that is created from the CSV file uploaded by the user. The dictionary format is {"Table Name" :"Field1, Field2, Field3, ..."}. The data in the dictionary will eventually be split on "," to create a list of field elements	
	def importOSCARSchemaData(self):
		mydict = dict()	
		try:
			with open(TABLE_SCHEMA_NAME, mode='r') as infile:
				reader = csv.reader(infile)
				
			
				for row in reader:
					
					if row[0] in mydict:	
						mydict[row[0]] = mydict[row[0]] + ',' + row[1]
					else:
						mydict.update({row[0]: row[1]})
				
				# mfile = open(TABLE_SCHEMA_NAME, "w")	
				# mfile.write(str(mydict))
				# mfile.close()		
		except:
			mydict = {"Please upload your":"", "database schema by clicking" :"", " \"Upload Table Schema\"":"", "and following the instructions":""}		
		return mydict

		# mfile=open(MEASUREMENTS_FILE_NAME, "r")
		# 	types = mfile.readlines()
		# 	types = [x[:-1] for x in types]
		# 	mfile.close()			

	# The function that displays the instructions to the user on how to upload the database schema from OSCAR. This function will create the upload button that the user will use to upload the schema
	# Input:
	#	- displayMessage: the display box that the instructions will be displayed in. In this case it will be the same box that the query is displayed in after building.
	# 	- options_listbox: the listbox that displays the OSCAR table contents for each respective table
	#	- table_listbox: the listbox that  displays the tables in OSCAR
	# Output: nothing. The schema is loaded to the application and GUI
	def loadSchema(self, displayMessage, options_listbox, table_listbox):
		displayMessage.delete('1.0', "end")
		print ("hi you clicked the Upload Table Schema button")
		query = "<report title=\"PC Extractor Built Query - Dynamic Query Builder\" description=\"Custom Query Developed by the PC Extractor\" active=\"1\"> <query> " +"SELECT TABLE_NAME, COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA=\"oscar_ephi\";" + "</query> </report>"

		displayMessage.insert("end", "Instructions\n 1. Copy query below and paste it into OSCAR report\n 2. Run report and export as *.CSV file \n 3. Click \'Upload\' and select the file you just created\n\n" + query)
		uploadButton =tk.Button(self, text="Upload", font=SMALL_FONT, 
			# command=lambda: self.createMeasurementsFile(display.get("1.0","end"),listbox, uploadButton))
			command= lambda:self.createSchemaFile(table_listbox, uploadButton, displayMessage))
		uploadButton.grid(row=7, column=1, columnspan=2) # uploadButton.grid_forget

	# The function responsible for persisting the OSCAR Schema uploaded by the user in memory (database) this could be another area that an SQL database could be handy. For now this will suffice.
	# Input:
	# 	- table_listbox: the listbox that displays the table data. This will be refreshed right after uploading of the schema
	#	- uploadButton: the upload button that the user clicks. This will be deleted after uploading complete
	#	- displayMessage: the display message box. This will be cleared after uploading complete (will remove the upload instructions)
	# Output: nothing. oscar schema CSV file is created that the applciation can use to re-read upon start-up. 
	def createSchemaFile(self, table_listbox, uploadButton, displayMessage):
		userFile = tk.filedialog.askopenfilename(initialdir="/", title="Select File")
		infile = open(TABLE_SCHEMA_NAME, mode="w+")
		selectFile = open(userFile, mode="r")

		global DATABASESCHEMA
		read = csv.reader(selectFile)
		writer = csv.writer(infile)
		for row in read:
			writer.writerow(row)

		DATABASESCHEMA = self.importOSCARSchemaData()
		table_listbox.delete(0,'end')

		self.loadDisplay(DATABASESCHEMA.keys(), table_listbox)
		displayMessage.delete('1.0', "end")
		uploadButton.grid_forget()
		# print(DATABASESCHEMA)
		# self.loadDisplay((table +"."+ field for field in (DATABASESCHEMA[table].split(','))), options_listbox)	

	# The function responsible for filtering out tables with or without patient data (using the demographic_no as the filter)
	# Input:
	# 	- toggleVar: the stringv variable (text on the button) that determines what data from the database schema to show. If it is set to Demographics Only then only the tables with demographic_no included will be displayed, else the full table set will be displayed.
	#	- table_listbox: the listbox object to update. In this case we are updating the table listbox field.
	# Output: mothing. The GUI is updated to include information to the user
	def toggleTableTypes(self, toggleVar, table_listbox):
		global DATABASESCHEMA
		demographicDisplay = list()
		table_listbox.delete(0,'end')

		if toggleVar.get() == "Demographics Only":
			# The case where the user only wants to see tables that have the demographic number (i.e. tables that have patient data) -> need
			for table in DATABASESCHEMA.keys():
				if "demographic_no" in DATABASESCHEMA[table].split(','):
					demographicDisplay.append(table)
				elif "demographicNo" in DATABASESCHEMA[table].split(','):
					demographicDisplay.append(table)	
			self.loadDisplay(demographicDisplay, table_listbox)
			toggleVar.set("Full Schema")
		else:
			# The case where the user wants to see all the tables in OSCAR
			self.loadDisplay(DATABASESCHEMA.keys(), table_listbox)
			toggleVar.set("Demographics Only")

	# Function reponsible for implementing searching in the Demographics Module
	# Input
	# Output:
	def searchSchema(self, value, table_listbox, toggleVar):
		global DATABASESCHEMA
		search_list = list()
		for data in DATABASESCHEMA.keys():
			value = value.lower()
			d = data.lower()
			if value in d:
				search_list.append(data)
		# print(search_list)
		table_listbox.delete(0,'end')	
		# depending on if the toggle for demographics is set, only display the fields that have a demographic_no entry
		if toggleVar.get() == "Demographics Only":	
			self.loadDisplay(search_list, table_listbox)
		else:
			display_list = list()
			for table in search_list:
				if "demographic_no" in DATABASESCHEMA[table].split(','):
					display_list.append(table)
				elif "demographicNo" in DATABASESCHEMA[table].split(','):
					display_list.append(table)
			self.loadDisplay(display_list, table_listbox)					



app=PCExtractorApp()
app.mainloop()






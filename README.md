ARISS Moderator Script Generator Tool - READ ME File
====================================================
By: Ken McCaughey (N3FZX)  
On: 2024-11-30   
Ver 3.0.0   

<!-- In MarkDownd format. -->
<!-- Page breaks set for MarkText, US letter, with 10 top & bot.-->

Contents
--------
* Goals  
* Disclaimer  
* How It Works  
* Setup  
* Instructions and Work Flow  
* Notes About the Moderator Script Format  
* Dictionary of Script Document Variables


Goals
-----
This tool helps create an ARISS Moderator Script used for ISS school 
contacts.  

The goals of this tool are to:    
1. Have good consistent formatting that is easy to read and follow.  
2. Have all the checklists and important details included.  
   These are often not included in ARISS scripts, thus more ad-lib.  
3. Automate filling out the template to ensure accuracy.   
4. Automate the calculation of the event timeline. No manual time math!  
5. Produce an event timeline outline to support event planning.  
6. Allow for easy customization for contact needs.   
7. Speed up the script generation time.  
8. Provide predictability for mentors and moderators.  


Disclaimer
----------

This free software is provided as is.  


<div style="page-break-after: always;"></div>

How It Works
------------

Two files are needed to get started; a moderator script template 
in MS-Word `docx` format, and a completed text file form containing 
the values of needed variables. The Python script basically works 
like a mail merge to populate the template with the variable values 
(such as names, callsigns, etc.) set in the form file. It also takes 
care of the script timeline and does time math.  

Two files are generated; the moderator script in MS-Word `docx` format, 
and an event outline text file. The outline is useful in finalizing the 
event plan. It maps out the start time for each event block, planned 
durations, and time to ISS rise of the given event block. The file is 
easy to e-mail.  

The outline time calculations use the start of the conference time and 
the ISS rise time as anchors. The calculations assume typical time 
durations for ARISS related activities, such as audio checks, and ARISS
program. The school/group program start time and duration are calculated as 
a remainder of time left after accounting for the ARISS portions of the 
event. The baseline durations are specified in the form file and can be
changed if needed. 


Setup
-----

Before you begin, make sure things are set up correctly.

1. From GitHub download the files as a Zip file (click on the green 
   `<> Code` button and choose `Download ZIP`), and unzip.

2. In a folder called `ARISS_mod_script_gen-main` make sure the following 
   files are present:  

     - `ARISS_mod_script_form_blank.txt`
     - `ARISS_mod_script_temp_master_universal.docx`  
        There could be multiple master template files to choose from, 
        or they could be in a folder called `Templates`.  
     - `ARISS_mod_script_gen.py`
     - `README.md` and/or `README.pdf` (this file)
     - `HELPER.md` and/or `HELPER.pdf` (more help with Python setup)

2. This tool requires that Python 3.x is installed. 

     - See `https://www.python.org/downloads/`

3. The Python script requires the `docxtlp` library.

     - See https://pypi.org/project/docxtpl/   

<div style="page-break-after: always;"></div>

Instructions and Work Flow
--------------------------

1. MAKE a working script template file. 

   - COPY the desired master template file to be used 
     (i.e.  `ARISS_mod_script_temp_master.docx`) and name it as
     `ARISS_mod_script_temp.docx`. The working template needs to be 
     in the same folder as the Python script. The working template will 
     be edited.
   
   - There is a useful checklist on the last page of the template file.

2. MAKE a working input form file.

   - COPY the file `ARISS_mod_script_form_blank.txt` and name it
     `ARISS_mod_script_form.txt`. 
   
   - Running the Python script generates a new clean form file named 
     `ARISS_mod_script_form_blank.txt` to ensure there is a blank 
     form available.
       
3. COMPLETE the text file form, `ARISS_mod_script_form.txt`.   

   - This should be done by the mentor and/or moderator. There are 
     instructions within the file. Fill out as much as you can, or needed, 
     using a text file editor. 
   
   - To get a usable or first draft outline, only the `Script version`, 
    `Important Dates and Times`, and the `School/group name` need to be 
     completed in the form file.
       
4. EDIT the working template file `ARISS_mod_script_temp.docx`, 
   not the `master`.  

   In general the provided templates should be sufficient to cover the needs
   for a contact without much editing. Edits should be based on the plans 
   for the contact in terms on event flow and planned components, such as 
   videos and school/group program.
   
   - Paste in the questions from ARISS Op Uplink file.
   
   - OK to edit the script text and add/remove cues and notes as needed.  
     (See dictionary of variable below.)
     
   - OK to removed unused/optional blocks, such as the videos.

   - Remove the red colored text script notes.
   
   - Do NOT add more event blocks or change the event block names.
   
<div style="page-break-after: always;"></div>
       
5. RUN the Python script using an IDE or at the command line.  
   See the `HELPER` file for information on running Python.

   - The two input files must be in the same folder as the Python script.
     The files must have the following names:
        * Working template: `ARISS_mod_script_temp.docx`  
        * Working form: `ARISS_mod_script_form.txt` 

   - Command line: `python ARISS_mod_script_gen.py`  

   - You will see some messages scroll across the screen. There is limited 
     error checking. It will report success if there were no errors.

   - Two new files will be generated. If they already existed, they will 
     be overwritten. These are the final product files.
        * `ARISS_mod_script_<short_name>_V<ver#>.docx`  
        * `ARISS_mod_script_outline_<short_name>_V<ver#>.txt`  

6. OPEN the new moderator script file and review it for completeness and 
   correctness. If changes are needed, there are three ways to handle them.  

   - Just edit the moderator script directly and save. This is best
     path for minor edits if no more edits are anticipated and the Python
     script will not be re-run.  
       
   - Edit the working template file and rerun the Python script. A new 
     `docx` file will be created and overwrite the old one. A new outline 
     file will be generated, overwriting the old one.
   
  - If it is related to a variable, update the form text file and 
     rerun the Python script. A new `docx` file will be created and 
     overwrite the old one. A new outline file will be generated,
     overwriting the old one.  

7. UPDATE. If a version of the moderator script was distributed and needs
   to be updated, there are two ways to handle this.  

   - Just edit the generated script `docx` file directly. Be sure to 
     change the version number on script cover page. Save with a new 
     filename changing the version number. This is a good option for
     minor final edits.
   
   - If it is related to a variable or a change in the timeline, update 
     the form text file. Be sure to update the version number variable in 
     the form. Then rerun the Python script. A new `docx` file will be 
     created along with a new timeline report file.  

<div style="page-break-after: always;"></div>

Notes About the Moderator Script Template Format
------------------------------------------------

- The script template file must be in MS-Word `docx` format (not `doc`). 
  These files can be edited with MS-Word or Libre Writer. If using Libre 
  Writer, be sure to save in the `docx` format.   

- The MS-Word `docx` script template file needs to have variables inside 
  double braces, i.e. `{{variable}}`. The form text file maps all the 
  variables to their values. Only use variables that are listed below.

- The moderator script is divided into event blocks. Do NOT reorder.  
  
- Typical durations have been established for ARISS blocks. The durations 
  are specified in the form and can be changed if necessary. 

- The event blocks in the script are in a one column table. Each event 
  block is in a row. The table is set up so that page breaks are not 
  permitted within a row. This keeps each event block together on the same 
  page, helping with readability and flow during the event. It is very 
  helpful to turn on the "view table gridlines" feature to see the hidden 
  boarders. 

  
Dictionary of Script Document Variables
---------------------------------------

The form file is the vehicle to specify the variable values for the 
script. The form consists of a list of field names and variables pairs. 

	Field name: {{variable}}  =  field/variable pair
	
The variables take the form of double braces around a variable name (i.e. 
field name `ISS callsign to be used` variable is `{{ISS_callsign}}`). 
These names are fixed in the Python script and should not be changed.

Below is the list of field names and their corresponding variables that are
supported by the Python script. The variables can be placed anywhere, and
repeated, in the `docx` moderator script working template document. It is 
not necessary to use all of the available variables in a script. Note that 
most variables are specified in the form file, while others are only 
generated by the Python script. If additions are needed, the Python script 
would need to be updated. 

The default form file only has the minimum necessary field/variable pairs.
To use additional pairs, they will need to be added to the form file from 
the list below (not including the calculated timing variables).

<div style="page-break-after: always;"></div>

**The field/variable pairs marked with a * at the end are included by**
**default in the form file.**

#### Script version
Script version: `{{version}}`  *  

#### School/Group Information  
School/group name: `{{school_group_name}}`  *  
School/group location: `{{school_group_city_state}}`  *  
Coordinator/teacher at venue: `{{school_coordinator_name}}`  *   
School principal name: `{{principal_name}}`  *  
School teacher name: `{{teacher_name}}`  *  
Venue phone number: `{{school_coordinator_phone}}`  
Emergency back-up phone number: `{{school_coordinator_backup_phone}}` 

#### ISS Information  
Astronaut name: `{{astronaut_name}}`  *  
Astronaut callsign: `{{astronaut_callsign}}`  *  
ISS callsign to be used: `{{ISS_callsign}}`  *  

#### ARISS Moderator Information  
Moderator name: `{{moderator_name}}`  *  
Moderator callsign: `{{moderator_callsign}}`  *  
Moderator phone number: `{{moderator_phone}}`  
Moderator will be On-site/Remote for the contact: `{{moderator_location}}`  *  

#### ARISS Mentor Information  
Mentor name: `{{mentor_name}}`  *  
Mentor callsign: `{{mentor_callsign}}`  *  
Mentor phone number: `{{mentor_phone}}`  
Mentor will be On-site/Remote for the contact: `{{mentor_location}}`  *  

<div style="page-break-after: always;"></div>

#### ARISS Tele-bridge Information  
Tele-bridge station callsign: `{{telebridge_callsign}}`  *  
Tele-bridge station location: `{{telebridge_location}}`  *  
Tele-bridge station telephone number: `{{telebridge_phone}}`  
Tele-bridge operator name: `{{operator_name}}`  *  
Tele-bridge operator callsign: `{{operator_callsign}}`  *  
Tele-bridge operator phone number: `{{operator_phone}}`  
Tele-bridge support name(s) and callsign(s): `{{support_names_callsigns}}`  
Tele-bridge audio interface): `{{audio_interface}}`  *  
Tele-bridge video interface: `{{telebridge_video}}`  *  

#### ARISS Optional Videos
Contact from student perspective (Yes/No): `{{student_video}}`  *  
Contact from ISS perspective (Yes/No): `{{ISS_video}}`  *  

#### Live Streaming
Live steam planned (Yes/No): `{{livestream_plan}}`  *  
Live stream operator name: `{{livestream_name}}`  *  
Live stream operator callsign: `{{livestream_callsign}}`  *  
Live stream operator phone number: `{{livestream_phone}}`  

#### Fixed Timing
Contact date: `{{contact_date}}`  *  
Start of conference in UTC: `{{conf_utc}}`  *  
Start of conference school time: `{{conf_sch}}`  *  
ISS rise time in UTC: `{{AOS_UTC}}`  *  
ISS rise time in school time: `{{AOS_sch}}`  *  

<div style="page-break-after: always;"></div>

#### Calculated Timing

The variables listed below are calculated by the Python script. These are
predominately used to time tag the event blocks and generate the outline
report file. 

| Event                           | Start Time   | Duration  | ISS Rise  |
|:--------------------------------|:------------:|:---------:|:---------:|
| Conference start time           | `{{T01}}`    | `{{D01}}` | `{{R01}}` | 
| Ground station checklist        | `{{T02}}`    | `{{D02}}` | `{{R02}}` |
| Contact preparation checklist   | `{{T03}}`    | `{{D03}}` | `{{R03}}` |
| Practice run through w/students | `{{T04}}`    | `{{D04}}` | `{{R04}}` |
| School/group program/slack time | `{{T05}}`    | `{{D05}}` | `{{R05}}` |
| Start ARISS program             | `{{T06}}`    | `{{D06}}` | `{{R06}}` |
| ARISS introduction              | `{{T07}}`    | `{{D07}}` | `{{R07}}` |
| Video from student perspective  | `{{T08}}`    | `{{D08}}` | `{{R08}}` |
| Video from ISS perspective      | `{{T09}}`    | `{{D09}}` | `{{R09}}` |
| Introduce the ground station    | `{{T10}}`    | `{{D10}}` | `{{R10}}` |
| Handover to ground station      | `{{T11}}`    | `{{D11}}` | `{{R11}}` |
| ISS rise and AOS                | `{{T12}}`    | `{{D12}}` | `{{R12}}` |
| ISS Contact!                    | `{{AOS_sch}}`| -         |     -     |
| ISS set and  LOS                | `{{T13}}`    | -         |     -     |
| Closing & end of ARISS program  | `{{T13}}`    | `{{D13}}` |     -     |
| Contact preparation duration    | -            | `{{D14}}` |     -     |
| Shool/group program duration    | -            | `{{D15}}` |     -     | 
| ARISS program duration          | -            | `{{D16}}` |     -     |
| Total event duration            | -            | `{{D17}}` |     -     |

# === ARISS_mod_script_gen.py ================================================
"""
| NAME: ARISS Moderator Script Generator
| BY: Ken McCaughey (N3FZX)
| ON: 2024-11-30
| PROJECT: ARISS
| SCRIPT: ARISS_mod_script_gen.py
| VERSION: 3.0.0
| STATUS: Final version.
| SPDX-FileCopyrightText: 2024 Ken McCaughey
| SPDX-License-Identifier: Creative Commons Attribution-ShareAlike 4.0

PURPOSE:
  Help create an ARISS Moderator Script used for ISS school contacts.
  It is based on a template and a file containing variables. Basically
  works like a mail merge. Takes care of the script timeline and time math.

DISCLAIMER:
  This free software is provided as is.

DESCRIPTION:
  - Written using PyCharm for Python 3.10 on Linux Manjaro.
  - Requires a MS-Word docx file used as a template. The template is
    populated with variables to be filled in.
  - Reads a text file with the list of variables.
  - The script takes the variables and populates the occurrences in
    the template. It also does timeline calculations and generates
    timeline variables, which also get populated.
  - An outline report is generated.
  - A new MS-Word docx file is generated.
  - The template docx and form text input files are not changed.
  - The script docx file can be edited as needed.
  - A blank moderator script form file is created.

USAGE:
  - MS-Word docx template file and form text file are expected in same
    folder as the script executable.
  - Assumes fixed file names for template and form file.
  - The MS-Word docx file used as the template needs to have variables
    inside double braces, i.e. {{variable}}. The same variable can be
    used multiple times. See README files for list of valid variables.
  - The blank form text file maps all the variables to their descriptions.
    The variables are shown inside double braces, i.e. {{variable}}.
  - Moderator script is divided into event blocks. Each block has a number.
    Same numbers are used for event times (T##), time to ISS Rise (R##),
    and durations (D##). These need to match for this to work.
  - Two output files are generated. The MS-Word docx Moderator Script, named
    short name and version, and a timeline report file with fixed file name.
  - Works with docx files generated/edited with Libre Writer and saved in
    docx format.
  - Limited error checking for input file names and date + time formats.

MAKING EXECUTABLE VERSIONS:
  - On Linux use command line:
      pyinstaller --clean -w -F -i "ARISS_logo_simple.ico" ARISS_mod_script_gen.py
  - Windows 10 pyinstaller command line
      pyinstaller --clean --console -F -i "ARISS_logo_simple.ico" ARISS_mod_script_gen.py

EXTERNAL CREDITS:
  How to Generate Automated Word Documents with Python
  https://plainenglish.io/blog/how-to-generate-automated-word-documents-with-python-d6b7f6d3f801

TODO (top level):
  - Maybe make a version where file names can be passed on command line?
"""

# === LIBRARIES (must be first) ===
from docxtpl import DocxTemplate
from datetime import datetime
from datetime import timedelta

# Version info
version_date = '2024-11-30'
version = '3.0.0'

# === USER CONFIGURATION ===
# Display outline report on commandline?
display = 'N'  # 'Y' yes display, or 'N' no, do not display.

# --- Input filenames. These should not be changed. ---
# Import docx template document, it must be this file name.
template_file = 'ARISS_mod_script_temp.docx'
# Form file should be in same folder as executable and must be this file name.
form_file = 'ARISS_mod_script_form.txt'

# --- Output filenames. These should not be changed. ---
# Blank form file should be in same folder as executable.
blank_form_file = 'ARISS_mod_script_form_blank.txt'
# Final script file prefix. Final name is built below.
script_file_prefix = 'ARISS_mod_script_'
# Outline report file prefix. Final name is built below.
outline_report_file_prefix = 'ARISS_mod_script_outline_'  

# --- Declare variables ---
# These should not need to be changed.
pass_len = 11  # Pass length, typical, in minutes.

# Dictionary default keys and values.
#   The keys (field names) need to match what is in the form text file.
#   The values (variables) need to match what is used in the template file.
#   All the variables in the double braces {{ }} in the template document
#   will get replaced with values from the text form file. The list below
#   are the default field names used by the dictionary keys and the default
#   values. The values will get replaced by new ones from the form file.
# NOTE: IF ANY OF THESE CHANGE, THE BLANK FORM AND THE CONTEXT BELOW BOTH
#   NEED TO CHANGE AND MATCH.
a_dictionary = {
    # Script version
    'Script version': '{{version}}',
    'Short name': 'test',
    # Important Dates and Times
    'Date of contact (YYYY-MM-DD)': version_date,
    'Start of conference in UTC time (HH:mm)': '01:00',
    'Start of conference school time (HH:mm)': '02:00',
    'ISS rise in UTC time (HH:mm)': '03:00',
    'ISS rise school time (HH:mm)': '04:00',
    # School/Group Information
    'School/group name': '{{school_group_name}}',
    'School/group location': '{{school_group_city_state}}',
    'Coordinator/teacher at venue': '{{school_coordinator_name}}',
    'Venue phone number': '{{school_coordinator_phone}}',
    'Emergency back-up phone number': '{{school_coordinator_backup_phone}}',
    'School principal name': '{{principal_name}}',
    'School teacher name': '{{teacher_name}}',
    # ISS Information
    'Astronaut name': '{{astronaut_name}}',
    'Astronaut callsign': '{{astronaut_callsign}}',
    'ISS callsign to be used': '{{ISS_callsign}}',
    # ARISS Moderator Information
    'Moderator name': '{{moderator_name}}',
    'Moderator callsign': '{{moderator_callsign}}',
    'Moderator phone number': '{{moderator_phone}}',
    'Moderator will be On-site/Remote for the contact': '{{moderator_location}}',
    # ARISS Mentor Information
    'Mentor name': '{{mentor_name}}',
    'Mentor callsign': '{{mentor_callsign}}',
    'Mentor phone number': '{{mentor_phone}}',
    'Mentor will be On-site/Remote for the contact': '{{mentor_location}}',
    # ARISS Tele-bridge Ground Station
    'Tele-bridge station callsign': '{{telebridge_callsign}}',
    'Tele-bridge station location': '{{telebridge_location}}',
    'Tele-bridge station telephone number': '{{telebridge_phone}}',
    'Tele-bridge operator name': '{{operator_name}}',
    'Tele-bridge operator callsign': '{{operator_callsign}}',
    'Tele-bridge operator phone number': '{{operator_phone}}',
    'Tele-bridge support name(s) and callsign(s)': '{{support_names_callsigns}}',
    'Tele-bridge audio interface': '{{audio_interface}}',
    'Tele-bridge video interface': '{{telebridge_video}}',
    # ARISS optional videos
    'Contact from student perspective (Yes/No)': 'Yes',
    'Contact from the ISS perspective (Yes/No)': 'Yes',
    # Live Stream
    'Live stream planned (Yes/No)': 'No',
    'Live stream operator name': '{{livestream_name}}',
    'Live stream operator callsign': '{{livestream_callsign}}',
    'Live stream operator phone number': '{{livestream_phone}}',
}  # End of dictionary initialization.


# ========================================================================
# FUNCTIONS
# ========================================================================

def read_form_file():
    """
    Description:
    - Try to read form text file.
    - Fill dictionary with form variable values.
    - Saves the file.
    Output:
      Dictionary with form variable values.
    TODO (make_mod_script_file): None.
    """
    # File uses '#' for comments.
    # Form file data read into a dictionary.
    try:
        a_file = open(form_file, encoding="utf-8")  # Open configuration text file.
        print('Form text file found...')
    except FileNotFoundError:  # If form file not found error, create one.
        print('ERROR -', form_file, 'file not found.')
        exit(1)
    for line in a_file:  # Loop through eac line in text file.
        # print(line)
        # Ignore comment lines starting with '#', blank space, or new line.
        if not (line.startswith('#') or line.startswith('\n') or line.startswith(' ')):
            key, value = line.split(': ')  # Separate keys from values based on colon and space.
            a_dictionary[key] = value.strip('\n')  # Load dictionary. Remove newlines from values.
    # print('Form text file read...')
    # Print form dictionary. Used to verify all the elements are being read in correctly.
    # Can be commented out.
    # print()
    # print('Form Dictionary')
    # print(a_dictionary)
    # print()
    # End of function read_form_file().


def make_output_filename(file_prefix, ext):
    """
    Description:
      - Generates outline report filename based on information from form file.
    Output:
      Outline report filename
    TODO (make_output_report_filename): None.
    """
    # Build timeline report file name using variables from form file.
    file_name = file_prefix + a_dictionary['Short name'] + '_V' + a_dictionary['Script version'] + ext
    return file_name
    # End of function make_output_filename().


def time_calcs():
    # --- Timeline calculations. ---

    # Timeline durations specified in minutes.
    # Numbers correspond to script event block numbers.
    # TODO (time_calcs): None.
    d01 = a_dictionary['D01']  # Default = 3. Start conference.
    d02 = a_dictionary['D02']  # Default = 2. Moderator ground station checklist.
    d03 = a_dictionary['D03']  # Default = 5. Contact preparation prior to start of school/group program.
    d04 = a_dictionary['D04']  # Default = 10. Run through with all students and ground station.
    # d05 is the School/group program. It is the remaining time after accounting for all other event blocks.
    d06 = a_dictionary['D06']  # Default = 1. Start ARISS program.
    d07 = a_dictionary['D07']  # Default = 3. ARISS moderator introduction.
    d08 = a_dictionary['D08']  # Default = 6. Video of ARISS contact from student perspective.
    d09 = a_dictionary['D09']  # Default = 3. Video of ARISS contact from ISS perspective.
    d10 = a_dictionary['D10']  # Default = 3. Introduce the ground station.
    d11 = a_dictionary['D11']  # Default = 1. Handover to ground station.
    d12 = a_dictionary['D12']  # Default = 1. ISS contact!
    d13 = a_dictionary['D13']  # Default = 2. Closing remarks & end of ARISS program.

    # Check to see if either of the two optional videos are to be included.
    # If not, zero out the respective durations.
    if a_dictionary['Contact from student perspective (Yes/No)'] == 'No':
        d08 = 0
    if a_dictionary['Contact from the ISS perspective (Yes/No)'] == 'No':
        d09 = 0

    # In-elegant cumulative time durations from AOS needed for calculating times from AOS to start of ARISS program.
    ad13 = int(d13)
    # AD14 = AD13 + int(D14)
    ad12 = -1 * int(d12)
    ad11 = (ad12 - int(d11))
    ad10 = (ad11 - int(d10))
    ad09 = (ad10 - int(d09))
    ad08 = (ad09 - int(d08))
    ad07 = (ad08 - int(d07))
    ad06 = (ad07 - int(d06))

    # Timeline calculation anchor times.

    aos_date = a_dictionary['Date of contact (YYYY-MM-DD)']  # Get contact date from form file.
    aos_time = a_dictionary['ISS rise school time (HH:mm)']  # Get AOS time from form file.
    aos = aos_date + ' ' + aos_time  # AOS date and time string.
    try:
        aos_obj = datetime.strptime(aos, '%Y-%m-%d %H:%M')  # Convert AOS string to time object.
    except ValueError:
        print('ERROR - Date of contact (YYYY-MM-DD) in form file has incorrect format.')
        exit(1)
    conf_time = a_dictionary['Start of conference school time (HH:mm)']  # Get start of conference time from form file.
    conf_start_time = aos_date + ' ' + conf_time  # Conference start date and time string.
    try:
        # Convert conference time to time object.
        conf_start_time_obj = datetime.strptime(conf_start_time, '%Y-%m-%d %H:%M')
    except ValueError:
        print('ERROR - Start of conference school time (HH:mm) in form file has incorrect format.')
        exit(1)

    # Calculate event block times based on durations and anchor times.
    # Numbers correspond to script event block numbers.
    t01 = time_calc(conf_time, 0)  # Start conference.
    t02 = time_calc(t01, d01)  # Moderator ground station checklist.
    t03 = time_calc(t02, d02)  # Contact preparation checklist.
    t04 = time_calc(t03, d03)  # Run through with all students and ground station.
    t05 = time_calc(t04, d04)  # Start school/group program.
    t06 = time_calc(aos_time, ad06)  # Start ARISS program.
    t07 = time_calc(aos_time, ad07)  # ARISS moderator introduction.
    t08 = time_calc(aos_time, ad08)  # Video of an ARISS contact from the student perspective.
    t09 = time_calc(aos_time, ad09)  # Video of an ARISS contact from the ISS perspective.
    t10 = time_calc(aos_time, ad10)  # Introduce the ground station.
    t11 = time_calc(aos_time, ad11)  # Handover to ground station.
    t12 = time_calc(aos_time, ad12)  # ISS contact!
    los = time_calc(aos_time, pass_len)  # Loss of Signal.
    t13 = time_calc(aos_time, pass_len)  # Closing remarks & end of ARISS program.
    # Calculated time to AOS in minutes based on timeline.
    # Numbers correspond to script event block numbers.
    r01 = aos_calc(aos_time, t01)
    r02 = aos_calc(aos_time, t02)
    r03 = aos_calc(aos_time, t03)
    r04 = aos_calc(aos_time, t04)
    r05 = aos_calc(aos_time, t05)
    r06 = aos_calc(aos_time, t06)
    r07 = aos_calc(aos_time, t07)
    r08 = aos_calc(aos_time, t08)
    r09 = aos_calc(aos_time, t09)
    r10 = aos_calc(aos_time, t10)
    r11 = aos_calc(aos_time, t11)
    r12 = aos_calc(aos_time, t12)

    # D05 is the School/group program. It is the remaining time after accounting for all other event blocks.
    d05 = aos_calc(t06, t05)  # School/group program.

    # Summary durations
    d14 = str(int(d01) + int(d02) + int(d03) + int(d04))
    d15 = str(int(d05))
    d16 = str(int(d06) + int(d07) + int(d08) + int(d09) + int(d10) + int(d11) + int(pass_len) + int(d13))
    d17 = str(int(d01) + int(d02) + int(d03) + int(d04) + int(d05) + int(d06) + int(d07) + int(d08) + int(d09)
              + int(d10) + int(d11) + int(pass_len) + int(d13))

    # print('Timeline calculations complete...')
    return (aos_date, aos_time, conf_time, conf_start_time,
            d01, d02, d03, d04, d05, d06, d07, d08, d09, d10, d11, d12, d13, d14, d15, d16, d17,
            los,
            r01, r02, r03, r04, r05, r06, r07, r08, r09, r10, r11, r12,
            t01, t02, t03, t04, t05, t06, t07, t08, t09, t10, t11, t12, t13
            )
    # End of function time_calcs().


def make_outline_report_file(d):
    """
    Description:
      - Creates a moderator script outline report file.
      - Saves the file.
    Output:
      ARISS_moderator_script_outline.txt.
      Prints report to the terminal.
    TODO (make_outline_report_file): None.
    """
    report_text = ['',
                   'ARISS Moderator Script Outline',
                   '==============================',
                   '',
                   'School / group: ' + a_dictionary['School/group name'],
                   'ISS contact on: ' + a_dictionary['Date of contact (YYYY-MM-DD)'],
                   'Script version: ' + a_dictionary['Script version'],
                   '',
                   'Note: All times are local school time (24hr).',
                   '      Event durations and times to ISS Rise and are in minutes (m).',
                   '',
                   'Conference start at: ' + Conf_start_time,
                   'ISS rise time (AOS): ' + AOS_time,
                   'Tele-bridge station: ' + a_dictionary['Tele-bridge station callsign'] + ', '
                   + a_dictionary['Tele-bridge station location'],
                   '',
                   'Time   Dur  Rise  Event Block Description',
                   '-----  ---  ----  -------------------------------------------------',
                   T01 + '  ' + space(D01) + 'm   ' + space(R01) + 'm  Start conference',
                   T02 + '  ' + space(D02) + 'm   ' + space(R02) + 'm  Moderator ground station checklist',
                   T03 + '  ' + space(D03) + 'm   ' + space(R03) + 'm  Contact preparation checklist',
                   T04 + '  ' + space(D04) + 'm   ' + space(R04) + 'm  Run through with all students & ground station',
                   T05 + '  ' + space(D05) + 'm   ' + space(R05) + 'm  School/group program.(Optional)',
                   T06 + '  ' + space(D06) + 'm   ' + space(R06) + 'm  Start ARISS program',
                   T07 + '  ' + space(D07) + 'm   ' + space(R07) + 'm  ARISS introduction',
                   T08 + '  ' + space(D08) + 'm   ' + space(R08) + 'm  Optional video from student perspective - '
                   + a_dictionary['Contact from student perspective (Yes/No)'],
                   T09 + '  ' + space(D09) + 'm   ' + space(R09) + 'm  Optional video from the ISS perspective - '
                   + a_dictionary['Contact from the ISS perspective (Yes/No)'],
                   T10 + '  ' + space(D10) + 'm   ' + space(R10) + 'm  Introduce the ground station',
                   T11 + '  ' + space(D11) + 'm   ' + space(R11) + 'm  Handover to ground station',
                   T12 + '  ' + space(D12) + 'm   ' + space(R12) + 'm  ISS rise and Acquisition of Signal (AOS)',
                   AOS_time + '  ' + space(pass_len) + 'm    0m  ISS contact!.',
                   LOS + '   -     -   ISS set and Loss of Signal (LOS)',
                   T13 + '  ' + space(D13) + 'm    -   Closing remarks & end of ARISS program',
                   '',
                   'Any events with 0m duration have been eliminated from the program,',
                   'but are not removed from the calculation report.',
                   '',
                   'Based on conference call start time, ISS rise time, and ARISS ',
                   'durations (prep & program), the school/group program time, or slack',
                   'time, is estimated to be no more than ' + str(D05) + ' minutes starting at ' + str(T05) + '.',
                   '',
                   'Contact preparation     ~' + str(int(D01) + int(D02) + int(D03) + int(D04)) + 'm',
                   'School/group program    ~' + str(int(D05)) + 'm',
                   'ARISS program/contact   ~' + str(int(D06) + int(D07) + int(D08) + int(D09) + int(D10) + int(D11) +
                                                     int(pass_len) + int(D13)) + 'm',
                   '============================',
                   'Total event duration    ~' + str(int(D01) + int(D02) + int(D03) + int(D04) + int(D05) + int(D06) +
                                                     int(D07) + int(D08) + int(D09) + int(D10) + int(D11) +
                                                     int(pass_len) + int(D13)) + 'm',
                   '',
                   'Made Using Python ARISS Moderator Script Generator Version ' + str(version) + '.',
                   ''
                   ]
    # Create config file.
    with open(outline_report_file, 'w', encoding="utf-8") as f:
        for text_line in report_text:
            f.write(text_line)  # Write line to file.
            if d == 'Y':
                print(text_line)  # Print line to screen (optional).
            f.write('\n')
    # End of function make_outline_report_file().


def space(number_int):
    """
    Takes integer number & outputs a 2 digit string with space zero, if needed.
    Used to make timeline table columns neater.
    TODO (space) - None.
    """
    number_int = int(number_int)
    # print(number_int)
    number_str = str(number_int)
    if number_int < 10:
        number_str = ' ' + number_str
    # print(number_str)
    return number_str
    # End of function space().


def time_calc(base_time_str, delta_min):
    """
    Calculate new time given a base time and delta in minutes.
    TODO (time_calc) - None.
    """
    # Get contact date from form file.
    AOS_date = a_dictionary['Date of contact (YYYY-MM-DD)']  
    base_time_str = AOS_date + ' ' + base_time_str
    base_time_obj = datetime.strptime(base_time_str, '%Y-%m-%d %H:%M')
    delta_obj = timedelta(minutes=int(delta_min))
    calc_time_obj = base_time_obj + delta_obj
    calc_time_str = calc_time_obj.strftime('%H:%M')
    return calc_time_str
    # End of function time_calc().


def aos_calc(base_time_str, delta_time_str):
    """
    Calculate delta in integer minutes given two times.
    TODO (aos_calc) - None.
    """
    # Get contact date from form file.
    AOS_date = a_dictionary['Date of contact (YYYY-MM-DD)']  
    base_time_str = AOS_date + ' ' + base_time_str
    delta_time_str = AOS_date + ' ' + delta_time_str
    base_time_obj = datetime.strptime(base_time_str, '%Y-%m-%d %H:%M')
    delta_time_obj = datetime.strptime(delta_time_str, '%Y-%m-%d %H:%M')
    calc_delta_obj = base_time_obj - delta_time_obj
    calc_delta_str = int(calc_delta_obj.total_seconds() / 60)
    return calc_delta_str
    # End of function aos_calc().


def build_output_dictionary():
    """
    Description:
      Fill output dictionary with form variable values and new calculated variables.
    Output:
      Output dictionary with variable values to merge with the template.
    TODO (build_output_dictionary): None.
    """
    # Variables to be incorporated into new file.
    #   Dictionary to be written to the template creating the new script.
    #   The keys (variable names) need to match what is in the variables,
    #   in the double braces {{ }}, in the template document, and will
    #   get replaced with values read from the text form file or calculated
    #   by this  Python script.
    # NOTE: IF ANY OF THESE CHANGE, THE DICTIONARY AND THE BLANK FORM ABOVE
    #   BOTH NEED TO CHANGE AND MATCH.
    context = {
        # Python tool version
        'tool_version': version,
        # Timeline (calculated)
        'T01': T01, 'A01': R01, 'D01': D01,
        'T02': T02, 'A02': R02, 'D02': D02,
        'T03': T03, 'A03': R03, 'D03': D03,
        'T04': T04, 'A04': R04, 'D04': D04,
        'T05': T05, 'A05': R05, 'D05': D05,
        'T06': T06, 'A06': R06, 'D06': D06,
        'T07': T07, 'A07': R07, 'D07': D07,
        'T08': T08, 'A08': R08, 'D08': D08,
        'T09': T09, 'A09': R09, 'D09': D09,
        'T10': T10, 'A10': R10, 'D10': D10,
        'T11': T11, 'A11': R11, 'D11': D11,
        'T12': T12, 'A12': R12, 'D12': D12,
        'T13': T13, 'D13': D13, 'D14': D14,
        'D15': D15, 'D16': D16, 'D17': D17,
        # Version from form file
        'version': a_dictionary['Script version'],
        # Dates and times from form file
        'contact_date': a_dictionary['Date of contact (YYYY-MM-DD)'],
        'conf_UTC': a_dictionary['Start of conference in UTC time (HH:mm)'],
        'conf_sch': a_dictionary['Start of conference school time (HH:mm)'],
        'AOS_UTC': a_dictionary['ISS rise in UTC time (HH:mm)'],
        'AOS_sch': a_dictionary['ISS rise school time (HH:mm)'],
        # School info from form file
        'school_group_name': a_dictionary['School/group name'],
        'school_group_city_state': a_dictionary['School/group location'],
        'school_coordinator_name': a_dictionary['Coordinator/teacher at venue'],
        'school_coordinator_phone': a_dictionary['Venue phone number'],
        'school_coordinator_backup_phone': a_dictionary['Emergency back-up phone number'],
        'principal_name': a_dictionary['School principal name'],
        'teacher_name': a_dictionary['School teacher name'],
        # ISS info from form file
        'astronaut_name': a_dictionary['Astronaut name'],
        'astronaut_callsign': a_dictionary['Astronaut callsign'],
        'ISS_callsign': a_dictionary['ISS callsign to be used'],
        # ARISS moderator info from form file
        'moderator_name': a_dictionary['Moderator name'],
        'moderator_callsign': a_dictionary['Moderator callsign'],
        'moderator_phone': a_dictionary['Moderator phone number'],
        'moderator_location': a_dictionary['Moderator will be On-site/Remote for the contact'],
        # ARISS mentor info from form file
        'mentor_name': a_dictionary['Mentor name'],
        'mentor_callsign': a_dictionary['Mentor callsign'],
        'mentor_phone': a_dictionary['Mentor phone number'],
        'mentor_location': a_dictionary['Mentor will be On-site/Remote for the contact'],
        # ARISS tele-bridge info from form file
        'telebridge_callsign': a_dictionary['Tele-bridge station callsign'],
        'telebridge_location': a_dictionary['Tele-bridge station location'],
        'telebridge_phone': a_dictionary['Tele-bridge station telephone number'],
        'operator_name': a_dictionary['Tele-bridge operator name'],
        'operator_callsign': a_dictionary['Tele-bridge operator callsign'],
        'operator_phone': a_dictionary['Tele-bridge operator phone number'],
        'support_names_callsigns': a_dictionary['Tele-bridge support name(s) and callsign(s)'],
        'audio_interface': a_dictionary['Tele-bridge audio interface'],
        'telebridge_video': a_dictionary['Tele-bridge video interface'],
        # ARISS optional videos
        'student_video': a_dictionary['Contact from student perspective (Yes/No)'],
        'ISS_video': a_dictionary['Contact from the ISS perspective (Yes/No)'],
        # Live Stream
        'livestream_plan': a_dictionary['Live stream planned (Yes/No)'],
        'livestream_name': a_dictionary['Live stream operator name'],
        'livestream_callsign': a_dictionary['Live stream operator callsign'],
        'livestream_phone': a_dictionary['Live stream operator phone number'],
    }
    return context
    # End of function build_output_dictionary().


def make_mod_script_file(context):
    """
    Description:
      - Creates a moderator script file.
      - Uses 'context' array
      - Saves the file.
    Output:
      ARISS Moderator Script docx file.
    TODO (make_mod_script_file): None.
    """
    # --- Make script file ---
    # Render automated report.
    template = DocxTemplate(template_file)
    try:
        # Read list that maps template variables with form data read from file.
        template.render(context)  
        print('Template file found...')
    except:  # File not found error.
        print('=====')
        print('ERROR -', template_file, 'is missing or has or spelling error.')
        print('=====')
        exit(1)
    # Create new MS-Word file.
    template.save(script_file)
    # print('New moderator script generated...')
    # End of function make_mod_script_file().


def make_blank_form_file():
    """
    Description:
      - Creates a moderator script form text file.
      - Saves the file.
    Output:
      ARISS_moderator_script_form_blank.txt.
    TODO (Make_Blank_Form_File): None.
    """
    # NOTE: IF ANY OF THESE CHANGE, THE DICTIONARY ABOVE AND THE CONTEXT
    #   BELOW BOTH NEED TO CHANGE AND MATCH.
    form_text = [
        '# ARISS Moderator Script Generator Form',
        '# =====================================',
        '#   By: Ken McCaughey (N3FZX)',
        '#   On: ' + version_date,
        '#   Ver ' + version,
        '#',
        '# This form is used to generate an ARISS moderator script.',
        '# The Python script ARISS_mod_script_gen.py will read this',
        '# form and combine with a script template to create a',
        '# complete moderator script in a properly formatted MS-WORD',
        '# document and a timeline report.',
        '#',
        '# The script timeline is calculated based on estimated durations',
        '# of the event blocks.',
        '#',
        '# THINGS TO KNOW ABOUT THIS FORM:',
        '#',
        '#   Lines that begin with a "#" are comments.',
        '#   Feel free to add more comments to make notes.',
        '#   The form consists of a list of field names and variables.',
        '#     Field name: {{variable}}',
        '#     School/group name: {{school_group_name}}',
        '#   Field names must be separated from variables with a colon+space',
        '#     ": "',
        '#',
        '# INSTRUCTIONS:',
        '#',
        '#   Replace the variables, including {{ and }}, with known data.',
        '#   For example:',
        '#     School/group name: {{school_group_name}}',
        '#     School/group name: My school',
        '#   Be sure to update the version number if doing a revision.',
        '#   Do NOT change the field names.',
        '#   Do NOT add or remove lines, except for comments.',
        '#   Do NOT use line breaks, carriage returns or hard word wrap',
        '#     for any long lines.',
        '#   Adjust timeline event block durations only as needed.',
        '#',
        '',
        '# === START HERE ===',
        '',
        '# ==============',
        '# Script version',
        '# ==============',
        '# Update this each time just before a new WORD doc is generated.',
        'Script version: {{version}}',
        '',
        '# Short one word nickname to be added to the output filenames.',
        'Short name: test',
        '',
        '# =========================',
        '# Important Dates and Times',
        '# =========================',
        '# Only enter numbers in the specified formats.',
        'Date of contact (YYYY-MM-DD): 2024-11-30',
        '',
        '# Conference typically starts 1 hour before ISS Rise & AOS.',
        'Start of conference in UTC time (HH:mm): 01:00',
        'Start of conference school time (HH:mm): 02:00',
        '',
        '# Round down ISS rise time to the nearest minute.',
        'ISS rise in UTC time (HH:mm): 03:00',
        'ISS rise school time (HH:mm): 04:00',
        '',
        '# ========================',
        '# School/Group Information',
        '# ========================',
        'School/group name: {{school_group_name}}',
        'School/group location: {{school_group_city_state}}',
        'Coordinator/teacher at venue: {{school_coordinator_name}}',
        'School principal name: {{principal_name}}',
        'School teacher name: {{teacher_name}}',
        '',
        '# ===============',
        '# ISS Information',
        '# ===============',
        'Astronaut name: {{astronaut_name}}',
        'Astronaut callsign: {{astronaut_callsign}}',
        'ISS callsign to be used: {{ISS_callsign}}',
        '',
        '# ===========================',
        '# ARISS Moderator Information',
        '# ===========================',
        'Moderator name: {{moderator_name}}',
        'Moderator callsign: {{moderator_callsign}}',
        'Moderator will be On-site/Remote for the contact: {{moderator_location}}',
        '',
        '# ========================',
        '# ARISS Mentor Information',
        '# ========================',
        'Mentor name: {{mentor_name}}',
        'Mentor callsign: {{mentor_callsign}}',
        'Mentor will be On-site/Remote for the contact: {{mentor_location}}',
        '',
        '# ================================',
        '# ARISS Tele-bridge Ground Station',
        '# ================================',
        'Tele-bridge station callsign: {{telebridge_callsign}}',
        'Tele-bridge station location: {{telebridge_location}}',
        'Tele-bridge operator name: {{operator_name}}',
        'Tele-bridge operator callsign: {{operator_callsign}}',
        '',
        '# Tele-bridge audio interface options: Verizon, Zoom Dial-in, Zoom Video, etc.',
        'Tele-bridge audio interface: {{audio_interface}}',
        '',
        '# Tele-bridge video interface options: None, Zoom, Google Meet, etc.',
        'Tele-bridge video interface: {{telebridge_video}}',
        '',
        '# =====================',
        '# ARISS Optional Videos',
        '# =====================',
        '# Default is Yes. Change to No to remove from the timeline.',
        'Contact from student perspective (Yes/No): Yes',
        'Contact from the ISS perspective (Yes/No): Yes',
        '',
        '# ==============',
        '# Live Streaming',
        '#===============',
        'Live stream planned (Yes/No): {{livestream_plan}}',
        'Live stream operator name: {{livestream_name}}',
        'Live stream operator callsign: {{livestream_callsign}}',
        '',
        '',
        '# ====================',
        '# Timeline assumptions',
        '# ====================',
        '# Below are the Event Blocks Duration estimates used for the',
        '#    timeline calculations. Defaults are based on experience.',
        '#    Default values are listed in the comments for reference.',
        '#    All durations are integer minutes.',
        '#    ONLY change these if necessary.',
        '',
        '# Event - Start conference.',
        '# Default duration = 3 min',
        'D01: 3',
        '',
        '# Event - Moderator ground station checklist.',
        '# Default duration = 2 min',
        'D02: 2',
        '',
        '# Event - Contact preparation checklist.',
        '# Default duration = 5 min',
        'D03: 5',
        '',
        '# Event - Run through with all students and ground station.',
        '# Default duration = 10 min',
        'D04: 10',
        '',
        '# Event - Start school/group program or slack time.',
        '# Nothing to change here.',
        '# The script calculates D05 time as a remainder of time left.',
        '',
        '# Event - Start ARISS program.',
        '# Default duration = 1 min',
        'D06: 1',
        '',
        '# Event - ARISS introduction.',
        '# Default duration = 4 min',
        'D07: 4',
        '',
        '# OPTIONAL Event - Video of ARISS contact from student perspective.',
        '# Default duration = 6 min',
        'D08: 6',
        '',
        '# OPTIONAL Event- Video of ARISS contact from ISS perspective.',
        '# Default duration = 3 min',
        'D09: 3',
        '',
        '# Event - Introduce the ground station.',
        '# Default duration = 3 min',
        'D10: 3',
        '',
        '# Event - Handover to ground station.',
        '# Default duration = 1 min',
        'D11: 1',
        '',
        '# Event - ISS contact!',
        '# Default duration = 1 min',
        'D12: 1',
        '',
        '# Event - Closing remarks & end of ARISS program.',
        '# Default duration = 3 min',
        'D13: 3',
        '',
        '# End of form',
        '',
    ]  # End of form text.
    # Create config file.
    with open(blank_form_file, 'w', encoding="utf-8") as f:
        for text_line in form_text:
            f.write(text_line)  # Write line to file.
            f.write('\n')
    # End of function make_blank_form_file().


# ========================================================================
# MAIN
# ========================================================================

# Print welcome message.
print()
print('Python script: ARISS_mod_script_gen.py')
print('           V.:', version)
print('           By: Ken McCaughey, N3FZX')
print('           On:', version_date)
print()
print('This tool creates an ARISS Moderator Script.')
print('It reads data from a form text file and a MS-Word docx template file.')
print('Then generates a complete script and timeline report.')
print()
print('Required Input Files:')
print('  Moderator form  -->', form_file)
print('  Script template -->', template_file)
print()

# Generate new blank forma file.
# - Call function any time.
make_blank_form_file()
print('Blank moderator form text file generated...')

# Read form test file to populate working dictionary of variable values.
# - Call function.
# - Must be run first.
read_form_file()
print('Form text file read...')

# Generate output filenames based on information from form file.
# - Call functions after reading form text file.
script_file = make_output_filename(script_file_prefix, '.docx')
outline_report_file = make_output_filename(outline_report_file_prefix, '.txt')
print('Output filenames generated...')

# Time calculations.
# - Call function after reading form text file.
(AOS_date, AOS_time, Conf_time, Conf_start_time,
 D01, D02, D03, D04, D05, D06, D07, D08, D09, D10, D11, D12, D13, D14, D15, D16, D17,
 LOS,
 R01, R02, R03, R04, R05, R06, R07, R08, R09, R10, R11, R12,
 T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13
 ) = time_calcs()
print('Timeline calculations complete...')

# Make outline report file.
# - Call function after time calculations.
# - Optionally display report on command line.
# - 'Y' yes display, or 'N' no, do not display. Set at top.
make_outline_report_file(display)  
print('Outline report file generated...')

# Build output dictionary based on form test file and calculated variables.
# - Call function after time calculations.
Context = build_output_dictionary()
print('Variable dictionary updated...')

# Generate moderator script file.
# - Call function after building output dictionary.
make_mod_script_file(Context)
print('New moderator script generated...')

# Print output filenames.
print()
print('Output Files Created:')
print('  Blank form file -->', blank_form_file)
print('  Outline report  -->', outline_report_file)
print('  Complete script -->', script_file)
print()
print('Success!')

# The End
print()
print('Python Script Done')

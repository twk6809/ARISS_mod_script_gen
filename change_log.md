ARISS Moderator Script Generator - Change Log
=============================================

This record only covers official releases and not any interim development
versions.  

V4.0.0 - 2026-02-04
-------------------
- Made a lot of changes under the hood to better position the tool for 
  generating scripts telebridge and direct contacts.  Many of the field
  names and variables were renamed to be a bit more generic.
- Added the "short name" variable to the catalog of output variables so it 
  can be used in the template doc. It is specifically designed to be used 
  on the footers of the template pages. 
- Added time zone shift variable. This is simply a text value so that the
  UTC time zone shift can be denoted. It is important to understand that
  the tool does NOT check the UTC time zone and time zone abbreviation to 
  see that they match. Likewise, the value is NOT used for any time math.
- Added some error checking for event times. Checks that the conference
  start time is before the ISS rise time. Also checks to make sure there is 
  enough time for all the event blocks. Warns if conference start is too late.
- Cleaned up the form file. Demoted some variables that are really not used 
  or needed. Adjusted the default event block timings to account for an 
  expanded checklist and the new ISS video, which is a bit longer.
- Updated all templates. Added the new Nichole Ayers ARISS ISS video, 
  replacing the Time Peake version. Updated YouTube links and added DropBox 
  links for downloading the videos. Cleaned up template wording and reduced 
  the number of customization notes. Added short name and version to the 
  footer of each page for better version control. Fixed some wording and typos.
- Updated all templates to use renamed variables.
- Created a new template to accommodate a language translation. This is new
  and somewhat experimental based on a custom template that was used for an
  ARISS contact. See the template catalog for more details.
- Created new templates that only have one or the other videos. There are 
  now templates for both videos, first video only, second video only, or no
  videos. This reduces the template edits.
- Created template that is just the timeline and logistics and no script. 
- Reworked and updated the README to reflect the variable changes. Added a 
  section for suggestions for success. Updated the troubleshooting tips. 
- Updated the HELPER file.


V3.1.2 - 2026-02-02 (unofficial limited release)
-------------------
- Added the "short name" variable to the catalog of output variables so it 
  can be used in the template doc. It is specifically designed to be used 
  on the footers of the template pages. 
- Added time zone shift variable. This is simply a text value so that the
  UTC time zone shift can be denoted. It is important to understand that
  the tool does NOT check the UTC time zone and time zone abbreviation to 
  see that they match. Likewise, the value is NOT used for any time math.
- Added some error checking for event times. Checks that the conference
  start time is before the ISS rise time. Also checks to make sure there is 
  enough time for all the event blocks.
- Cleaned up the form file. Demoted some variables that are really not
  used. Adjusted the default event block timings to account for an expanded 
  checklist and the new ISS video, which is a bit longer.
- Updated templates. Added the new ARISS ISS video, replacing the Time Peake
  version. Also cleaned up template wording and reduced the number of 
  customization notes. Added short name and version to the footer of each
  page for better version control. Fixed some wording and typos.
- Created a new template to accommodate a language translation. This is new
  and somewhat experimental based on a custom template that was used for an
  ARISS contact. See the template catalog for more details.
- Created news templates that only have one or the other videos. There are 
  now templates for both videos, first video only, second video only, or no
  videos. This reduces the template edits.
- Updated the README to reflect the variable changes. Added a section for 
  suggestions for success. Updated the troubleshooting tips. 


V3.1.1 - 2025-11-02 (unofficial limited release)
-------------------
- Added the "short name" variable to the catalog of output variables so it 
  can be used in the template doc. It is specifically designed to be used 
  on the footers of the template pages. 


V3.1.0 - 2025-05-20
-------------------
- Added new variable to the form file: `Event time zone: {{etz}}`. It is 
  simply designed to capture and report the time zone abbreviation for
  informational purposes. No calculations are based on this value. 
- Added new variable to the form file: `School/group presenter name:`
  `{{presenter_name}}`. Since the school/group presenter could be the 
  principal, teacher, or someone else, it was easier to just separate 
  out that role. This will be carried over to the templates I provide.
- In the form file added annotation for the event timing. Each event
  block has a number. This will be carried over to the templates I 
  provide.
- Cleaned up the outline report. Added the event time zone. Added event
  block numbers. Fixed some number alignments to allow for duration or 
  minutes until times that might use three digits.
- Fixed a bug in the form file for the optional videos. The Yes/No 
  answer was case sensitive. Now case no longer matters. If anything 
  other than No (or no, or NO, or nO) is entered it defaults to Yes.
- Updated the README and HELPER files to reflect the variable changes.


V3.0.1 - 2025-02-16
-------------------
- Improved error handling. Especially for common errors in the form file.
  Provides more useful feedback on what to look for to fix the form file.
- Updated the instructions in the form file.
- Updated the README and HELPER files. Improved instructions in the work 
  flow.
- Removed instruction for making native binaries. That is a more advanced 
  topic and out of scope for most users of this tool. 
- Jettisoning native binaries for Windows and Mac-OS. Too difficult to 
  maintain and too many difficulties with anti-virus programs flagging them.
- Updated the folder structure. Eliminated some unnecessary files.


V3.0.0 - 2024-11-30
-------------------
- Additional changes to the variable list. Added variables for live 
  streaming and the two ARISS videos. Changed the AOS and LOS nomenclature 
  to ISS rise and set times.
- Updated the form file. Streamlined to minimal data set.
- Improved the README file. Included the full list of variables available.
- Generated a HELPER file. Has instructions on how to use Python. Also has
  details on how to use the Thonny IDE to help make it easier for beginner
  Python users. Has info on how to make native binaries.
- Streamlined the file names to be a bit shorter.
- Re-organized the internal code into more functions. 
- Reduced the command line terminal output text.
- Updated the template file, and expanded it to several templates. Reduced
  the number of red-line notes to edit. Cleaned up the text to make it more
  universal. Have a long and short versions that are with and without the 
  two ARISS videos, respectively. Changed the AOS and LOS nomenclature to 
  ISS rise and set times. Eliminated colored text, expect for the red 
  editorial notes.
- Updated the outline report with more information. Video use more 
  explicitly indicated.
- Made a separate instruction file for moderators with a checklist.


V2.0 - 2023-11-05
-----------------
- Updated variable list.
- Updated form file. Added some variables
- Made changes to the template file format. Removed phone numbers.
- Made changes to template file. Removed event block numbering.
- Generated a README file.
- Fixed bugs.  


V1.3 - 2023-05-21
-----------------
- Baseline release. Previous versions were developmental.

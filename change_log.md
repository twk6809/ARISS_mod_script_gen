ARISS Moderator Script Generator - Change Log
=============================================

This record only covers official releases and not any interim development
versions.  

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
- Baseline release. 

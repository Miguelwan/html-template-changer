# html-template-changer
## Introduction
This is a simple script in python to make modifications on html files of a webpage. The script was made under the assumption that all the html files to modify have the same structure (same id markers, tag paths, etc).

## How it works

### Setting up
The script uses the packeges beautifullsoup and pandas between others, the packages requiered to run the script can be foundin requirements.txt, these packages should be installed before running the script.
The html files that will be modified must be in the same folder as the script, also the file webpages.csv.
The file webpages.csv must contain the name of the html files that will be modify, in the column "webpage".

### Running the scrip
The script starts with a main menu with three options:

*Inspect index.html*
*Modify template*
*Exit.*

The option **Inspect index.html** is design to inspect the template and do the correct selction by tag, id, and/or attribute. Also it will allow to preview the changes on the file index.html. This menu is only for selection and preview only, no change is saved in this option.

The option **Modify template** is desing to applied the selected changes from * Inspect index.html * to all the files listed in webpages.csv.

### Inspect index.html
The option **Inspect index.html** contains the following options:

*Print index.html*
*Select id*
*Select tag*
*Select attribute*
*Show selection*
*Change content*
*Reset selection*
*Return to main menu.*

### Modify template
The option **Modify template** contains the following options:

*Load webpages list*
*Modify webpages*
*Return to main menu.*

# Extract external identifiers

Written by		David Saunders, Symplectic Helpdesk, Research Services, University of Oxford
Created date	19-05-2021
Updated date	19-05-2021

## Purpose
To enable easier reporting to funders of the publication identifiers (e.g. PubMed) of a list of publications (e.g. by user, or group)

## Description
This script takes the list of identifers in the 'External identifiers' field in the Symplectic Elements publications report (Basic Reports). It then writes the separate identifiers (pubmed,pmc,isidoc)to individual columns. n.b. Is specifically written for pubmed, pmc and isidoc identifiers.

## Input
Publications report from SE Basic Reports placed in the input folder (filename pubs.csv, see example file with headers only). This can be obtained from from Menu > Basic Reports. Select group or user. Object category : 'Publications (linked to the selected users)'. Since the script does not duplicate, you can use a report returning either 'Publications' or 'Publications by linked user'. Tick 'Display all fields'. The script identifies columns by index (column number) so whilst you can amend column names, do not add or remove columns from the input file.

Place in the input folder. See pubs.csv

## Output
Writes extids.csv to the output folder (see example file with headers only). 

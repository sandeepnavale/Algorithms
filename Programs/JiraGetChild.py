from jira import JIRA
import datetime
import getpass
import numpy as np
import pandas as pd
from pandas import ExcelWriter
# import matplotlib.pyplot as plt

user, passwd = 'nsandeep', '$unny1nAUS'
options = {'server': 'https://dev.pulsesecure.net/jira/'}
jira = JIRA(options, basic_auth=(user, passwd))
jqQIOpen_DevClosed = 'filter=SN_PCS_QI_Open_DevClosed'
# Search filter
jq = jqQIOpen_DevClosed

manualDf = pd.DataFrame()


allIssues = jira.search_issues(jq, expand="changelog", maxResults=5000)
i = 0


def getAllChild(parentIssue, i=0):
    for subissue in parentIssue.fields.subtasks:
        i += 1
        try:
            st = jira.issue(subissue.key)
        except NotImplementedError:
            print('ST ERROR NotImplementedError ')
            continue
        manualDf.loc[i, 'ParentKey'] = parentIssue.key
        manualDf.loc[i, 'ChildKey'] = st.key
        manualDf.loc[i, 'Summary'] = st.fields.summary
        if hasattr(st.fields, 'resolution') and st.fields.resolution:
            manualDf.loc[i, 'Resolution'] = st.fields.resolution.name

        if hasattr(st.fields, 'assignee') and st.fields.assignee:
            manualDf.loc[i, 'Assignee'] = st.fields.assignee.displayName
#             manualDf.set_value(i,'Email',st.fields.assignee.name)
#             print("\t ## Child -",st.key," - ",st.fields.assignee.displayName)
        if hasattr(st.fields, 'fixVersions') and len(st.fields.fixVersions) > 0:
            manualDf.loc[i, 'FixVersion'] = st.fields.fixVersions[0].name
        if hasattr(st.fields, 'status') and st.fields.status is not None:
            manualDf.loc[i, 'Status'] = st.fields.status.name
            manualDf.loc[i, 'Type'] = st.fields.issuetype.name
        if hasattr(st.fields, 'customfield_10114') and hasattr(st.fields.customfield_10114, 'value'):
            manualDf.loc[i, 'CustomerEscalation'] = st.fields.customfield_10114.value
#             print(i,"\t ## Child -",st.key,'Status -> ',
                # st.fields.status.name," -Type -  ",st.fields.issuetype)

        if hasattr(st.fields, 'Labels') and st.fields.labels is not None:
            manualDf.loc[i, 'Labels'] = st.fields.labels
#         if hasattr(st.fields,'customfield_11000') and st.fields.customfield_11000:
#             manualDf.loc[i,'DevOwner'] = st.fields.customfield_11000.key

    return i+1


i = 0
for issue in allIssues:
    print("Analysing [", issue.key, "]")
    try:
        if hasattr(issue.fields, 'parent') and issue.fields.parent.key is not None:
            parentIssue = jira.issue(issue.fields.parent.key)
            if parentIssue and hasattr(parentIssue, 'fields'):
                manualDf.loc[i, 'ParentKey'] = parentIssue.key
                manualDf.loc[i, 'Status'] = parentIssue.fields.status.name
#                 manualDf.loc[i,'Summary'] = parentIssue.fields.summary

            #Get Creation date
                IssueCreationDate = pd.Timestamp(parentIssue.fields.created)
                manualDf.loc[i, 'CreationDate'] = IssueCreationDate.date()

            #  Get Severity
                if hasattr(parentIssue.fields, 'customfield_10125'):
                    manualDf.loc[i, 'Severity'] = parentIssue.fields.customfield_10125.value

                #   Get Regression attributes.
                if hasattr(parentIssue.fields, 'customfield_10101') and parentIssue.fields.customfield_10101:
                    manualDf.loc[i, 'Attributes'] = parentIssue.fields.customfield_10101[0].value
                # update component
                if (len(parentIssue.fields.components) > 0):
                    manualDf.loc[i, 'Component'] = parentIssue.fields.components[0].name
                if hasattr(parentIssue.fields, 'customfield_11501') and hasattr(parentIssue.fields.customfield_11501,'value'):
                    manualDf.loc[i, 'FoundInVersion'] = parentIssue.fields.customfield_11501.value

            i = getAllChild(parentIssue, i)

    except NotImplementedError:
        print("** NotImplementedError ERROR ** ")

print("DONE SANDEEP")

#  EXPORT TO EXCEL

XlWrtr = ExcelWriter("/Users/sandeep/QIReport.xlsx")
manualDf.to_excel(XlWrtr, sheet_name='All Data')
XlWrtr.save()
XlWrtr.close()

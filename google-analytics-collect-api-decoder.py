from datetime import datetime
from sys import exit
from os import mkdir

# Constants regarding dictionaries and their titles.
# Constant for the title key, present in most dictionaries below.
CONST_DIC_TITLE = "title"

# Parameters names
CONST_MAIN_PARAMETERS_TITLE = "Main Parameters"
CONST_OVERRIDE_PARAMETERS_TITLE = "Override Parameters"
CONST_EVENT_PARAMETERS_TITLE = "Events Parameters"
CONST_CAMPAIGN_VARIABLE_PARAMETERS_TITLE = "Campaign Variable Parameters"
CONST_TIMING_PARAMETERS_TITLE = "Timing Parameters"
CONST_ECOMERCE_PARAMETERS_TITLE = "eCommerce Parameters"
CONST_APP_TRACKING_PARAMETERS_TITLE = "App Tracking Parameters"
CONST_OTHER_PARAMETERS_TITLE = "Other Parameters"
CONST_GOOGLE_EXPERIMENTS_PARAMETERS_TITLE = "Google Experiments Parameters"
CONST_SOCIAL_TRACKING_PARAMETERS_TITLE = "Social Tracking Parameters"

# Source for the dictionaries, 
# written at the end of each file for the user to go if they have their doubts.
CONST_DICTIONARY_SOURCE = "https://cheatography.com/dmpg-tom/cheat-sheets/google-universal-analytics-url-collect-parameters/"

# Parameters dictionaries containing the full human readable names of the parameters.
CONST_MAIN_PARAMETERS_DIC = {
    CONST_DIC_TITLE : CONST_MAIN_PARAMETERS_TITLE,
    "a" : "Random number used to link Google Analytics to Adsense (currently not working)",
    "cid" : "Client ID number",
    "de" : "Document Encoding type",
    "dl" : "The Document Location",
    "dt" : "Document Title",
    "fl" : "FLash version",
    "je" : "Java Enabled? (1=yes, 0=no)",
    "ni" : "Non-Interaction hit type (set as true or '1' in code. Shows as 1 or 0 in parameters)",
    "_s" : "hit Sequence - increments each time an event (inc pageview)",
    "sd" : "Screen Depth",
    "sr" : "Screen Resolution",
    "t" : "the Type of tracking call this is (e.g. pageview, event)",
    "tid" : "Tracking ID (your UA number)",
    "_u" : "Verification code generated by GA analytics.js",
    "ul" : "User Language code",
    "_v" : "SDK Version number",
    "v" : "Protocol Version",
    "vp" : "View Port size (browser window visible area)",
    "z" : "cache buster"
}
CONST_OVERRIDE_PARAMETERS_DIC = {
    CONST_DIC_TITLE : CONST_OVERRIDE_PARAMETERS_TITLE,
    "dh" : "Document Host name override",
    "dp" : "Document Path - used when overriding the standard page name",
    "ua" : "User Agent override",
    "uip" : "User IP override",
    "cd" : "sCreen name - mainly used in app tracking",
    "linkid" : "Link ID of a clicked DOM element"
}
CONST_EVENT_PARAMETERS_DIC = {
    CONST_DIC_TITLE : CONST_EVENT_PARAMETERS_TITLE,
    "ea" : "Event Action",
    "ec" : "Event Category",
    "el" : "Event Label",
    "ev" : "Event Value",
}
CONST_CAMPAIGN_VARIABLE_PARAMETERS_DIC = {
    CONST_DIC_TITLE : CONST_CAMPAIGN_VARIABLE_PARAMETERS_TITLE,
    "cn" : "Campaign Name",
    "cs" : "Campaign Source",
    "cm" : "Campaign MediumCampaign Medium",
    "ck" : "Campaign Keyword",
    "cc" : "Campaign Content",
    "ci" : "Campaign Id",
    "glcid" : "Google adwords ID",
    "dclid" : "google Display ads ID"
}
CONST_TIMING_PARAMETERS_DIC = {
    CONST_DIC_TITLE : CONST_TIMING_PARAMETERS_TITLE,
    "utc" : "User Timing Catergory (not universal coordinated time)",
    "utv" : "User Timing Variable name",
    "utt" : "User Timing Time",
    "utl" : "User Timing Label",
    "plt" : "Page Load Time",
    "dns" : "DNS time",
    "pdt" : "Page Download Time",
    "rrt" : "Redirect Response Time",
    "tcp" : "TCP connect time",
    "srt" : "Server Response Time",
    "exd" : "EXception Description",
    "exf" : "is EXception Fatal?",
}
CONST_ECOMERCE_PARAMETERS_DIC = {
    CONST_DIC_TITLE : CONST_ECOMERCE_PARAMETERS_TITLE,
    "cu" : "CUrrency that the transaction takes place in",
    "in" : "Item Name",
    "ic" : "Item Code (sku)",
    "ip" : "Item Price (per unit)",
    "iq" : "Item Quantity",
    "iv" : "Item Variation (normally category)",
    "ta" : "Transaction Affiliation",
    "ti" : "Transaction Identification number",
    "tr" : "Transaction Revenue value",
    "ts" : "Transaction Shipping value",
    "tt" : "Transaction Tax value"
}
CONST_APP_TRACKING_PARAMETERS_DIC = {
    CONST_DIC_TITLE : CONST_APP_TRACKING_PARAMETERS_TITLE,
    "aid" : "Application ID",
    "aiid" : "Application Installer ID",
    "an" : "Application Name",
    "av" : "Application Version",
    "ht" : "HiT sequence number"
}
CONST_OTHER_PARAMETERS_DIC = {
    CONST_DIC_TITLE : CONST_OTHER_PARAMETERS_TITLE,
    "aip" : "Anonymize IP (see note below)",
    "jid" : "JoinID (binding your GA cookie to DoubleClick cookie)",
    "qt" : "Queue Time (for collecting offline data)",
    "sc" : "Session Control",
    "uid" : "User ID (known uid as opposed to cid)"
}
CONST_GOOGLE_EXPERIMENTS_PARAMETERS_DIC = {
    CONST_DIC_TITLE : CONST_GOOGLE_EXPERIMENTS_PARAMETERS_TITLE,
    "xid" : "Experiment ID",
    "xvar" : "Experiment VARiant"
}
CONST_SOCIAL_TRACKING_PARAMETERS_DIC = {
    CONST_DIC_TITLE : CONST_SOCIAL_TRACKING_PARAMETERS_TITLE,
    "sn" : "Social Network",
    "sa" : "Social Action",
    "st" : "Social action Targt (normally a url)"
}

# Dictionary used to associate a parameter or a group of parameters to a description.
CONST_DIC_PARAMS_TO_DESC = {
    "a" : "#",
    "cid": "*",
    "t" : "*",
    "tid" : "*",
    "_u" : "+",
    "v" : "*",
    "aip" : "aip"
}

# Parameters descriptions.
CONST_DIC_PARAM_DESC = {
    "#" : "Equivalent of the classic analytics utmhid parameter",
    "*" : "Must be present on EVERY call to be accepted by GA servers",
    "+" : "See http://stackoverflow.com/questions/26849042/u-parameter-in-universal-google-analytics-collect-hits for full explanation",
    CONST_EVENT_PARAMETERS_TITLE : "You will only see any of these when t (type) = event",
    CONST_CAMPAIGN_VARIABLE_PARAMETERS_TITLE : "To register any campaign variables (c*) you MUST populate Campaign Source AND Campaign Medium as a minimum.",
    CONST_ECOMERCE_PARAMETERS_TITLE : "You will only see these when t (Type) = transaction or item.",
    "aip" : "The value of this parameter can be absolutely anything to cause the IP to be anonymized. This includes a blank value. $aip=, $aip=0, &aip=1 will all cause anonymity."
}

# Output messages for the explainGoogleAnalytics output.
CONST_DIC_STATUS = {
    0: "Success.",
    1: "Failed: The inputed URL is not supported."
}

# Array containing all the dictionaries above.
CONST_API_DIC_ARRAY = [
    CONST_MAIN_PARAMETERS_DIC,
    CONST_OVERRIDE_PARAMETERS_DIC,
    CONST_EVENT_PARAMETERS_DIC,
    CONST_CAMPAIGN_VARIABLE_PARAMETERS_DIC,
    CONST_TIMING_PARAMETERS_DIC,
    CONST_ECOMERCE_PARAMETERS_DIC,
    CONST_APP_TRACKING_PARAMETERS_DIC,
    CONST_OTHER_PARAMETERS_DIC,
    CONST_GOOGLE_EXPERIMENTS_PARAMETERS_DIC,
    CONST_SOCIAL_TRACKING_PARAMETERS_DIC
]



# Global Variables
# Curren date and time, used for the file formats
currentTimeForFileName = ((str(datetime.now()).replace(" ", "_")).replace(":", "-")).replace(".", "_")

# Name of the output file or directory
fileName = "google-analytics-collect-api-" + currentTimeForFileName

# For Debugging:
# Checks if a variable is of a specific type and exits if it isn't.
# Params:
# variable: The variable to evaluate.
# varType: the expected type of the variable, any other variable types may throw error.
#          To be noted that:
#                           Case sensitive.
#                           For ease of use, just input the type
#                               i.e. if the type expected is a list, input "list"
#                                    and not "<class 'list'>".
# methodName: name of the method where the assertion failed, helps for debugging.
def checkVariableByType(variable, varType, methodName):
    if(str(type(variable)) != "<class '"+varType+"'>"):
        exit("System Error: variable in"+methodName+" isn't a"+varType)

# Search logic for looking up the parameters name.
# Given a parameter name in the URL, search for full human readable names in the dictionaries
# Params:
# paramName: name of the parameter in the URL to lookup.
# Return:
# Returns a string that either is the name if found, otherwise return a default message.
def searchParamInDic(paramName):
    for dic in CONST_API_DIC_ARRAY:
        if paramName in dic:
            return dic[paramName]
    return "Unknown Parameter"

# Search logic for looking up a parameter's description
# Given a parameter name in the URL, search for a description for it.
# Params:
# paramName: name of the parameter in the URL to lookup.
# Return:
# Returns a string to be later used to retrieve the description in CONST_DIC_PARAM_DESC.
# If no description is found, return "0"
def getParamDescriptionKey(paramName):
    if paramName in CONST_DIC_PARAMS_TO_DESC:
            return CONST_DIC_PARAMS_TO_DESC[paramName]
    for dic in CONST_API_DIC_ARRAY:
        if paramName in dic:
            if dic[CONST_DIC_TITLE] in CONST_DIC_PARAM_DESC:
                return dic[CONST_DIC_TITLE]
    return "0" 

# URL handling logic
# Given an URL, see if the URL is valid, get the name and description of the parameters
# in the URL, and then write all of it to a file.
# Params:
# requestURL: URL of Google Analytics' Collect's GET API Call alongside its parameters
# Return:
# 0 if succesful, otherwise return any number corresponding to an error message in
# CONST_DIC_STATUS
# Output:
# Outputs a text file (*.txt) with all the URL's parameters' data.
def explainGoogleAnalytics(requestURL):
    requestURL = requestURL.strip()
    requestURLArr = requestURL.split("?")

    if (requestURLArr[0] != "https://www.google-analytics.com/collect"):
        return 1
        # For debug purposes
        # exit("The requested URL is not supported.")

    requestAPIParamArr = requestURLArr[1].split("&")

    # For debug purposes
    # checkVariableByType(requestAPIParamArr, "list", "main")
    sequentialParamArrDesc = []
    paramDescriptionArr = []
    for param in requestAPIParamArr:
        paramName = (param.split("="))[0]
        sequentialParamArrDesc.append(searchParamInDic(paramName))
        paramDescriptionArr.append(getParamDescriptionKey(paramName))

    # For debug purposes
    # if(len(requestAPIParamArr) != len(sequentialParamArrDesc) and len(requestAPIParamArr) != len(paramDescriptionArr) and len(sequentialParamArrDesc) != len(paramDescriptionArr)):
    #     exit("System Error: the list of Parameters did not match the list of Parameters descriptions")

    with open((fileName+".txt"), mode = "w") as f:
        f.write("Request URL Imputted:\n" + requestURL)
        f.write("\n\nParameters Description:\n")
        for i in range(0, len(requestAPIParamArr)):
            f.write("\n")
            f.write(sequentialParamArrDesc[i] + "\n")
            if paramDescriptionArr[i] in CONST_DIC_PARAM_DESC:
                f.write(CONST_DIC_PARAM_DESC[paramDescriptionArr[i]] + "\n")
            f.write(requestAPIParamArr[i] + "\n")
        f.write("\n")
        f.write("\nSource: " + CONST_DICTIONARY_SOURCE)
    f.close()
    return 0

# Main
# Method to run when the file is called from terminal.
# Input:
# Requests an URL, either a file containing a list of URLs, each one delimited by a new line,
# or a single URL
# Output:
# Outputs a status message in the terminal for each URL processed.

if __name__ =="__main__":
    request = input("Please enter the Google Analytics API Call: ")
    try:
        file1 = open(request, 'r')
        lines = file1.readlines()
        file1.close()
        statusArr = []
        ogFn = fileName
        mkdir(ogFn)
        for i in range (0, len(lines)):
            fileName = ogFn + "/"  + "Request_"+ str(i)
            statusArr.append(explainGoogleAnalytics(lines[i]))
        for i in range(0, len(statusArr)):
            print("Line "+str(i)+": "+CONST_DIC_STATUS[statusArr[i]])

    except IOError as err:
        print("File not found, processing directly from terminal:")
        res = explainGoogleAnalytics(request)
        if(res == 1):
            exit(CONST_DIC_STATUS[res])
        print(CONST_DIC_STATUS[res])

# to download data/csv files from the internet
import urllib.request

goog_url = "http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv"

def data_analysis(csv_url):
    response = urllib.request.urlopen(csv_url)      # response opens the data
    csv = response.read()   # reads the data in the url
    csv_str = str(csv)      #   converts all the data into string
    lines = csv_str.split("\\n")    # \\n splits the whole string into different lines accordingly
        # of course we dont want all the string in the url in one whole line
    destination = r'goog.csv'   #destination of the file
    fx = open(destination, "w")      #to open up the file

    for line in lines:    # to write in the file
        fx.write(line + "\n")

    fx.close()

data_analysis(goog_url)


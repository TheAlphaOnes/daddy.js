import requests , bs4

def get_html(URL):
    data = requests.get(URL)
    if data.status_code == 200:
        doc = data.text
        return doc
    else:
        if data.status_code == 200:
            doc = data.text
            return doc
        else: 300

def get_data(data,doc):
    resp = []
    doc = bs4.BeautifulSoup(doc , "html.parser")
    for i in data.keys():
        req_text = doc.find(id=i).text
        resp.append([data.get(i),req_text])
    return resp

def daddy_api(url,data):
    html = get_html(url)
    if 300 == html:
        return 300
    else:
        repr = get_data(data,html)
        return repr

# data = {"12a":"gg1","12b":"gg2"}



# gg = daddy_api("https://daddyjstest.netlify.app",data)
# print(gg)
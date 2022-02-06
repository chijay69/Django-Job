#imports
import json
import http.client
import requests
import psycopg2
import sys



start = '''[
'''
stop = '''
]'''
comma = ','

#logic goes here
def get_item_id(value):
        return f"/v0/item/{value}.json?print=pretty"

    
def get_item(url, connect, payload_dict):
    """
    args:
    url(str): url retrieved from id passed to get_item_id
    returns:
    dataArray(str)
    """
    conn = connect
    payload = payload_dict
    print("\n")
    conn.request("GET", url, payload)
    res = conn.getresponse()
    data = res.read()
    dataArray = data.decode("utf-8")
    return dataArray

                                    
#connection made here

def get_data_json():
    
    #connect to site
    conn = http.client.HTTPSConnection("hacker-news.firebaseio.com")
    payload = "{}"
    
    #request starts here
    # get newstories
    print("Get new stories id")
    conn.request("GET", "/v0/newstories.json?print=pretty", payload)
    res = conn.getresponse()
    data = res.read()
    #print(data)

    dataArray = data.decode("utf-8")

    #print(type(data),type(dataArray))
    data_list = (dataArray.replace('[','').replace(']','').replace('\n','').split(',')) #remove [ ] and \n from the string and convert it to a list

    data_list = [c.lstrip().rstrip() for c in data_list] #strip of preceeding and succeeding whitespaces

    print("\ndata_list after cleaning:")
    data_list = data_list[len(data_list) - 100:len(data_list)] #100 new stories

    print(len(data_list))


    #write json file
    with open("data.json", "w") as outfile:
        for i in range(len(data_list)):
            id_ = get_item_id(data_list[i])
            content = get_item(id_, conn, payload)
            content_dict = json.loads(content)
            outfile.write(start)
            if i != len(data_list):
                outfile.write(comma)
            outfile.write(stop)

                                                                                    
    

    





#extract kids and time columns
#NB: kids_list is already having all int members
#kids_list = content_dict['kids']
#print('kids:',kids_list)
#time = content_dict['time']
#print('time:',time)


#def do_insert(rec: dict):
#    cols = rec.keys()
#    cols_str = ','.join(cols)
#    vals = [ rec[k] for k in cols ]
#    vals_str = ','.join( ['%s' for i in range(len(vals))] )
#    sql_str = """INSERT INTO hack_basemodel ({}) VALUES ({})""".format(cols_str, vals_str)
#    cur.execute(sql_str, vals)

#writing commands

            
#write csv file
#a_file = open("data.csv", "w") #open csv file
#writer = csv.writer(a_file) #create writer obj
#for i in range(len(data_list)):
#    id_ = get_item_id(data_list[i])
#    content = get_item(id_)
#    content_dict = json.loads(content)
#    print(content_dict)
#    for key, value in content_dict.items():
#        writer.writerow([key, value])
#        #close csv file
#        a_file.close()
        
        
#read csv into pandas
#df=pd.read_csv('data.csv', headers = ['by', 'descendants', 'id', 'score', 'time', 'title','type', 'url'],)
#pd.set_option('display.max_rows', None)
#print(df.head())


def do_insert(rec: dict):
    cols = rec.keys()
    cols_str = ','.join(cols)
    vals = [ rec[k] for k in cols ]
    vals_str = ','.join( ['%s' for i in range(len(vals))] )
    sql_str = """INSERT INTO hack_basemodel ({}) VALUES ({})""".format(cols_str, vals_str)
    cur.execute(sql_str, vals)
    con.commit()

                                                                                        

def read_json_to_db():
    #read json file
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    #connect to database
    con = psycopg2.connect("dbname=jobdb user=u0_a292 password = ngoziKAMA")
    cur = con.cursor()
    for dat in data:
        print(dat)
        print("inserting to db")
        do_insert(dat)


                                                                                                        
    

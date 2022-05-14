from neo4j import GraphDatabase, basic_auth
import datas as dt
import country as ct
import stocks as st
URL = 'neo4j://localhost:7687'
USER = 'neo4j'
PASSWORD = '1234'

type_list = {dt.Data:'Data', ct.Country:'Country', st.Stock:'Stock'}

def make_properties(dic):
    pro_str = '{'
    for key, value in dic.items():
        str_value = str(value).replace("'",'')
        pro_str += str(key) +':'+ "'" +str_value + "'" +','
    pro_str = pro_str[:-1]
    pro_str += '}'
    return pro_str

def make_graph(data_dict):
    driver = GraphDatabase.driver(URL, auth=basic_auth(USER, PASSWORD))
    sess = driver.session()
    for key, value in data_dict.items():
        info = value.__dict__
        if 'effecting' in info:
            info.pop('effecting')
        if 'effected' in info:
            info.pop('effected')

        query = 'CREATE ' + '(:' + type_list[value.__class__] + make_properties(info) + ')'
        print(query)
        sess.run(query)

def make_country_relation(country_dict):
    driver = GraphDatabase.driver(URL, auth=basic_auth(USER, PASSWORD))
    sess = driver.session()
    for key, value in country_dict.items():
        export_dict = value.export_item

        for export_item, ratio in export_dict.items():
            if export_item in dt.data_dict:
                query = "MATCH (c:Country), (d:Data) WHERE c.name = \"{}\" and d.name = \"{}\" "\
                        "CREATE (c)-[e:Export]->(d) RETURN type(e)".format(value.name, export_item)
                print(query)
                sess.run(query)
            else:
                print(export_item + " doesnt exist in data")

if __name__ == '__main__':
    make_graph(dt.data_dict)
    make_graph(ct.country_dict)
    make_country_relation(ct.country_dict)







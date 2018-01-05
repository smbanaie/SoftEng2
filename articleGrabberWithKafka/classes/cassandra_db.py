__author__ = 'Javad'

from cassandra.cluster import Cluster


class Article(Cluster):
    def __init__(self,data=None):
        super(Article, self).__init__()
        cluster = Cluster()
        self.session = cluster.connect('article')
        self.data = data

    def insert_data(self):
        result = self.session.execute("""
            insert into articledb (author, caption, publishyear, publishlocation, code,language,size,summery,keyword)
             values ('{author}', '{caption}', '{publishyear}','{publishlocation}', '{code}', '{language}','{size}','{summery}','{keyword}')
        """.format(author=self.data['author'], caption=self.data['caption'], publishyear=self.data['publishyear'],publishlocation=self.data['publishlocation'],
                   code=self.data['code']
                   , language=self.data['language'], size=self.data['size'], summery=self.data['summery'],
                   keyword=self.data['keyword']))
        print result



    def select_data(self, select):
        list_result = []
        result = self.session.execute("select * from articledb where keyword='{keyword}'".format(keyword=select))
        for item in result:
            list_result.append(item)
        return list_result



class Keyword(Cluster):
    def __init__(self, data=None):
        super(Keyword, self).__init__()
        cluster = Cluster()
        self.session = cluster.connect('article')
        self.data = data

    def insert(self):
        result = self.session.execute("""
            insert into keyworddb (author, caption, publishyear, publishlocation, code,language,size,summery,keyword)
             values ('{author}', '{caption}', '{publishyear}','{publishlocation}', '{code}', '{language}','{size}','{summery}','{keyword}')
        """.format(author=self.data['author'], caption=self.data['caption'], publishyear=self.data['publishyear'],publishlocation=self.data['publishlocation'],
                   code=self.data['code']
                   , language=self.data['language'], size=self.data['size'], summery=self.data['summery'],
                   keyword=self.data['keyword']))
        print result

    def select(self, select):
        list_result = []
        result = self.session.execute("select * from keyworddb where keyword='{keyword}'".format(keyword=select))
        for item in result:
            list_result.append(item)
        return list_result

class Keywordyear(Cluster):
    def __init__(self,data=None):
        super(Keywordyear, self).__init__()
        cluster = Cluster()
        self.session = cluster.connect('article')
        self.data=data

    def insert(self):
        result = self.session.execute("""
            insert into  keyword_yeardb(author, caption, publishyear, publishlocation, code,language,size,summery,keyword)
             values ('{author}', '{caption}', '{publishyear}','{publishlocation}', '{code}', '{language}','{size}','{summery}','{keyword}')
        """.format(author=self.data['author'], caption=self.data['caption'], publishyear=self.data['publishyear'],publishlocation=self.data['publishlocation'],
                   code=self.data['code']
                   , language=self.data['language'], size=self.data['size'], summery=self.data['summery'],
                   keyword=self.data['keyword']))
        print result

    def select(self,keyword,publishyear):
        list_result = []
        result = self.session.execute("select * from keyword_yeardb where keyword='{keyword}',publishyear='{publishyear}'".format(keyword=keyword,publishyear=publishyear))
        for item in result:
            list_result.append(item)
        return list_result


class year(Cluster):
    def __init__(self,data=None):
        super(year, self).__init__()
        cluster = Cluster()
        self.session = cluster.connect('article')
        self.data = data

    def insert(self):
        result = self.session.execute("""
            insert into  yeardb(author, caption, publishyear, publishlocation, code,language,size,summery,keyword)
             values ('{author}', '{caption}', '{publishyear}','{publishlocation}', '{code}', '{language}','{size}','{summery}','{keyword}')
        """.format(author=self.data['author'], caption=self.data['caption'], publishyear=self.data['publishyear'],
                   publishlocation=self.data['publishlocation'],
                   code=self.data['code']
                   , language=self.data['language'], size=self.data['size'], summery=self.data['summery'],
                   keyword=self.data['keyword']))
        print result

    def select(self,publishyear):
        list_result = []
        result = self.session.execute("select * from keyworddb where publishyear='{publishyear}'".format(publishyear=publishyear))
        for item in result:
            list_result.append(item)
        return list_result

#!usr/bib/env python
# -*- encoding UTF-8 -*-

from HTMLParser import HTMLParser


class ConferencesPage(HTMLParser):
    """
        This class is for parsing conference html page
        __init__()
            self.conferences_links : The most important field that is list of all conference links
        handle_start():
            tag :parameter  start tag
            attrs :parameter E.g attrs: '[('href', 'http....'),('class','ex..'), ]
    """

    def __init__(self):
        HTMLParser.__init__(self)
        self.conferences_links = []
        self.find_h4 = False
        self.find_h4_a = False

    def handle_starttag(self, tag, attrs):
        if tag == 'h4':
            self.find_h4 = True
            self.find_h4_a = False
        elif tag == 'a' and self.find_h4:
            self.find_h4_a = True
            self.find_h4 = False
            # append value of href attribute to conferences_links list
            self.conferences_links.append(attrs[0][1])
        else:
            self.find_h4 = False
            self.find_h4_a = False

    def handle_endtag(self, tag):
        if self.find_h4_a:
            self.find_h4 = False
            self.find_h4_a = False

    def handle_data(self, data):
        if self.find_h4_a:
            self.find_h4 = False
            self.find_h4_a = False

    def error(self, message):
        pass

    def get_conferences_links(self):
        return self.conferences_links


class ArticlesPage(HTMLParser):
    """
        This class return list of articles links
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.find_div_class_item = False
        self.find_div_class_item_a = False
        self.links = []

    def handle_starttag(self, tag, attrs):
        try:
            if attrs[0][1] == 'item':
                self.find_div_class_item = True
                self.find_div_class_item_a = False
            if self.find_div_class_item:
                try:
                    if tag == 'a':
                        self.find_div_class_item_a = True
                        self.find_div_class_item = False
                        self.links.extend([atr_val for atr_name, atr_val in attrs if atr_name == 'href'])
                except IndexError:
                    pass
            else:
                self.find_div_class_item = False
                self.find_div_class_item_a = False
        except IndexError:
            pass

    def handle_endtag(self, tag):
        if self.find_div_class_item_a:
            self.find_div_class_item = False
            self.find_div_class_item_a = False

    def handle_data(self, data):
        if self.find_div_class_item_a:
            self.find_div_class_item = False
            self.find_div_class_item_a = False

    def get_articles_link(self):
        return self.links

    def error(self, message):
        pass


class ArticleIndex(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.info = {}
        self.find_h1 = False
        self.counter = 1
        self.find_div_class_info_j = True
        self.atr = None
        self.info['author'] = []
        self.f = 0
        self.find_pyblisher_one = 1
        self.find_div_class_info_j_b = False
        self.find_div_class_info_j_b_a = False
        self.find_class_table = False
        self.c = 0
        self.c2 = 0

    def handle_starttag(self, tag, attrs):
        if self.find_div_class_info_j_b_a and tag == 'h3':
            self.find_pyblisher_one = 0
            self.find_div_class_info_j_b_a = False
            self.find_div_class_info_j = False
            self.find_div_class_info_j_b = False
            del self.info['author'][-1]
            del self.info['author'][0]

        if tag == 'h1':
            self.find_h1 = True
        else:
            try:
                if tag == 'div' and 'info j' == attrs[0][1]:
                    self.find_div_class_info_j = True
                    self.f = 1

                if self.find_div_class_info_j and tag == 'b':
                    self.find_div_class_info_j_b = True
                    self.find_div_class_info_j_b_a = False
                    self.find_div_class_info_j = False

                if self.find_div_class_info_j_b and tag == 'a':
                    self.find_div_class_info_j_b_a = True
                    self.find_div_class_info_j = False
                    self.find_div_class_info_j_b = False

                if self.find_div_class_info_j_b_a and tag == 'b':
                    self.find_div_class_info_j_b_a = False
                    self.find_div_class_info_j = False
                    self.find_div_class_info_j_b = True

                if attrs[0][1] == 'table':
                    self.find_class_table = True
                    self.atr = attrs[0][1]

            except IndexError:
                pass

    def handle_endtag(self, tag):
        if self.find_div_class_info_j_b_a and tag == 'div':
            self.find_div_class_info_j = False
            self.find_div_class_info_j_b_a = False
            self.find_div_class_info_j_b = False

    def handle_data(self, data):
        data = data.strip()
        if self.find_h1 is True:
            self.info['caption'] = data
            self.find_h1 = False
        if self.find_class_table:
            self.counter += 1
            if self.counter == 4:
                self.info['publish_year'] = data
            if self.counter == 8:
                self.info['publish_location'] = data
            if self.counter == 11:
                self.info['code'] = data
            if self.counter == 14:
                self.info['language'] = data
            if self.counter == 17:
                self.info['size'] = data

        if self.find_div_class_info_j_b_a:
            self.c += 1
            if self.c % 3 == 1 and self.find_pyblisher_one:
                self.info['author'].append(data.decode('UTF-8'))

        if self.f == 1:
            self.c2 += 1
            if self.c2 == 15:
                self.info['summery'] = data
            if self.c2 == 17:
                self.info['key_word'] = data.split('\xd8\x8c')[-1].split('.')[0]

    def get_information(self):
        return self.info

    def error(self, message):
        pass


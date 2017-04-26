from setting import Settings
import urllib



def main():
    url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
    data = urllib.urlopen(url).read()
    print data


if __name__ == '__main__':
    main()
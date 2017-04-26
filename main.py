from setting import Settings
import urllib

settingPath = './setting.txt'


def main():
    settings = Settings(settingPath)
    url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
    data = urllib.urlopen(url).read()
    print data


if __name__ == '__main__':
    main()
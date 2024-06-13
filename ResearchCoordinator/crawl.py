from icrawler.builtin import BingImageCrawler, GoogleImageCrawler

bing_crawler = BingImageCrawler(
    feeder_threads=1,
    parser_threads=2,
    downloader_threads=7,
    storage={'root_dir': 'Celebrity(US)_Male1'})

filters = dict(
    type = 'photo',
    size='small',
    color='orange',
    license='noncommercial,modify',
    people = 'portrait',
    layout = 'square',
    date = 'pastweek'
)

bing_crawler.crawl(keyword= 'Andrew Garfield', 
                max_num= 110, 
                offset=0)


# google_crawler = GoogleImageCrawler(
#     feeder_threads=1,
#     parser_threads=2,
#     downloader_threads=4,
#     storage={'root_dir': 'Caucasian(US)_Male1'})
# filters = dict(
#     size='large',
#     color='orange',
#     license='noncommercial,modify',
#     date=((2016, 1, 1), (2017, 1, 1))
#     )

# google_crawler.crawl(keyword='Man Face Portrait', filters=filters, max_num=120, file_idx_offset=0)


#if u have dataset of the celebrity or dataset of people use this code
#--------------------------------------------------------------#
# import pandas as pd
# from icrawler.builtin import GoogleImageCrawler
# from icrawler.builtin import BingImageCrawler
# from pathlib import Path

# mitFilter=True
# #Set the filter to creative vommons license and set if th eimage is either photo, face, clipart, linedrawing, or animated
# filters = dict(
#     type='photo',
#     license='noncommercial,modify',)

# howmany= 10
# names=pd.read_csv('Top 1000 Actors and Actresses.csv', encoding = "ISO-8859-1")

# subset=names.Name

# for keyword in subset:
#     crawler = BingImageCrawler(
#         parser_threads=5,
#         downloader_threads=5,
#         storage={'root_dir': 'Celebs/{}'.format(keyword)}
#     )    
#     if mitFilter==True:
#         crawler.crawl(keyword=keyword, filters=filters, max_num=howmany, min_size=(500, 500))
#     else:
#         crawler.crawl(keyword=keyword, max_num=howmany, min_size=(500, 500))


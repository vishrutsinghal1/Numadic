## Coding challenge for Data Engineer role at ISentia. ##

### Purpose ###
Create a solution that crawls for articles from a news website, cleanses the response, stores in a mongo database then makes it available to search via an API.
### Solution ###
* Scrapy framework based crawler which traverses page links recursively and uses xpath to fetch article details and text, then stores to external MongoDB server 
* Flask based REST API using MongoDB text search to get the list of documets containing a keyword
### Installation ###
* Ensure Python 3.x is installed: `python -V`
* Install required libraries: `pip install -r REQUIREMENTS.txt`
### Usage ###
Web crawler can accept either one url or a file containing line-separated urls as a command line parameter

For one url please use: `scrapy crawl news -a url={your_url}`

For a file please use: `scrapy crawl news -a filename={your_url_list_file}`

API is running on 0.0.0.0:5000

API search function is available at /getnews/:keyword, method=GET

For example: <http://127.0.0.1:5000/getnews/Trump>
### TODOs and Improvement suggestions ###
- [ ] MongoDB -> Elasticsearch for better keyword lookup and ranking
- [ ] Add config (ini or json) per each site being crawled
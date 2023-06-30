## update_blogPost.py
import feedparser

blog_url = "https://syeon2.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

preREADME = """
#### 책을 좋아하는 개발자📚
"기술에 대한 호기심을 가지고 꾸준히 성장하는 개발자"

###### Skills
<img src="https://img.shields.io/badge/java-c74634?style=flat-square&logo=oracle&logoColor=white"> <img src="https://img.shields.io/badge/spring-6DB33F?style=flat-square&logo=spring&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=flat-square&logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/redis-DC382D?style=flat-square&logo=mysql&logoColor=white">

<a href="https://github.com/syeon2"><img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white"></a> <a href="https://fascinated-beechnut-581.notion.site/Daebi-s-Devlog-f2c82ac119d44e9eb5a46988b0882c13"><img src="https://img.shields.io/badge/notion-181717?style=flat-square&logo=Notion&logoColor=white" /></a> <img src="https://img.shields.io/badge/slack-6441A5?style=flat-square&logo=Slack&logoColor=white" />

------
#### 💁🏻‍♂️ Latest Blog Post

"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)

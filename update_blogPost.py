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
"지식의 확장과 성장을 즐기며 이를 활용해 문제 해결과 성취감을 찾는 개발자입니다."

###### Skills
<img src="https://img.shields.io/badge/java-c74634?style=flat-square&logo=oracle&logoColor=white"> <img src="https://img.shields.io/badge/spring-6DB33F?style=flat-square&logo=spring&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=flat-square&logo=mysql&logoColor=white">

<a href="https://github.com/syeon2"><img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white"></a> <a href="https://fascinated-beechnut-581.notion.site/Daebi-s-Devlog-f2c82ac119d44e9eb5a46988b0882c13"><img src="https://img.shields.io/badge/notion-181717?style=flat-square&logo=Notion&logoColor=white" /></a> <img src="https://img.shields.io/badge/slack-6441A5?style=flat-square&logo=Slack&logoColor=white" />

###### Blog
<a href="https://syeon2.github.io/" target="_blank">
  <img src="https://img.shields.io/badge/Devlog-000000?style=flat-square&logo=Bitdefender&logoColor=white"/></a>
</a>


--------------------

[![Baekjoon Algorithm](http://mazassumnida.wtf/api/v2/generate_badge?boj=waterkite)](https://solved.ac/waterkite/)

------
#### 💁🏻‍♂️ Latest Blog Post
<br />
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)

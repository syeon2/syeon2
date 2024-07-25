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
### 책을 좋아하는 개발자📚
"기술에 대한 호기심을 가지고 꾸준히 성장합니다."

###### Skills
<img src="https://img.shields.io/badge/java-c74634?style=flat-square&logo=oracle&logoColor=white"> <img src="https://img.shields.io/badge/spring-6DB33F?style=flat-square&logo=spring&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=flat-square&logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/redis-DC382D?style=flat-square&logo=redis&logoColor=white">

<br />

#### 💁🏻‍♂️ Latest Blog Post

"""

nextREADME = """

<br />

--------

<br />

<a href="https://github.com/syeon2">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=syeon2&layout=donut&show_icons=true&theme=material-palenight&hide_border=true&bg_color=20232a&icon_color=58A6FF&text_color=fff&title_color=58A6FF&count_private=true&exclude_repo=Face-Transfer-Application" width=38% />
</a>    
<a href="https://github.com/syeon2">
  <img src="https://github-readme-stats.vercel.app/api?username=syeon2&show_icons=true&theme=material-palenight&hide_border=true&bg_color=20232a&icon_color=58A6FF&text_color=fff&title_color=58A6FF&count_private=true" width=56% />
</a>
<a href="https://github.com/syeon2">
    <img src="https://github-readme-activity-graph.vercel.app/graph?username=syeon2&theme=react-dark&bg_color=20232a&hide_border=true&line=58A6FF&color=58A6FF" width=94%/>
</a>
"""

resultREADME = f"{preREADME}{latest_posts}{nextREADME}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)

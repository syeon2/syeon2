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
### 덕업일치(悳業一致)의 삶을 꿈꾸는 개발자🧑🏻‍💻

'기술의 근간을 탐구하고 엔지니어링적으로 적용할 수 있는 개발자'라는 모토를 가지고 있습니다.

기술에 대한 호기심을 바탕으로 꾸준히 성장하며, 실용적인 가치를 창출하고 지속 가능한 솔루션을 개발하는 데 주력합니다.


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

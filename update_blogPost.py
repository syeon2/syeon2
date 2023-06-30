## update_blogPost.py
import feedparser

blog_url = "https://teawon.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

preREADME = """
## 기존의 README.md 내용
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)

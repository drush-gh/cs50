import re

#iframe = input("HTML: ")

link1 = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

link2 = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'

link3 = '<iframe width="560" height="315" src="https://www.youtube.com/embed/aoag03mSuXQ?si=uzCB2xg1jjnQ-xOk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'

pattern1 = r"(src=\"https?://(?:www)?\.youtube\.com/embed/.*)(title.?)"

pattern2 = r"(src=\"https?://(?:www)?\.youtube\.com/embed/.*)(></iframe)"


pattern1link1 = re.search(pattern1, link1)

pattern2link1 = re.search(pattern2, link1)

pattern1link2 = re.search(pattern1, link2)

pattern2link2 = re.search(pattern2, link2)

pattern1link3 = re.search(pattern1, link3)

pattern2link3 = re.search(pattern2, link2)

print()
print(f"This is pattern1 with link1: {pattern1link1.groups()}")
print()
print(f"This is pattern2 with link2: {pattern2link1.groups()}")
print()
print(f"This is pattern1 with link2: {pattern1link2.groups()}")
print()
print(f"This is pattern2 with link1: {pattern2link2.groups()}")
print()
print(f"This is pattern1 with link3: {pattern1link3.groups()}")
print()
print(f"This is pattern2 with random link: {pattern2link3.groups()}")

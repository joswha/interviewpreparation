import re

# taken from paiv's solution
def parse(markdown):
    s = markdown
    s = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>', s)
    s = re.sub(r'_([^\n]+?)_', r'<em>\1</em>', s)
    s = re.sub(r'^\* (.*?$)', r'<li>\1</li>', s, flags=re.M)
    s = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', s, flags=re.S)
    for i in range(6, 0, -1):
        s = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), s, flags=re.M)
    s = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', s, flags=re.M)
    s = re.sub(r'\n', '', s)
    return s

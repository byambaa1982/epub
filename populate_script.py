import os
import glob
from bs4 import BeautifulSoup
from bs4 import Comment

# Define the Google Tag Manager script as a string
gtm_script_line = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-6R7KD1FNMR"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-6R7KD1FNMR');
</script>
"""

# Iterate over all .html files in the _build directory and subdirectories
for filepath in glob.glob('_build/**/*.html', recursive=True):
    # Open, parse and modify the file
    with open(filepath, 'r+', encoding='utf8') as f:
        soup = BeautifulSoup(f, 'lxml')

        # If head tag doesn't exist, create it
        if soup.head is None:
            head = soup.new_tag('head')
            soup.html.append(head)
        else:
            head = soup.head

        # Insert the second line of the Google Tag Manager script into the head tag
        head.insert(0, BeautifulSoup(gtm_script_line, 'html.parser'))

        # Overwrite the file with the modified contents
        f.seek(0)
        f.write(str(soup))
        f.truncate()
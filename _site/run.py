import os

print('Preview your local Jekyll site in your web browser at http://localhost:4000.')
os.system('bundle update')
os.system('bundle exec jekyll serve')
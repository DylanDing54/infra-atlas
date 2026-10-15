"""Build the GitHub-hosted catalogue from its English data snapshot."""
import json,re
from pathlib import Path
B=Path(__file__).resolve().parents[1]
data=json.loads((B/'data/library.json').read_text())
s=(B/'source/template.html').read_text()
s=s.replace('Local library · Available offline',f"Research library · {len(data['papers']):,} papers")
s=s.replace('Sources: local PDFs and metadata','Sources: papers and proceedings')
s=s.replace('Original PDFs remain in place','Links to original publications')
s=s.replace('paper-library/papers.en.json','data/papers.json').replace('paper-library/README.en.md','README.md').replace('paper-library/classification-audit.md','source/classification-audit.md')
s=s.replace('paper-library/architecture-audit.md','source/architecture-audit.md')
s=s.replace('The HTML works offline; keep its location relative to the Paper folder unchanged.','Paper links open the original publication. Items without a verified publication URL provide a title search. Full-text PDFs are not hosted here.')
expr="${encodeURI(p.file).replace(/#/g,'%23').replace(/\\?/g,'%3F').replace(/'/g,'%27')}"
assert s.count(expr) in (2,3), 'The local-link template changed; review publication links.'
s=s.replace(expr,'${esc(paperLink(p))}')
s=s.replace('${esc(paperLink(p))}#page=${a.page}', '${esc(paperLink(p))}')
s=s.replace('>PDF page ${a.page} ↗</a>', '>Source (evidence on PDF page ${a.page}) ↗</a>')
s=s.replace('>Read PDF ↗</a>','>${p.url?\'Open paper ↗\':\'Find paper ↗\'}</a>')
s=s.replace('function card(p)',"function paperLink(p){return /^https?:\\/\\//.test(p.url)?p.url:'https://scholar.google.com/scholar?q='+encodeURIComponent(p.title)}\nfunction card(p)")
# The main title and footer now open the source; avoid duplicate source links.
s=s.replace("${/^https?:\\/\\//.test(p.url)?`<a href=\"${esc(p.url)}\" target=\"_blank\" rel=\"noopener\">Source ↗</a>`:''}",'')
payload=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
assert s.count('__DATA__')==1
assert 'encodeURI(p.file)' not in s
assert 'paper-library/' not in s
(B/'index.html').write_text(s.replace('__DATA__',payload))
(B/'data/papers.json').write_text(json.dumps(data['papers'],ensure_ascii=False,indent=2))
print('Built',B/'index.html')

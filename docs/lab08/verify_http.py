import json
import urllib.request
import urllib.error
from pathlib import Path

BASE = 'http://127.0.0.1:8008'
records = []
def request(label, method, path, data=None, expected=200, html=False):
    headers = {'Accept': 'text/html' if html else 'application/json'}
    raw = None
    if data is not None:
        raw = json.dumps(data).encode()
        headers['Content-Type'] = 'application/json'
    req = urllib.request.Request(BASE + path, data=raw, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            status, body = response.status, response.read().decode()
    except urllib.error.HTTPError as error:
        status, body = error.code, error.read().decode()
    parsed = {'html_received': 'rest_framework' in body or 'api' in body.lower()} if html else (json.loads(body) if body else None)
    records.append({'case': label, 'method': method, 'url': path, 'request': data, 'status': status, 'expected': expected, 'response': parsed})
    print(f'{label}: {method} {path} -> {status} (expected {expected})')
    assert status == expected, body[:500]
    return parsed

request('Browsable API root', 'GET', '/api/', html=True)
e = request('Create exam', 'POST', '/api/exams/', {'title': 'LAB08 HTTP temporary', 'description': 'External HTTP verification'}, 201)
eid = e['id']
request('List exams', 'GET', '/api/exams/')
request('Exam detail', 'GET', f'/api/exams/{eid}/')
request('Update exam', 'PATCH', f'/api/exams/{eid}/', {'description': 'Updated by HTTP client'})
payload = {'exam': eid, 'text': 'What is Django?', 'score': 2, 'choices': [{'text': 'Web framework', 'is_correct': True}, {'text': 'Database', 'is_correct': False}]}
q = request('Create question', 'POST', '/api/questions/', payload, 201)
qid=q['id']
request('List questions', 'GET', '/api/questions/')
request('Question detail', 'GET', f'/api/questions/{qid}/')
request('Update question', 'PATCH', f'/api/questions/{qid}/', {'score': 3})
c = request('Create choice', 'POST', '/api/choices/', {'question': qid, 'text': 'Extra wrong option', 'is_correct': False}, 201)
cid = c['id']
request('List choices', 'GET', '/api/choices/')
request('Choice detail', 'GET', f'/api/choices/{cid}/')
request('Update choice', 'PATCH', f'/api/choices/{cid}/', {'text': 'Updated wrong option'})
request('Delete choice', 'DELETE', f'/api/choices/{cid}/', expected=204)
request('Missing required field', 'POST', '/api/exams/', {}, 400)
request('Incorrect field type', 'POST', '/api/questions/', {**payload, 'score': 'abc'}, 400)
request('Zero correct choices', 'POST', '/api/questions/', {**payload, 'choices': [{'text': 'Wrong', 'is_correct': False}]}, 400)
request('Two correct choices', 'POST', '/api/questions/', {**payload, 'choices': [{'text': 'A', 'is_correct': True}, {'text': 'B', 'is_correct': True}]}, 400)
request('Protect correct choice', 'DELETE', f"/api/choices/{q['choices'][0]['id']}/", expected=400)
for number in range(6):
    request(f'Pagination fixture {number+1}', 'POST', '/api/questions/', {**payload, 'text': f'Python pagination {number+1}'}, 201)
filtered = request('Filter by exam', 'GET', f'/api/questions/?exam={eid}')
assert filtered['count'] == 7 and len(filtered['results']) == 5 and filtered['next']
searched=request('Search question text', 'GET', f'/api/questions/?exam={eid}&search=Python')
assert searched['count']==6
page=request('Second page', 'GET', f'/api/questions/?exam={eid}&page=2')
assert len(page['results'])==2
request('Browsable questions', 'GET', '/api/questions/', html=True)
request('Delete question', 'DELETE', f'/api/questions/{qid}/', expected=204)
request('Deleted question', 'GET', f'/api/questions/{qid}/', expected=404)
request('Delete exam and temporary data', 'DELETE', f'/api/exams/{eid}/', expected=204)
Path(__file__).with_name('http-results.json').write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'PASS: {len(records)} HTTP checks. Temporary exam removed.')

from bottle import route, run, template
import os 


@route('/')
def index():
    name = 'APT Spring 2015'
    participants = [
       'German Ilyin',
    ]
    return template("""
    <h1>HW2 for {{course}}</h1>
    Participants list:
    <ul>
      % for item in lst:
      <li>{{ item }}</li>
      % end
    </ul>
    """, course=name, lst=participants)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

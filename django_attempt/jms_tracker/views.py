from django.http import HttpResponse
from datetime import datetime


def index(request):
    return HttpResponse(f"""<p>Hello, world. You're on the jms_tracker homepage (╯°□°）╯︵ ┻━┻</p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/mLRbZJS5A_E" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br> <br>

    Oh damn, look, it's today's date! {datetime.now()}
    """)
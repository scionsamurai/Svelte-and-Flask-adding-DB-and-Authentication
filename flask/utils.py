from flask import request, url_for, redirect
from urllib.parse import urlparse, urljoin
from flask_login import current_user


def check_user():
    if current_user.__dict__ == {}:
        return 'anon'
    else:
        return current_user.__dict__ 
    
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

def redirect_back(endpoint, **values):
    target = request.form['next'] if request.form and 'next' in request.form else request.args.get('next')
    if not target or not is_safe_url(target):
        target = url_for(endpoint, **values)
    return redirect(target)
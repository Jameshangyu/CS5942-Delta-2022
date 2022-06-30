import urllib
from urllib.parse import urljoin, urlparse
from behave import given, when, then, model
from django.conf import settings
from django.shortcuts import resolve_url
from selenium.webdriver.common.by import By

@given(u'I navigate to the index page')
def step_impl(context):
    base_url = urllib.request.url2pathname(context.test_case.live_server_url)
    open_url = urljoin(base_url,'')
    context.browser.get(open_url)
    assert '' in context.browser.page_source

@when(u'The page opens')
def click(context):
    base_url = urllib.request.url2pathname(context.test_case.live_server_url)
    open_url = urljoin(base_url,'')
    context.browser.get(open_url)
    assert '' in context.browser.page_source
    
@then(u'I should see the details for the form')
def details(context):
    print(context.browser.page_source)
    print(context.browser.page_source)
    assert 'Scan A Panel Into A Variogram' in context.browser.page_source



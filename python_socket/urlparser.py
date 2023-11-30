from urllib.parse import urlparse

# url = 'https://example.com/employees/name/?salary>=25000'
# parser_url = urlparse(url)
# print(type(parser_url))
# print(f"scheme: {parser_url.scheme}")
# print(f"netloc: {parser_url.netloc}")
# print(f"path : {parser_url.path}")
# print(f"params : {parser_url.params}")
# print(f"query string: {parser_url.query}")
# print(f"fragemet: {parser_url.fragment}")

url ="https://www.tutorialspoint.com/python/python_url_processing.htm"
parse_url = urlparse(url)
print(f"scheme: {parse_url.scheme}")
print(f"netloc : {parse_url.netloc}")
print(f"path : {parse_url.path}")
print(f"params : {parse_url.params}")
print(f"query: {parse_url.query}")
print(f"fragment : {parse_url.fragment}")
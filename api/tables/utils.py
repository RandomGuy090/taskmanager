
def get_table_url(path):
    "gets tbl_id from /api/tables/tbl_id/users"
    url = path
    if url.endswith("/"):
        url=url[:-1]
    url = url.split("/")
    url = url[url.index(url[-1])-1]
    return url
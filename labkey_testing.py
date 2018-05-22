#!/anaconda3/bin/python3

from labkey.utils import create_server_context
from labkey.query import select_rows

print("Create a server context")
labkey_server = 'warp.hivresearch.org'
project_name = 'Humoral%20Section'  # Project folder name
contextPath = 'query'
schema = 'core'
table = 'Users'

server_context = create_server_context(labkey_server, project_name, contextPath, use_ssl=True)

result = select_rows(server_context, schema, table)
if result is not None:
    print(result['rows'][0])
    print("select_rows: Number of rows returned: " + str(result['rowCount']))
else:
    print('select_rows: Failed to load results from ' + schema + '.' + table)
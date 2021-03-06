import os
basedir = os.path.abspath(os.path.dirname(__file__))

# BASIC APP CONFIG
WTF_CSRF_ENABLED = True
SECRET_KEY = 'supersecret'
BIND_ADDRESS = '0.0.0.0'
PORT = 9393
LOGIN_TITLE = "PDNS"

# TIMEOUT - for large zones
TIMEOUT = 10

# LOG CONFIG
LOG_LEVEL = 'DEBUG'
LOG_FILE = ''

# Upload
UPLOAD_DIR = os.path.join(basedir, 'upload')

# DATABASE CONFIG
#You'll need MySQL-python
SQLA_DB_USER = 'root'
SQLA_DB_PASSWORD = '__DB_PASSWORD__'
SQLA_DB_HOST = '__DB_HOST__'
SQLA_DB_NAME = '__DB_NAME__'

#MySQL
SQLALCHEMY_DATABASE_URI = 'mysql://'+SQLA_DB_USER+':'\
    +SQLA_DB_PASSWORD+'@'+SQLA_DB_HOST+'/'+SQLA_DB_NAME
#SQLite
#SQLALCHEMY_DATABASE_URI = 'sqlite:////path/to/your/pdns.db'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# LDAP CONFIG
#LDAP_TYPE = 'ldap'
#LDAP_URI = 'ldaps://your-ldap-server:636'
#LDAP_USERNAME = 'cn=dnsuser,ou=users,ou=services,dc=duykhanh,dc=me'
#LDAP_PASSWORD = 'dnsuser'
#LDAP_SEARCH_BASE = 'ou=System Admins,ou=People,dc=duykhanh,dc=me'
# Additional options only if LDAP_TYPE=ldap
#LDAP_USERNAMEFIELD = 'uid'
#LDAP_FILTER = '(objectClass=inetorgperson)'

## AD CONFIG
#LDAP_TYPE = 'ad'
#LDAP_URI = 'ldaps://your-ad-server:636'
#LDAP_USERNAME = 'cn=dnsuser,ou=Users,dc=domain,dc=local'
#LDAP_PASSWORD = 'dnsuser'
#LDAP_SEARCH_BASE = 'dc=domain,dc=local'
## You may prefer 'userPrincipalName' instead
#LDAP_USERNAMEFIELD = 'sAMAccountName'
## AD Group that you would like to have accesss to web app
#LDAP_FILTER = 'memberof=cn=DNS_users,ou=Groups,dc=domain,dc=local'

# Github Oauth
GITHUB_OAUTH_ENABLE = False
#GITHUB_OAUTH_KEY = ''
#GITHUB_OAUTH_SECRET = ''
#GITHUB_OAUTH_SCOPE = 'email'
#GITHUB_OAUTH_URL = 'http://127.0.0.1:5000/api/v3/'
#GITHUB_OAUTH_TOKEN = 'http://127.0.0.1:5000/oauth/token'
#GITHUB_OAUTH_AUTHORIZE = 'http://127.0.0.1:5000/oauth/authorize'

#Default Auth
BASIC_ENABLED = True
SIGNUP_ENABLED = False

# POWERDNS CONFIG
PDNS_STATS_URL = '__API_URL__'
PDNS_API_KEY = '__API_KEY__'
PDNS_VERSION = '__PDNS_VERSION__'

# RECORDS ALLOWED TO EDIT
RECORDS_ALLOW_EDIT = ['A', 'AAAA', 'CNAME', 'SPF', 'PTR', 'MX', 'TXT']

# EXPERIMENTAL FEATURES
PRETTY_IPV6_PTR = False


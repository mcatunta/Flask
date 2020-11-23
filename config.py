def get_sql_uri():
    return 'mssql+pyodbc://DESKTOP-KSN5K9G/ventas?driver=ODBC+Driver+13+for+SQL+Server?Trusted_Connection=yes'

def get_jwt_secret():
    return 'securitytokenprivate'

def get_jwt_lifetime_seconds():
    return 3600
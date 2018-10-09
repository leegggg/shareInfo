import pandas


def getAllCodes(dbClient):
    codes = []
    codesSql = 'select code from CLASSIFIED_AREA;'
    codeDF = pandas.read_sql_query(codesSql, dbClient.engine)
    for _, row in codeDF.iterrows():
        code = row.loc['code']
        codes.append(code)
    return codes
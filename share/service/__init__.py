import pandas
import logging
from typing import List

logger = logging.getLogger(__name__).addHandler(logging.NullHandler())


def getAllCodes(dbClient) -> List[str]:
    codes = []
    codesSql = 'select code from CLASSIFIED_AREA;'
    codeDF = pandas.read_sql_query(codesSql, dbClient.engine)
    for _, row in codeDF.iterrows():
        code = row.loc['code']
        codes.append(code)
    return codes


def getAllIndexCodes() -> List[str]:
    import tushare.stock.cons as cons
    codes = []
    for index, value in cons.INDEX_SYMBOL.items():
        codes.append(index)

    return codes

from sqlalchemy import Column, String, create_engine, Integer, Float, Text, Date
from share.model.dao import Base
from dateutil.parser import parse
from share.util.numberUtil import toFloat
import logging
import datetime
from datetime import timedelta, datetime

def rowToORM(row, year, quarter):
    obj = ReportMain()
    obj.code = row.loc['code']  # 代码
    obj.name = row.loc['name']  # 名称
    obj.year = year  # year
    obj.quarter = quarter  # quarter


    tsString = "{:04d}-{:s}".format(year, row.loc['report_date'])
    if quarter >= 4:
        tsString = "{:04d}-{:s}".format(year+1, row.loc['report_date'])
    obj.report_date = datetime(year=year, month=quarter * 3, day=1) + timedelta(days=32)
    try:
        obj.report_date = parse(tsString)  # 发布日期
        if obj.report_date.month // 3 + 1 < quarter:
            if quarter < 4:
                obj.report_date = datetime(
                year=obj.report_date.year + 1,month=obj.report_date.month,day=obj.report_date.day)
    except ValueError:
        obj.report_date = datetime(year=year, month=quarter * 3, day=1) + timedelta(days=32)
        logging.warning(
            'Parse date {} for code {}({}) on {}Q{} failed using fallback {}.'.format(tsString, obj.code, obj.name,
                                                                                      year, quarter, obj.report_date))
        pass
    obj.eps = toFloat(row.loc['eps'])  # 每股收益
    obj.eps_yoy = toFloat(row.loc['eps_yoy'])  # 每股收益同比(%)
    obj.bvps = toFloat(row.loc['bvps'])  # 每股净资产
    obj.roe = toFloat(row.loc['roe'])  # 净资产收益率(%)
    obj.epcf = toFloat(row.loc['epcf'])  # 每股现金流量(元)
    obj.net_profits = toFloat(row.loc['net_profits'])  # 净利润(万元)
    obj.profits_yoy = toFloat(row.loc['profits_yoy'])  # 净利润同比(%)
    obj.distrib = toFloat(row.loc['distrib'])  # 分配方案
    obj.net_profit_ratio = toFloat(row.loc['net_profit_ratio'])  # 净利率(%)
    obj.gross_profit_rate = toFloat(row.loc['gross_profit_rate'])  # 毛利率(%)
    obj.business_income = toFloat(row.loc['business_income'])  # 营业收入(百万元)
    obj.bips = toFloat(row.loc['bips'])  # 每股主营业务收入(元)
    obj.arturnover = toFloat(row.loc['arturnover'])  # 应收账款周转率(次)
    obj.arturndays = toFloat(row.loc['arturndays'])  # 应收账款周转天数(天)
    obj.inventory_turnover = toFloat(row.loc['inventory_turnover'])  # 存货周转率(次)
    obj.inventory_days = toFloat(row.loc['inventory_days'])  # 存货周转天数(天)
    obj.currentasset_turnover = toFloat(row.loc['currentasset_turnover'])  # 流动资产周转率(次)
    obj.currentasset_days = toFloat(row.loc['currentasset_days'])  # 流动资产周转天数(天)
    obj.mbrg = toFloat(row.loc['mbrg'])  # 主营业务收入增长率(%)
    obj.nprg = toFloat(row.loc['nprg'])  # 净利润增长率(%)
    obj.nav = toFloat(row.loc['nav'])  # 净资产增长率
    obj.targ = toFloat(row.loc['targ'])  # 总资产增长率
    obj.epsg = toFloat(row.loc['epsg'])  # 每股收益增长率
    obj.seg = toFloat(row.loc['seg'])  # 股东权益增长率
    obj.currentratio = toFloat(row.loc['currentratio'])  # 流动比率
    obj.quickratio = toFloat(row.loc['quickratio'])  # 速动比率
    obj.cashratio = toFloat(row.loc['cashratio'])  # 现金比率
    obj.icratio = toFloat(row.loc['icratio'])  # 利息支付倍数
    obj.sheqratio = toFloat(row.loc['sheqratio'])  # 股东权益比率
    obj.adratio = toFloat(row.loc['adratio'])  # 股东权益增长率
    obj.cf_sales = toFloat(row.loc['cf_sales'])  # 经营现金净流量对销售收入比率
    obj.rateofreturn = toFloat(row.loc['rateofreturn'])  # 资产的经营现金流量回报率
    obj.cf_nm = toFloat(row.loc['cf_nm'])  # 经营现金净流量与净利润的比率
    obj.cf_liabilities = toFloat(row.loc['cf_liabilities'])  # 经营现金净流量对负债比率
    obj.cashflowratio = toFloat(row.loc['cashflowratio'])  # 现金流量比率
    return obj


# 定义User对象:
class ReportMain(Base):
    # 表的名字:
    __tablename__ = 'REPORT_MAIN'

    # 表的结构:
    code = Column(String(32), primary_key=True)  # 代码
    name = Column(String(32))  # 名称
    year = Column(Integer, primary_key=True)  # 946722600,
    quarter = Column(Integer, primary_key=True)  # 946722600,
    report_date = Column(Date)  # 发布日期
    eps = Column(Float)  # 每股收益
    eps_yoy = Column(Float)  # 每股收益同比(%)
    bvps = Column(Float)  # 每股净资产
    roe = Column(Float)  # 净资产收益率(%)
    epcf = Column(Float)  # 每股现金流量(元)
    net_profits = Column(Float)  # 净利润(万元)
    profits_yoy = Column(Float)  # 净利润同比(%)
    distrib = Column(Float)  # 分配方案
    net_profit_ratio = Column(Float)  # 净利率(%)
    gross_profit_rate = Column(Float)  # 毛利率(%)
    business_income = Column(Float)  # 营业收入(百万元)
    bips = Column(Float)  # 每股主营业务收入(元)
    arturnover = Column(Float)  # 应收账款周转率(次)
    arturndays = Column(Float)  # 应收账款周转天数(天)
    inventory_turnover = Column(Float)  # 存货周转率(次)
    inventory_days = Column(Float)  # 存货周转天数(天)
    currentasset_turnover = Column(Float)  # 流动资产周转率(次)
    currentasset_days = Column(Float)  # 流动资产周转天数(天)
    mbrg = Column(Float)  # 主营业务收入增长率(%)
    nprg = Column(Float)  # 净利润增长率(%)
    nav = Column(Float)  # 净资产增长率
    targ = Column(Float)  # 总资产增长率
    epsg = Column(Float)  # 每股收益增长率
    seg = Column(Float)  # 股东权益增长率
    currentratio = Column(Float)  # 流动比率
    quickratio = Column(Float)  # 速动比率
    cashratio = Column(Float)  # 现金比率
    icratio = Column(Float)  # 利息支付倍数
    sheqratio = Column(Float)  # 股东权益比率
    adratio = Column(Float)  # 股东权益增长率
    cf_sales = Column(Float)  # 经营现金净流量对销售收入比率
    rateofreturn = Column(Float)  # 资产的经营现金流量回报率
    cf_nm = Column(Float)  # 经营现金净流量与净利润的比率
    cf_liabilities = Column(Float)  # 经营现金净流量对负债比率
    cashflowratio = Column(Float)  # 现金流量比率

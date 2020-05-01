# Using an online data source

Many online sources of data can be queried directly from Python via "APIs". An API is an Application Programmer Interface. An API is a suite of programmer's tools and rules for accessing some library or service. Some APIs are quite complex, but others are quite straight forward.

## The Yahoo Finance API

Our good friends at Yahoo made an API for accessing their financial database just for students of CSC 1100. Just kidding. Actually [some guy](https://aroussi.com/post/python-yahoo-finance)
 did all the hard work for us.

### Installing

```text
pip3 install yfinance
pip3 install lxml
```

For Windows, use `pip` instead of `pip3`.

### Importing

```python
import yfinance as yf
```

This can take a while.

### Getting an equity or other Exchange entity

equity = yf.Ticker('MSFT')

### Various things you get access to

#### `.info`

```python
equity.info
```

`.info` is an **enormous** dictionary of data. 

Here is a sample:

```python
print(equity.info)
{'zip': '98052', 'sector': 'Technology', 'fullTimeEmployees': 144000, 'longBusinessSummary': 'Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. Its Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, and Skype for Business, as well as related Client Access Licenses (CAL); and Skype, Outlook.com, and OneDrive. It also provides LinkedIn that includes Talent and marketing solutions, and subscriptions; and Dynamics 365, a set of cloud-based and on-premises business solutions for small and medium businesses, large organizations, and divisions of enterprises. Its Intelligent Cloud segment licenses SQL and Windows Servers, Visual Studio, System Center, and related CALs; GitHub that provides a collaboration platform and code hosting service for developers; and Azure, a cloud platform. It also provides support services and Microsoft consulting services to assist customers in developing, deploying, and managing Microsoft server and desktop solutions; and training and certification to developers and IT professionals on various Microsoft products. Its More Personal Computing segment offers Windows OEM licensing and other non-volume licensing of the Windows operating system; Windows Commercial, such as volume licensing of the Windows operating system, Windows cloud services, and other Windows commercial offerings; patent licensing; Windows Internet of Things; and MSN advertising. It also provides Microsoft Surface, PC accessories, and other intelligent devices; Gaming, including Xbox hardware, and Xbox software and services; video games and third-party video game royalties; and Search, including Bing and Microsoft advertising. It sells its products through distributors and resellers; and directly through digital marketplaces, online stores, and retail stores. It has strategic partnerships with Humana Inc., Nokia, Telkomsel, Swiss Re, and Kubota Corporation. The company was founded in 1975 and is headquartered in Redmond, Washington.', 'city': 'Redmond', 'phone': '425-882-8080', 'state': 'WA', 'country': 'United States', 'companyOfficers': [], 'website': 'http://www.microsoft.com', 'maxAge': 1, 'address1': 'One Microsoft Way', 'fax': '425-706-7329', 'industry': 'Software—Infrastructure', 'previousClose': 177.43, 'regularMarketOpen': 180, 'twoHundredDayAverage': 158.63124, 'trailingAnnualDividendYield': 0.01093389, 'payoutRatio': 0.32930002, 'volume24Hr': None, 'regularMarketDayHigh': 180.4, 'navPrice': None, 'averageDailyVolume10Day': 39135125, 'totalAssets': None, 'regularMarketPreviousClose': 177.43, 'fiftyDayAverage': 159.41656, 'trailingAnnualDividendRate': 1.94, 'open': 180, 'toCurrency': None, 'averageVolume10days': 39135125, 'expireDate': None, 'yield': None, 'algorithm': None, 'dividendRate': 2.04, 'exDividendDate': 1589932800, 'beta': 0.962017, 'circulatingSupply': None, 'startDate': None, 'regularMarketDayLow': 176.23, 'priceHint': 2, 'currency': 'USD', 'trailingPE': 31.215816, 'regularMarketVolume': 53875857, 'lastMarket': None, 'maxSupply': None, 'openInterest': None, 'marketCap': 1363080249344, 'volumeAllCurrencies': None, 'strikePrice': None, 'averageVolume': 55850511, 'priceToSalesTrailing12Months': 10.153374, 'dayLow': 176.23, 'ask': 176.3, 'ytdReturn': None, 'askSize': 1200, 'volume': 53875857, 'fiftyTwoWeekHigh': 190.7, 'forwardPE': 29.28268, 'fromCurrency': None, 'fiveYearAvgDividendYield': 1.97, 'fiftyTwoWeekLow': 119.01, 'bid': 176.1, 'tradeable': False, 'dividendYield': 0.0115, 'bidSize': 3000, 'dayHigh': 180.4, 'exchange': 'NMS', 'shortName': 'Microsoft Corporation', 'longName': 'Microsoft Corporation', 'exchangeTimezoneName': 'America/New_York', 'exchangeTimezoneShortName': 'EDT', 'isEsgPopulated': False, 'gmtOffSetMilliseconds': '-14400000', 'quoteType': 'EQUITY', 'symbol': 'MSFT', 'messageBoardId': 'finmb_21835', 'market': 'us_market', 'annualHoldingsTurnover': None, 'enterpriseToRevenue': 9.702, 'beta3Year': None, 'profitMargins': 0.33016, 'enterpriseToEbitda': 21.259, '52WeekChange': 0.40583146, 'morningStarRiskRating': None, 'forwardEps': 6.12, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 7606049792, 'fundInceptionDate': None, 'annualReportExpenseRatio': None, 'bookValue': 14.467, 'sharesShort': 53310482, 'sharesPercentSharesOut': 0.0069999998, 'fundFamily': None, 'lastFiscalYearEnd': 1561852800, 'heldPercentInstitutions': 0.74035, 'netIncomeToCommon': 44323000320, 'trailingEps': 5.741, 'lastDividendValue': None, 'SandP52WeekChange': 0.0075372458, 'priceToBook': 12.387503, 'heldPercentInsiders': 0.01421, 'nextFiscalYearEnd': 1625011200, 'mostRecentQuarter': 1577750400, 'shortRatio': 0.82, 'sharesShortPreviousMonthDate': 1584057600, 'floatShares': 7494998724, 'enterpriseValue': 1302456958976, 'threeYearAverageReturn': None, 'lastSplitDate': 1045526400, 'lastSplitFactor': '2:1', 'legalType': None, 'morningStarOverallRating': None, 'earningsQuarterlyGrowth': 0.383, 'dateShortInterest': 1586908800, 'pegRatio': 2.2, 'lastCapGain': None, 'shortPercentOfFloat': 0.0069999998, 'sharesShortPriorMonth': 55155176, 'category': None, 'fiveYearAverageReturn': None, 'regularMarketPrice': 180, 'logo_url': 'https://logo.clearbit.com/microsoft.com'}
```

#### `.major_holders

```python
print(equity.major_holders)
        0                                      1
0   1.42%        % of Shares Held by All Insider
1  74.04%       % of Shares Held by Institutions
2  75.10%        % of Float Held by Institutions
3    4583  Number of Institutions Holding Shares
```

#### .history

```python
print (equity.history())
              Open    High     Low   Close    Volume  Dividends  Stock Splits
Date                                                                         
2020-04-01  153.00  157.75  150.82  152.11  57969900          0             0
2020-04-02  151.86  155.48  150.36  155.26  49630700          0             0
2020-04-03  155.10  157.38  152.19  153.83  41243300          0             0
2020-04-06  160.32  166.50  157.58  165.27  67111700          0             0
2020-04-07  169.59  170.00  163.26  163.49  62769000          0             0
2020-04-08  165.67  166.67  163.50  165.13  48318200          0             0
2020-04-09  166.36  167.37  163.33  165.14  51431800          0             0
2020-04-13  164.35  165.57  162.30  165.51  41905300          0             0
2020-04-14  169.00  173.75  168.00  173.70  52874300          0             0
2020-04-15  171.20  173.57  169.24  171.88  40940800          0             0
2020-04-16  174.30  177.28  172.90  177.04  50479600          0             0
2020-04-17  179.50  180.00  175.87  178.60  52765600          0             0
2020-04-20  176.63  178.75  174.99  175.06  36669600          0             0
2020-04-21  173.50  173.67  166.11  167.82  56203700          0             0
2020-04-22  171.39  174.00  170.82  173.52  34651600          0             0
2020-04-23  174.11  175.06  170.91  171.42  32790800          0             0
2020-04-24  172.06  174.56  170.71  174.55  34305300          0             0
2020-04-27  176.59  176.90  173.30  174.05  33194400          0             0
2020-04-28  175.59  175.67  169.39  169.81  34392700          0             0
2020-04-29  173.22  177.68  171.88  177.43  50872900          0             0
2020-04-30  180.00  180.40  176.23  179.21  53875857          0             0
```

This method can be quite complicated.

#### .recommendations

```python
 print(equity.recommendations)
                            Firm       To Grade From Grade Action
Date                                                             
2012-03-16        Argus Research            Buy                up
2012-03-19        Hilliard Lyons  Long-Term Buy              main
2012-03-22        Morgan Stanley     Overweight              main
2012-04-03                   UBS            Buy              main
2012-04-20  McAdams Wright Ragen            Buy              main
...                          ...            ...        ...    ...
2020-04-30        Morgan Stanley     Overweight              main
2020-04-30             Citigroup        Neutral              main
2020-04-30           BMO Capital     Outperform              main
2020-04-30         Credit Suisse     Outperform              main
2020-04-30                Mizuho            Buy              main

[281 rows x 4 columns]
```

### Many returned values are "Data Frames"

A Data Frame is a specialized container lending itself to data science work.

They are very rich and very deep. Data frames are way beyond this course. *However* there is an easy way to convert a data frame to CSV format and *that* you know how to use. There's a couple of intermediate steps needed.

```python
data = equity.recommendations.to_csv()
lines = data.split("\n")
reader = csv.reader(lines)
```

From here, you've got a CSV reader like you are accustomed to using.

Here's another example getting price history:

Here's an interactive example:

```python
>>> import yfinance as yf
>>> equity = yf.Ticker('MSFT')
>>> data = equity.history(period='max')
>>> type(data)
<class 'pandas.core.frame.DataFrame'>
>>> data = data.to_csv()
>>> lines = data.split('\n')
>>> import csv
>>> reader = csv.reader(lines)
>>> next(reader)
['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']
>>> 
```



SELECT StockCode
      ,InvoiceDate
	  ,max(StockCode) as maxStockCode
FROM
(
	SELECT [StockCode]
      ,[InvoiceDate]
      ,[Supplier]
	  ,max(StockCode) as maxStockCode1
  FROM [7.29.210.85,49170].[MyDB].[dbo].[EIRE_PTS$]
  GROUP BY StockCode, InvoiceDate, Supplier
) AS PT
GROUP BY StockCode, InvoiceDate

UNION ALL

SELECT StockCode
      ,InvoiceDate
	  ,max(StockCode) as maxStockCode
FROM
(
	SELECT [StockCode]
      ,[InvoiceDate]
      ,[Supplier]
	  ,max(StockCode) as maxStockCode1
  FROM [7.203.248.63,49170].[MyDB].[dbo].[France_PTS$]
  GROUP BY StockCode, InvoiceDate, Supplier
) AS PT
GROUP BY StockCode, InvoiceDate

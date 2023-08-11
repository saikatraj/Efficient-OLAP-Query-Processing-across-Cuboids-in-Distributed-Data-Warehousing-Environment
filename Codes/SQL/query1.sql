DECLARE @i INTEGER;
SET @i = 1;
WHILE @i <= 100
BEGIN
select SUM(UnitPrice) from dbo.OnlineRetail$ GROUP BY Country;
SET @i= @i+1;
END;
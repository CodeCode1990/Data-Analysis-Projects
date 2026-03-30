USE [Pharma BA report]
GO
--Changing the datatype since datetime was selected instead of date 
ALTER TABLE [dbo].[Fact_Sales_Canada_2021_2025]
ALTER COLUMN Date DATE;
GO
--We will need to calculate Revenue, total cost and profits into the Fact Sales Table
CREATE OR ALTER VIEW Fact_Sales AS 
SELECT 
    s.SalesID, s.Date, s.PatientID, s.Gender, s.Age_at_Sale, s.PharmacyID,
    s.DrugID, s.Units_Sold, s.Payment_Method,
    -- Base Financial Calculations (Row-Level)
    (s.Units_Sold * p.Unit_WAC) AS Revenue,
    COALESCE((s.Units_Sold * p.Prod_Cost), 0) AS MFC_Cost,
    -- Profit Logic
    CASE 
        WHEN p.Prod_Cost IS NOT NULL THEN (s.Units_Sold * p.Unit_WAC) - (s.Units_Sold * p.Prod_Cost)
        ELSE 0 
    END AS Internal_Profit
FROM dbo.Fact_Sales_Canada_2021_2025 AS s
JOIN dbo.Dim_Product AS p ON s.DrugID = p.DrugID;


SELECT 
    FORMAT(trans_date, 'yyyy-MM') AS month, -- Extracts year and month
    country,
    COUNT(*) AS trans_count, -- Total number of transactions
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count, -- Approved transactions count
    SUM(amount) AS trans_total_amount, -- Total amount of all transactions
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount -- Total amount of approved transactions
FROM 
    Transactions
GROUP BY 
    FORMAT(trans_date, 'yyyy-MM'), country; -- Group by month and country

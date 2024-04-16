Select product_id ,year as first_year, quantity,price
from Sales s
where (product_id,year) in (Select product_id,min(year) 
                            from sales s 
                            group by product_id)
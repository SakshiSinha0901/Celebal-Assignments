# E-Commerce SQL Query Results

## q1_all_customers

 customer_id first_name last_name              email      city       state  join_date  is_premium
         101      Aarav    Sharma  aarav.s@email.com    Mumbai Maharashtra 2024-01-15           1
         102      Priya     Patel  priya.p@email.com Ahmedabad     Gujarat 2024-02-20           0
         103      Rohan     Gupta  rohan.g@email.com     Delhi       Delhi 2024-03-10           1
         104      Sneha     Reddy  sneha.r@email.com Hyderabad   Telangana 2024-04-05           0
         105     Vikram     Singh vikram.s@email.com    Jaipur   Rajasthan 2024-05-12           1
         106     Ananya      Iyer ananya.i@email.com   Chennai  Tamil Nadu 2024-06-18           0
         107      Karan     Mehta  karan.m@email.com      Pune Maharashtra 2024-07-22           1
         108      Divya      Nair  divya.n@email.com     Kochi      Kerala 2024-08-30           0

## q2_customer_names_city

first_name last_name      city
     Aarav    Sharma    Mumbai
     Priya     Patel Ahmedabad
     Rohan     Gupta     Delhi
     Sneha     Reddy Hyderabad
    Vikram     Singh    Jaipur
    Ananya      Iyer   Chennai
     Karan     Mehta      Pune
     Divya      Nair     Kochi

## q3_unique_product_categories

   category
   Clothing
Electronics
       Home

## q7_delivered_orders

 order_id  customer_id order_date    status  total_amount
     1001          101 2024-08-01 Delivered          4498
     1002          102 2024-08-03 Delivered           799
     1004          101 2024-08-10 Delivered          3499
     1006          105 2024-08-15 Delivered          5898
     1008          103 2024-08-20 Delivered           899
     1010          108 2024-08-28 Delivered          1598

## q8_electronics_above_2000

 product_id      product_name    category brand  unit_price  stock_qty
        203       Smart Watch Electronics Noise        2999        150
        205 Bluetooth Speaker Electronics   JBL        3499        200

## q9_maharashtra_customers_2024

 customer_id first_name last_name             email   city       state  join_date  is_premium
         101      Aarav    Sharma aarav.s@email.com Mumbai Maharashtra 2024-01-15           1
         107      Karan     Mehta karan.m@email.com   Pune Maharashtra 2024-07-22           1

## q10_orders_between_dates_not_cancelled

 order_id  customer_id order_date    status  total_amount
     1004          101 2024-08-10 Delivered          3499
     1006          105 2024-08-15 Delivered          5898
     1007          106 2024-08-18   Pending          1299
     1008          103 2024-08-20 Delivered           899
     1009          107 2024-08-25   Shipped          6098

## q11_index_benefit_sample_query

 order_id  customer_id order_date    status  total_amount
     1001          101 2024-08-01 Delivered          4498
     1002          102 2024-08-03 Delivered           799
     1003          103 2024-08-05   Shipped          7498
     1004          101 2024-08-10 Delivered          3499
     1005          104 2024-08-12 Cancelled          2999
     1006          105 2024-08-15 Delivered          5898
     1007          106 2024-08-18   Pending          1299
     1008          103 2024-08-20 Delivered           899

## q12_sargable_join_date_query

 customer_id first_name last_name              email      city       state  join_date  is_premium
         101      Aarav    Sharma  aarav.s@email.com    Mumbai Maharashtra 2024-01-15           1
         102      Priya     Patel  priya.p@email.com Ahmedabad     Gujarat 2024-02-20           0
         103      Rohan     Gupta  rohan.g@email.com     Delhi       Delhi 2024-03-10           1
         104      Sneha     Reddy  sneha.r@email.com Hyderabad   Telangana 2024-04-05           0
         105     Vikram     Singh vikram.s@email.com    Jaipur   Rajasthan 2024-05-12           1
         106     Ananya      Iyer ananya.i@email.com   Chennai  Tamil Nadu 2024-06-18           0
         107      Karan     Mehta  karan.m@email.com      Pune Maharashtra 2024-07-22           1
         108      Divya      Nair  divya.n@email.com     Kochi      Kerala 2024-08-30           0

## q13_total_orders

 total_orders
           10

## q14_total_revenue_delivered

 delivered_revenue
             17191

## q15_average_unit_price_by_category

   category  average_unit_price
   Clothing              2699.0
Electronics              2224.0
       Home               949.0

## q16_order_count_revenue_by_status

   status  order_count  total_revenue
Delivered            6          17191
  Shipped            2          13596
Cancelled            1           2999
  Pending            1           1299

## q17_max_min_product_price_by_category

   category  most_expensive_product_price  cheapest_product_price
   Clothing                          4599                     799
Electronics                          3499                     899
       Home                          1299                     599

## q18_categories_avg_price_above_2000

   category  average_unit_price
   Clothing              2699.0
Electronics              2224.0

## q19_inner_join_orders_customers

 order_id order_date first_name last_name  total_amount
     1001 2024-08-01      Aarav    Sharma          4498
     1002 2024-08-03      Priya     Patel           799
     1003 2024-08-05      Rohan     Gupta          7498
     1004 2024-08-10      Aarav    Sharma          3499
     1005 2024-08-12      Sneha     Reddy          2999
     1006 2024-08-15     Vikram     Singh          5898
     1007 2024-08-18     Ananya      Iyer          1299
     1008 2024-08-20      Rohan     Gupta           899
     1009 2024-08-25      Karan     Mehta          6098
     1010 2024-08-28      Divya      Nair          1598

## q20_left_join_customers_orders

 customer_id first_name last_name  order_id order_date  total_amount
         101      Aarav    Sharma      1001 2024-08-01          4498
         101      Aarav    Sharma      1004 2024-08-10          3499
         102      Priya     Patel      1002 2024-08-03           799
         103      Rohan     Gupta      1003 2024-08-05          7498
         103      Rohan     Gupta      1008 2024-08-20           899
         104      Sneha     Reddy      1005 2024-08-12          2999
         105     Vikram     Singh      1006 2024-08-15          5898
         106     Ananya      Iyer      1007 2024-08-18          1299
         107      Karan     Mehta      1009 2024-08-25          6098
         108      Divya      Nair      1010 2024-08-28          1598

## q21_three_table_join_order_items_products

 order_id         product_name  quantity  unit_price  discount_pct
     1001     Wireless Earbuds         2        1499             0
     1001         Laptop Stand         1         899            10
     1002       Cotton T-Shirt         1         799             0
     1003          Smart Watch         1        2999             0
     1003        Running Shoes         1        4599             5
     1004    Bluetooth Speaker         1        3499             0
     1005          Smart Watch         1        2999             0
     1006     Wireless Earbuds         1        1499            10
     1006        Running Shoes         1        4599             5
     1007         Bedsheet Set         1        1299             0
     1008         Laptop Stand         1         899             0
     1009    Bluetooth Speaker         1        3499             0
     1009 Cushion Covers (Set)         2         599            15
     1010         Bedsheet Set         1        1299             0
     1010 Cushion Covers (Set)         1         599             0

## q24_case_price_tiers

        product_name  unit_price price_tier
    Wireless Earbuds        1499  Mid-Range
      Cotton T-Shirt         799     Budget
         Smart Watch        2999  Mid-Range
       Running Shoes        4599    Premium
   Bluetooth Speaker        3499    Premium
        Bedsheet Set        1299  Mid-Range
        Laptop Stand         899     Budget
Cushion Covers (Set)         599     Budget

## q25_delivered_vs_not_delivered

 delivered_orders  not_delivered_orders
                6                     4

## validation_customers_count

 total_customers
               8

## validation_products_count

 total_products
              8

## validation_orders_count

 total_orders
           10

## validation_order_items_count

 total_order_items
                15


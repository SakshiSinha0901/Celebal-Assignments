# Superstore SQL Query Results

## 01_schema

 cid          name      type  notnull dflt_value  pk
   0        row_id   INTEGER        0       None   0
   1      order_id      TEXT        0       None   0
   2    order_date TIMESTAMP        0       None   0
   3     ship_date TIMESTAMP        0       None   0
   4     ship_mode      TEXT        0       None   0
   5   customer_id      TEXT        0       None   0
   6 customer_name      TEXT        0       None   0
   7       segment      TEXT        0       None   0
   8       country      TEXT        0       None   0
   9          city      TEXT        0       None   0
  10         state      TEXT        0       None   0
  11   postal_code   INTEGER        0       None   0
  12        region      TEXT        0       None   0
  13    product_id      TEXT        0       None   0
  14      category      TEXT        0       None   0
  15  sub_category      TEXT        0       None   0
  16  product_name      TEXT        0       None   0
  17         sales      REAL        0       None   0
  18      quantity   INTEGER        0       None   0
  19      discount      REAL        0       None   0

## 02_sample_data

 row_id       order_id          order_date           ship_date      ship_mode customer_id   customer_name   segment       country            city      state  postal_code region      product_id        category sub_category                                                     product_name    sales  quantity  discount    profit
      1 CA-2016-152156 2016-11-08 00:00:00 2016-11-11 00:00:00   Second Class    CG-12520     Claire Gute  Consumer United States       Henderson   Kentucky        42420  South FUR-BO-10001798       Furniture    Bookcases                                Bush Somerset Collection Bookcase 261.9600         2      0.00   41.9136
      2 CA-2016-152156 2016-11-08 00:00:00 2016-11-11 00:00:00   Second Class    CG-12520     Claire Gute  Consumer United States       Henderson   Kentucky        42420  South FUR-CH-10000454       Furniture       Chairs      Hon Deluxe Fabric Upholstered Stacking Chairs, Rounded Back 731.9400         3      0.00  219.5820
      3 CA-2016-138688 2016-06-12 00:00:00 2016-06-16 00:00:00   Second Class    DV-13045 Darrin Van Huff Corporate United States     Los Angeles California        90036   West OFF-LA-10000240 Office Supplies       Labels        Self-Adhesive Address Labels for Typewriters by Universal  14.6200         2      0.00    6.8714
      4 US-2015-108966 2015-10-11 00:00:00 2015-10-18 00:00:00 Standard Class    SO-20335  Sean O'Donnell  Consumer United States Fort Lauderdale    Florida        33311  South FUR-TA-10000577       Furniture       Tables                    Bretford CR4500 Series Slim Rectangular Table 957.5775         5      0.45 -383.0310
      5 US-2015-108966 2015-10-11 00:00:00 2015-10-18 00:00:00 Standard Class    SO-20335  Sean O'Donnell  Consumer United States Fort Lauderdale    Florida        33311  South OFF-ST-10000760 Office Supplies      Storage                                   Eldon Fold 'N Roll Cart System  22.3680         2      0.20    2.5164
      6 CA-2014-115812 2014-06-09 00:00:00 2014-06-14 00:00:00 Standard Class    BH-11710 Brosina Hoffman  Consumer United States     Los Angeles California        90032   West FUR-FU-10001487       Furniture  Furnishings Eldon Expressions Wood and Plastic Desk Accessories, Cherry Wood  48.8600         7      0.00   14.1694
      7 CA-2014-115812 2014-06-09 00:00:00 2014-06-14 00:00:00 Standard Class    BH-11710 Brosina Hoffman  Consumer United States     Los Angeles California        90032   West OFF-AR-10002833 Office Supplies          Art                                                       Newell 322   7.2800         4      0.00    1.9656
      8 CA-2014-115812 2014-06-09 00:00:00 2014-06-14 00:00:00 Standard Class    BH-11710 Brosina Hoffman  Consumer United States     Los Angeles California        90032   West TEC-PH-10002275      Technology       Phones                                   Mitel 5320 IP Phone VoIP phone 907.1520         6      0.20   90.7152
      9 CA-2014-115812 2014-06-09 00:00:00 2014-06-14 00:00:00 Standard Class    BH-11710 Brosina Hoffman  Consumer United States     Los Angeles California        90032   West OFF-BI-10003910 Office Supplies      Binders             DXL Angle-View Binders with Locking Rings by Samsill  18.5040         3      0.20    5.7825
     10 CA-2014-115812 2014-06-09 00:00:00 2014-06-14 00:00:00 Standard Class    BH-11710 Brosina Hoffman  Consumer United States     Los Angeles California        90032   West OFF-AP-10002892 Office Supplies   Appliances                                 Belkin F5C206VTEL 6 Outlet Surge 114.9000         5      0.00   34.4700

## 03_total_rows

 total_rows
       9994

## 04_filter_region_west

      order_id   customer_name region    sales   profit
CA-2016-138688 Darrin Van Huff   West   14.620   6.8714
CA-2014-115812 Brosina Hoffman   West   48.860  14.1694
CA-2014-115812 Brosina Hoffman   West    7.280   1.9656
CA-2014-115812 Brosina Hoffman   West  907.152  90.7152
CA-2014-115812 Brosina Hoffman   West   18.504   5.7825
CA-2014-115812 Brosina Hoffman   West  114.900  34.4700
CA-2014-115812 Brosina Hoffman   West 1706.184  85.3092
CA-2014-115812 Brosina Hoffman   West  911.424  68.3568
CA-2016-161389    Irene Maddox   West  407.976 132.5922
CA-2014-167164 Alejandro Grove   West   55.500   9.9900

## 05_filter_category_technology

      order_id   category sub_category    sales   profit
CA-2014-115812 Technology       Phones  907.152  90.7152
CA-2014-115812 Technology       Phones  911.424  68.3568
CA-2014-143336 Technology       Phones  213.480  16.0110
CA-2016-121755 Technology  Accessories   90.570  11.7741
CA-2016-117590 Technology       Phones 1097.544 123.4737
CA-2015-117415 Technology       Phones  371.168  41.7564
CA-2017-120999 Technology       Phones  147.168  16.5564
CA-2016-118255 Technology  Accessories   45.980  19.7714
CA-2016-169194 Technology  Accessories   45.000   4.9500
CA-2016-169194 Technology       Phones   21.800   6.1040

## 06_filter_date

      order_id          order_date   sales   profit
CA-2017-114412 2017-04-15 00:00:00  15.552   5.4432
US-2017-156909 2017-07-16 00:00:00  71.372  -1.0196
CA-2017-107727 2017-10-19 00:00:00  29.472   9.9468
CA-2017-120999 2017-09-10 00:00:00 147.168  16.5564
CA-2017-139619 2017-09-19 00:00:00  95.616   9.5616
CA-2017-114440 2017-09-14 00:00:00  19.050   8.7630
US-2017-118038 2017-12-09 00:00:00   1.248  -1.9344
US-2017-118038 2017-12-09 00:00:00   9.708  -5.8248
US-2017-118038 2017-12-09 00:00:00  27.240   2.7240
US-2017-119662 2017-11-13 00:00:00 230.376 -48.9549

## 07_filter_sales_above_500

      order_id      customer_name        category     sales     profit
CA-2014-145317        Sean Miller      Technology 22638.480 -1811.0784
CA-2016-118689       Tamara Chand      Technology 17499.950  8399.9760
CA-2017-140151       Raymond Buch      Technology 13999.960  6719.9808
CA-2017-127180       Tom Ashbrook      Technology 11199.968  3919.9888
CA-2017-166709       Hunter Lopez      Technology 10499.970  5039.9856
CA-2016-117121      Adrian Barton Office Supplies  9892.740  4946.3700
CA-2014-116904       Sanjit Chand Office Supplies  9449.950  4630.4755
US-2016-107440       Bill Shonely      Technology  9099.930  2365.9818
CA-2016-158841       Sanjit Engle      Technology  8749.950  2799.9840
CA-2016-143714 Christopher Conant      Technology  8399.976  1119.9968

## 08_multiple_filters

      order_id region  category    sales     profit
CA-2017-118892   East Furniture 4416.174  -630.8820
CA-2015-117086   East Furniture 4404.900  1013.1270
US-2015-126977   East Furniture 4228.704   158.5764
CA-2014-128209   East Furniture 4007.840   -50.0980
CA-2014-116246   East Furniture 3785.292   420.5880
US-2015-150630   East Furniture 3083.430 -1665.0522
CA-2017-100111   East Furniture 2888.127   609.7157
CA-2015-160227   East Furniture 2621.322   553.3902
CA-2016-169670   East Furniture 2563.056   313.2624
CA-2017-100111   East Furniture 2254.410   375.7350

## 09_sales_by_region

 region  total_sales
   West    725457.82
   East    678781.24
Central    501239.89
  South    391721.91

## 10_profit_by_region

 region  total_profit
   West     108418.45
   East      91522.78
  South      46749.43
Central      39706.36

## 11_sales_quantity_by_category

       category  total_sales  total_quantity
     Technology    836154.03            6939
      Furniture    741999.80            8028
Office Supplies    719047.03           22906

## 12_average_sales_by_category

       category  average_sales
     Technology         452.71
      Furniture         349.83
Office Supplies         119.32

## 13_profit_by_sub_category

sub_category  total_profit
     Copiers      55617.82
      Phones      44515.73
 Accessories      41936.64
       Paper      34053.57
     Binders      30221.76
      Chairs      26590.17
     Storage      21278.83
  Appliances      18138.01
 Furnishings      13059.14
   Envelopes       6964.18
         Art       6527.79
      Labels       5546.25
    Machines       3384.76
   Fasteners        949.52
    Supplies      -1189.10
   Bookcases      -3472.56
      Tables     -17725.48

## 14_top_10_products_by_sales

                                                               product_name  total_sales
                                      Canon imageCLASS 2200 Advanced Copier     61599.82
Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind     27453.38
                      Cisco TelePresence System EX90 Videoconferencing Unit     22638.48
                               HON 5400 Series Task Chairs for Big and Tall     21870.58
                                 GBC DocuBind TL300 Electric Binding System     19823.48
                           GBC Ibimaster 500 Manual ProClick Binding System     19024.50
                                       Hewlett Packard LaserJet 3310 Copier     18839.69
                  HP Designjet T520 Inkjet Large Format Printer - 24" Color     18374.90
                                  GBC DocuBind P400 Electric Binding System     17965.07
                                High Speed Automatic Electric Letter Opener     17030.31

## 15_top_10_products_by_profit

                                                               product_name  total_profit
                                      Canon imageCLASS 2200 Advanced Copier      25199.93
Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind       7753.04
                                       Hewlett Packard LaserJet 3310 Copier       6983.88
                                         Canon PC1060 Personal Laser Copier       4570.93
                  HP Designjet T520 Inkjet Large Format Printer - 24" Color       4094.98
                                          Ativa V4110MDD Micro-Cut Shredder       3772.95
                           3D Systems Cube Printer, 2nd Generation, Magenta       3717.97
                 Plantronics Savi W720 Multi-Device Wireless Headset System       3696.28
                                       Ibico EPK-21 Electric Binding System       3345.28
                                          Zebra ZM400 Thermal Label Printer       3343.54

## 16_top_categories_by_sales

       category  total_sales
     Technology    836154.03
      Furniture    741999.80
Office Supplies    719047.03

## 17_top_states_by_sales

       state  total_sales
  California    457687.63
    New York    310876.27
       Texas    170188.05
  Washington    138641.27
Pennsylvania    116511.91
     Florida     89473.71
    Illinois     80166.10
        Ohio     78258.14
    Michigan     76269.61
    Virginia     70636.72

## 18_monthly_sales_trend

  month  monthly_sales  monthly_profit
2014-01       14236.90         2450.19
2014-02        4519.89          862.31
2014-03       55691.01          498.73
2014-04       28295.35         3488.84
2014-05       23648.29         2738.71
2014-06       34595.13         4976.52
2014-07       33946.39         -841.48
2014-08       27909.47         5318.11
2014-09       81777.35         8328.10
2014-10       31453.39         3448.26
2014-11       78628.72         9292.13
2014-12       69545.62         8983.57
2015-01       18174.08        -3281.01
2015-02       11951.41         2813.85
2015-03       38726.25         9732.10
2015-04       34195.21         4187.50
2015-05       30131.69         4667.87
2015-06       24797.29         3335.56
2015-07       28765.33         3288.65
2015-08       36898.33         5355.81

## 19_yearly_sales_trend

year  yearly_sales  yearly_profit
2014     484247.50       49543.97
2015     470532.51       61618.60
2016     609205.60       81795.17
2017     733215.26       93439.27

## 20_top_customers_by_sales

     customer_name  total_sales
       Sean Miller     25043.05
      Tamara Chand     19052.22
      Raymond Buch     15117.34
      Tom Ashbrook     14595.62
     Adrian Barton     14473.57
      Ken Lonsdale     14175.23
      Sanjit Chand     14142.33
      Hunter Lopez     12873.30
      Sanjit Engle     12209.44
Christopher Conant     12129.07

## 21_top_customers_by_profit

       customer_name  total_profit
        Tamara Chand       8981.32
        Raymond Buch       6976.10
        Sanjit Chand       5757.41
        Hunter Lopez       5622.43
       Adrian Barton       5444.81
        Tom Ashbrook       4703.79
Christopher Martinez       3899.89
       Keith Dawkins       3038.63
         Andy Reiter       2884.62
       Daniel Raglin       2869.08

## 22_duplicate_order_ids

      order_id  duplicate_count
CA-2017-100111               14
CA-2017-157987               12
US-2016-108504               11
CA-2016-165330               11
US-2015-126977               10
CA-2016-105732               10
CA-2015-131338               10
US-2016-114013                9
US-2015-163433                9
CA-2017-140949                9

## 23_duplicate_row_ids

Empty DataFrame
Columns: [row_id, duplicate_count]
Index: []

## 24_loss_making_products

                                                     product_name  total_sales  total_profit
                        Cubify CubeX 3D Printer Double Head Print     11099.96      -8879.97
                        Lexmark MX611dhe Monochrome Laser Printer     16829.90      -4589.97
                        Cubify CubeX 3D Printer Triple Head Print      7999.98      -3839.99
         Chromcraft Bull-Nose Wood Oval Conference Tables & Bases      9917.64      -2876.12
             Bush Advantage Collection Racetrack Conference Table      9544.73      -1934.40
                        GBC DocuBind P400 Electric Binding System     17965.07      -1878.17
            Cisco TelePresence System EX90 Videoconferencing Unit     22638.48      -1811.08
               Martin Yale Chadless Opener Electric Letter Opener     16656.20      -1299.18
                                     Balt Solid Wood Round Tables      6518.75      -1201.06
BoxOffice By Design Rectangular and Half-Moon Meeting Room Tables      1706.25      -1148.44

## 25_missing_values_check

 missing_order_id  missing_order_date  missing_customer_name  missing_sales  missing_profit
                0                   0                      0              0               0

## 26_negative_sales_check

Empty DataFrame
Columns: [row_id, order_id, order_date, ship_date, ship_mode, customer_id, customer_name, segment, country, city, state, postal_code, region, product_id, category, sub_category, product_name, sales, quantity, discount, profit]
Index: []

## 27_negative_quantity_check

Empty DataFrame
Columns: [row_id, order_id, order_date, ship_date, ship_mode, customer_id, customer_name, segment, country, city, state, postal_code, region, product_id, category, sub_category, product_name, sales, quantity, discount, profit]
Index: []

## 28_date_range_validation

   first_order_date     last_order_date
2014-01-03 00:00:00 2017-12-30 00:00:00


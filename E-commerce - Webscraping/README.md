## E-commerce Project

### Assignment Objectives

This project aims to evaluate the concepts of Web Scraping, Business Knowledge, and Practical Statistics as follows:

- Ability to extract data from internet sources using Web Scraping
- Ability to perform data preparation before further analysis
- Ability to build a problem statement using the SMART framework as part of business understanding
- Ability to perform descriptive statistical calculations
- Ability to conduct statistical testing and formulate hypotheses
- Ability to derive insights and information from calculations
- Ability to draw conclusions that address the problem statement

### Assignment Instructions and Cases

#### Case
The goal is to increase income through sales without enough capital for production, relying only on promotional funds. Thus, the decision is made to pursue a dropshipping model on Tokopedia.

There is uncertainty about what product to sell, but seblak (a popular Indonesian snack) comes to mind due to its current trendiness. However, there is doubt about whether there is significant consumer interest in seblak.

As a Data Scienties, the object is to analyze seblak product sales on Tokopedia to determine consumer interest and purchasing behavior.

The challenge is that no existing data is available apart from what is visible on the Tokopedia website. Hence, the journey begins with data extraction using Web Scraping.

#### A. Web Scraping
1. Extract data from the search results for the keyword "seblak" on Tokopedia:
   https://www.tokopedia.com/search?navsource=&page=1&q=seblak&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=
2. Collect data on `Product Name`, `Product Price`, `Seller`, `Store Location`, `Number of Sales`, and `Product Rating`.
3. Tokopedia features promotional schemes where the top panel displays products from merchants who pay for advertisements. Only collect data from regular product boxes with the element `<div class="css-974ipl">`.

   **Note:** For new products, there may be no information on the number of sales and product rating, resulting in different data counts for these columns. In such cases, fill missing values with `None`.

4. Extract product information from at least 10 search result pages.

5. Save the scraped data into a Pandas DataFrame.

#### B. Data Preparation
1. Perform simple data exploration:
   - Display a few rows of data and provide insights.
   - Display a summary of the data and explain findings, including potential next steps.
   - Check for missing values and provide insights from these findings.
2. Perform data cleaning:
   - Handle missing values, ensuring data consistency and appropriate data types for statistical calculations.

#### C. Business Understanding/Problem Statement
Create a problem statement using the SMART framework, detailing the Specific, Measurable, Achievable, Relevant, and Time-bound aspects.

#### D. Analysis
The analysis will focus on the following:

1. Calculate the mean, median, standard deviation, skewness, and kurtosis for columns related to price, number of sales, and rating. Derive insights related to the distribution and potential outliers in seblak product data.

2. Determine the minimum and maximum potential revenue from selling seblak products using confidence intervals (95% confidence level). Assume the data follows a normal distribution and the sales figures represent monthly sales.

3. Test whether there is a significant difference in product prices between the Greater Jakarta area (Jabodetabek) and other regions, considering potential differences in material costs. Formulate the null and alternative hypotheses and perform the appropriate hypothesis test.

4. Investigate if consumers prefer cheaper products by testing the correlation between price and product ratings. Analyze the correlation coefficient and p-value.

This README provides an overview of the project's objectives and requirements. The main goal is to extract, prepare, and analyze e-commerce data to derive business insights and make data-driven decisions.

## HOW TO PROCEED

1. **Check the HTML Structure**:
   - Open your browser and navigate to the e-commerce site you want to scrape. 
   - Right-click on the product elements and select `Inspect` to open `Developer Tools`. 
   - Identify the HTML tags and class names that correspond to product name, price, and reviews.

2. **Update the Selectors in the Script**:
   <br>
   Replace
     - `"div", class_="product-item"`, 
     - `"h2", class_="product-name"`, 
     - `"span", class_="product-price"`, and 
     - `"div", class_="product-reviews"`
   with the actual selectors from the site you are scraping.
    
3. Run the Script:
   - Execute the script to scrape the data and save it as a CSV file in the `data` directory. 
   
4. Check the Output:
   - Navigate to the `data` directory and open `raw_data.csv` to ensure the scraped data has been saved correctly.
   
### Note on Ethical Scraping:
Always ensure that you have permission to scrape a website by checking its `robots.txt` file or terms of service. Many sites, especially large ones like Amazon, have strict policies against scraping. Consider using APIs or other legal means to obtain data from such sites.
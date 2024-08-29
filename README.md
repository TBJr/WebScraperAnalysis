# Web Scraper with Data Analysis

This project is a Python-based web scraper that gathers data from an e-commerce website, performs sentiment analysis on product reviews, and generates visual reports.

## Project Structure

- `scrapers/`: Contains the web scraper for the e-commerce site.
- `processing/`: Contains scripts for cleaning and processing the scraped data.
- `analysis/`: Contains scripts for performing sentiment analysis.
- `visualization/`: Contains scripts for generating visual reports.
- `notebooks/`: Contains Jupyter Notebooks for exploratory data analysis.
- `data/`: Contains raw, cleaned, and analyzed data.

## How to Run the Project

1. **Scrape the Data**:
   ```bash
   python scrapers/ecommerce_scraper.py

2. **Clean the Data**:
   ```bash
   python processing/clean_data.py

3. **Perform Sentiment Analysis**:
   ```bash
   python analysis/sentiment_analysis.py
   
4. **Generate Visual Reports**:
   ```bash
   python visualization/generate_reports.py
   
5. **Explore Data Using Jupyter Notebook**: <br>
   Open the `EDA.ipynb` notebook in `Jupyter` and run the cells to explore the data. <br><br>

6. **Requirements**:
   - Python 3.x
   - BeautifulSoup4 
   - Requests 
   - Pandas 
   - NLTK 
   - Matplotlib 
   - Seaborn 
   - Jupyter Notebook
   <br><br>

7. **License**:
   <br>
   This project is licensed under the [MIT License](MT License).
8. **Final Setup**:
   Make sure to activate your virtual environment and install all the required libraries:
    ```bash
    source .venv/bin/activate
    pip install -r requirements.txt
   
Now, you can run each script step by step as outlined in the README.md to scrape, process, analyze, and visualize the data. This setup gives you a solid foundation for building and expanding your web scraping and data analysis project.
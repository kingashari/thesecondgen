# thesecondgen

This project is a web scraping tool that retrieves lottery prediction data from multiple websites. The data from these websites is located in `textarea` elements, and the tool allows users to select a specific lottery by name, scrape the related page, and output the numbers contained in the page's `textarea`.

## Features
- **Lottery Selection**: Users can choose from a list of lottery prediction sites (e.g., Hongkong Lotto, Sydney Lotto, etc.).
- **Web Scraping**: The tool automatically fetches and scrapes the selected lottery page to extract the lottery numbers.
- **Output**: The numbers from the selected page are displayed as a single concatenated string after the scrape.

## How It Works  
1. **Scraping Process**:
   - Once the user selects a lottery, the script fetches the corresponding page using the Python `requests` module.
   - The page's content is parsed using `BeautifulSoup` to locate `textarea` elements that contain the prediction data.
   
2. **Data Output**:
   - The contents of all `textarea` elements on the selected page are concatenated into a single string and printed to the console.

## Requirements

To run this project, ensure you have the following Python packages installed:

- `requests`
- `beautifulsoup4`

You can install these packages via pip:
```bash
pip install requests beautifulsoup4
```

## Supported 12 Country

The scraper currently supports the following lotteries:

1. Hongkong Lotto
2. Sydney Lotto
3. Singapore
4. Taiwan
5. Magnum Cambodia
6. China Pools
7. Bullseye
8. Japan
9. Germany Plus5
10. Sydney
11. Singapore
12. Hongkong

## Notes

- The lottery data is fetched from publicly available prediction pages.
- The scraper is set to work with websites that are structured using `textarea` elements to contain the data.
- Data from the websites may change daily or at irregular intervals, and this tool provides up-to-date results based on when the script is run.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

from pathlib import Path
def testParseWebpageContent(url, data):
    # Check if website folder exists
    if not Path("websites").exists():
        Path("websites").mkdir()
    
    # get number of files in websites folder
    num_files = len([f for f in Path("websites").iterdir() if f.is_file()])

    # Saves data to file
    with open(f"websites/{num_files}.html", "wb") as f:
        f.write(data)
    

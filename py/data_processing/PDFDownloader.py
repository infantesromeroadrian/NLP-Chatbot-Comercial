import requests

class PDFDownloader:
    def __init__(self, urls):
        self.urls = urls

    def download(self):
        ml_papers = []
        for i, url in enumerate(self.urls):
            response = requests.get(url)
            if response.status_code == 200:
                filename = f"paper{i+1}.pdf"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                    print(f"Downloaded {filename}")
                ml_papers.append(filename)
            else:
                print(f"Failed to download {url}")
        return ml_papers
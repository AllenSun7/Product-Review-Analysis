from google_scrapy import GoogleInfo


def get_info():
    #get reviews of apple homepod
    website = "https://www.google.com/search?safe=active&sxsrf=ALeKk00Iv5DVSTq8EEHkIs4aloKTrDpDXA%3A1582608611729&ei=47BUXt6NLMv4-gTFxLXwBA&q=apple+homepod+reviews&oq=apple+homepod+reviews&gs_l=psy-ab.3..0l3j0i22i30l6.18669.20227..20435...0.2..0.107.689.7j1......0....1..gws-wiz.......0i71j35i39j0i20i263j0i67.CDVwVnXlanc&ved=0ahUKEwiei_vA_OvnAhVLvJ4KHUViDU4Q4dUDCAs&uact=5"
    output_csv = "apple_homepod.csv"
    product = GoogleInfo(website, output_csv)
    product.scrapy_info()

def main():
    get_info()

if __name__ == "__main__":
    main()


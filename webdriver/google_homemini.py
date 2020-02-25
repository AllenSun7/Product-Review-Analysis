from google_scrapy import GoogleInfo


def get_info():
    #get reviews of google homemini
    website = "https://www.google.com/search?safe=active&biw=1527&bih=817&sxsrf=ALeKk02L8MMR8f3MDNkX_4O_aRYF9nxkoA%3A1582666165985&ei=tZFVXty_O8Ke-gSfo57ADw&q=Google+Home+mini+reviews&oq=Google+Home+mini+reviews&gs_l=psy-ab.3..0j0i7i30l7j0j0i7i30.26759.27444..27919...0.2..0.119.485.4j1......0....1..gws-wiz.......0i71j35i304i39j0i13.t54Z__ksv-Y&ved=0ahUKEwic7vv00u3nAhVCj54KHZ-RB_gQ4dUDCAs&uact=5"
    output_csv = "google_homemini.csv"
    product = GoogleInfo(website, output_csv)
    product.scrapy_info()

def main():
    get_info()

if __name__ == "__main__":
    main()
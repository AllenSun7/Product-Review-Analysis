from google_scrapy import GoogleInfo


def get_info():
    #get reviews of google homemini
    website_google_homemini = "https://www.google.com/search?safe=active&biw=1527&bih=817&sxsrf=ALeKk02L8MMR8f3MDNkX_4O_aRYF9nxkoA%3A1582666165985&ei=tZFVXty_O8Ke-gSfo57ADw&q=Google+Home+mini+reviews&oq=Google+Home+mini+reviews&gs_l=psy-ab.3..0j0i7i30l7j0j0i7i30.26759.27444..27919...0.2..0.119.485.4j1......0....1..gws-wiz.......0i71j35i304i39j0i13.t54Z__ksv-Y&ved=0ahUKEwic7vv00u3nAhVCj54KHZ-RB_gQ4dUDCAs&uact=5"
    output_csv_google_homemini = "google_homemini.csv"
    #get reviews of google home nest hub
    website_google_home_nest_hub = "https://www.google.com/search?safe=active&biw=1527&bih=817&sxsrf=ALeKk02L8MMR8f3MDNkX_4O_aRYF9nxkoA%3A1582666165985&ei=tZFVXty_O8Ke-gSfo57ADw&q=Google+Home+mini+reviews&oq=Google+Home+mini+reviews&gs_l=psy-ab.3..0j0i7i30l7j0j0i7i30.26759.27444..27919...0.2..0.119.485.4j1......0....1..gws-wiz.......0i71j35i304i39j0i13.t54Z__ksv-Y&ved=0ahUKEwic7vv00u3nAhVCj54KHZ-RB_gQ4dUDCAs&uact=5"
    output_csv_google_home_nest_hub = "google_home_nest_hub.csv"
    #get reviews of apple homepod
    website_apple_homepod = "https://www.google.com/search?safe=active&sxsrf=ALeKk00Iv5DVSTq8EEHkIs4aloKTrDpDXA%3A1582608611729&ei=47BUXt6NLMv4-gTFxLXwBA&q=apple+homepod+reviews&oq=apple+homepod+reviews&gs_l=psy-ab.3..0l3j0i22i30l6.18669.20227..20435...0.2..0.107.689.7j1......0....1..gws-wiz.......0i71j35i39j0i20i263j0i67.CDVwVnXlanc&ved=0ahUKEwiei_vA_OvnAhVLvJ4KHUViDU4Q4dUDCAs&uact=5"
    output_csv_apple_homepod = "apple_homepod.csv"
    #get reviews of amazon echo dot 
    website_amazon_echo_dot = "https://www.google.com/search?safe=active&sxsrf=ALeKk020vsFlz0xUoNGanfwi7aLdYyDYgA%3A1582691567092&ei=7_RVXs-aBbK90PEPtd6smAo&q=echo+dot+reviews&oq=echo+dot+reviews&gs_l=psy-ab.3..35i39j0i7i30l9.5992.5992..6709...0.2..0.87.87.1......0....1..gws-wiz.......0i71.mIxWS2374Fc&ved=0ahUKEwiPzpTFse7nAhWyHjQIHTUvC6MQ4dUDCAs&uact=5"
    output_csv_amazon_echo_dot = "amazon_echo_dot.csv"
    

    #run to scrapy info
    product = GoogleInfo(website_amazon_echo_dot, output_csv_amazon_echo_dot)
    product.scrapy_info()

def main():
    get_info()

if __name__ == "__main__":
    main()
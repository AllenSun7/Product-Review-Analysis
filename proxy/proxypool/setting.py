# Redis database host
REDIS_HOST = '127.0.0.1'

# Redis post
REDIS_PORT = 6379

# Redis password，leave "None" if no password
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

# procy score
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# pool threshold
POOL_UPPER_THRESHOLD = 50000

# test cycle
TESTER_CYCLE = 20
# get cycle
GETTER_CYCLE = 300

# test API，your target address
TEST_URL = 'http://www.amazon.com'

# API setup 
API_HOST = '0.0.0.0'
API_PORT = 5555

# switch
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# maximal batch size
BATCH_TEST_SIZE = 10

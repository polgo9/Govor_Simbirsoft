from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.accept_insecure_certs = True

driver = webdriver.Chrome(options=options)

from selenium import webdriver
import time

# 企業の詳細画面おURLを全件取得する
def get_detail_url(driver):
    a_list = driver.find_elements_by_css_selector('#result_list > div > div.box_inner.clearfix > div.box_l > div.drug > a')
    url_list = []
    for a in a_list:
        url_list.append(a.get_attribute('href'))
    return url_list

def print_detail_info(driver):
    try:
        name = driver.find_element_by_css_selector('#headerInner > div > div.shop_data > div > h3').text
        mail = driver.find_element_by_css_selector('#shopContent > div.btmInfo > div.info_table.clearfix > div.right > dl:nth-child(4) > dd').text
        print(str(name) + ',' + str(mail))
    except:
        print(str(name) + 'の情報の取得に失敗しました')


def main():
    driver = webdriver.Chrome()

    # 一覧画面に遷移
    driver.get("https://www.kyo-navi.com/search/area/")

    is_continue = True
    while is_continue:
        current_url = driver.current_url
        url_list = get_detail_url(driver)

        for url in url_list:
            driver.get(url)
            print_detail_info(driver)
        try:
            driver.get(current_url)
            next_btn = driver.find_element_by_css_selector('#my_list > div:nth-child(3) > div.fl_r.clearfix > li.ne > a')
            next_btn.click()
        except:
            is_continue = False

    driver.quit()

if __name__  == '__main__':
    main()

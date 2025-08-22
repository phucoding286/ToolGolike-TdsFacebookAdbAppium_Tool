from modules import *

class GolikeFacebook:
    def __init__(self):
        pass

    def gl_init(self, driver: webdriver.Remote):
        try:
            driver.activate_app("com.golike")

            kiem_thuong_btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='Kiếm Thưởng']"))
            )
            kiem_thuong_btn.click()

            facebook_cell = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='Facebook']"))
            )
            facebook_cell.click()
            return "success"
        except:
            return "error"


    def get_task(self, driver: webdriver.Remote):
        try:
            driver.activate_app("com.golike")
            size = driver.get_window_size()
            x = size['width'] // 2
            y = size['height'] // 2
            driver.swipe(x, y, x, 0, 500)

            task_content, i = '', 0
            while task_content == "" and i < 5:
                try:
                    first_task = WebDriverWait(driver, 1).until(
                        EC.presence_of_all_elements_located((By.XPATH, "//*[@text='chevron_right']"))
                    )
                    first_task[0].click()
                except:
                    driver.swipe(x, y, x, 0, 500)
                    i += 1
                    continue

                time.sleep(1)

                task_content = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[starts-with(@text, 'TĂNG')]"))
                ).text

            target_info = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[starts-with(@text, 'Job Id')]"))
            ).text
            
            # facebook_btn = WebDriverWait(driver, 5).until(
            #     EC.presence_of_element_located((By.XPATH, "//*[@text='Facebook Làm việc bằng ứng dụng Facebook trên điện thoại. chevron_right']"))
            # )
            # facebook_btn.click()
            
            try:
                facebook_btn = WebDriverWait(driver, 2.5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[starts-with(@text, 'Facebook Làm việc bằng ứng dụng Facebook')]"))
                )
                facebook_btn.click()
            except:
                facebook_btn = WebDriverWait(driver, 2.5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[starts-with(@text, 'Làm việc bằng ứng dụng Facebook')]"))
                )
                facebook_btn.click()
            
            return task_content, target_info.split("Fb Id: ")[1]
        except:
            return "error"
    
    
    def verify_job(self, driver: webdriver.Remote):
        try:
            driver.activate_app("com.golike")
            size = driver.get_window_size()
            x = size['width'] // 2
            y = size['height'] // 2

            for _ in range(4):
                driver.swipe(x, 100, x, y -50, 500)
                time.sleep(0.1)

            driver.swipe(x, y, x, 100, 500)
        
            for i in range(2):
                try:
                    complete_btn = WebDriverWait(driver, 4).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@text='Bấm hoàn thành để nhận tiền sau khi làm việc xong.']"))
                    )
                    complete_btn.click()
                    break
                except:
                    driver.swipe(x, y, x, 100, 500)
                    continue
            else:
                return "error"

            try:
                error_job_check = WebDriverWait(driver, 5).until(
                     EC.presence_of_element_located((By.XPATH, "//*[@text='Lỗi']"))
                )
                ok_btn = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@text='OK']"))
                )
                ok_btn.click()
                return "error"
            except:
                pass
        
            success_job_check = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='Thành công']"))
            )
            ok_btn = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='OK']"))
            )
            ok_btn.click()
            return "success"
        except:
            return "error"
    

    def drop_job(self, driver: webdriver.Remote):
        try:
            driver.activate_app("com.golike")
            size = driver.get_window_size()
            x = size['width'] // 2
            y = size['height'] // 2

            for _ in range(4):
                driver.swipe(x, 100, x, y -50, 500)
                time.sleep(0.1)

            for i in range(2):
                driver.swipe(x, y, x, 100, 500)
                try:
                    drop_job_btn = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@text='Báo lỗi cho hệ thống khi làm việc thất bại']"))
                    )
                    drop_job_btn.click()
                    break
                except:
                    driver.swipe(x, y, x, 100, 500)
                    continue
            else:
                raise ValueError()
        
            for i in range(2):
                driver.swipe(x, y, x, 100, 500)
                try:
                    send_drop_job_btn = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@text='Gửi báo cáo']"))
                    )
                    send_drop_job_btn.click()
                    break
                except:
                    driver.swipe(x, y, x, 100, 500)
                    continue
            else:
                raise ValueError()
        
            try:
                sended_check = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@text='Đã gửi báo cáo lên hệ thống']"))
                )
                ok_btn = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@text='OK']"))
                )
                ok_btn.click()
                return "success"
            except:
                raise ValueError()
        except:
            return "error"
        

    def set_account_run(self, driver: webdriver.Remote, facebook_uid: str):
        try:
            ok_btn = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='OK']"))
            )
            ok_btn.click()
        except:
            pass
        try:
            driver.activate_app("com.golike")
            # select_list_account = WebDriverWait(driver, 5).until(
            #     EC.presence_of_element_located((By.XPATH, "//*[@text='kiếm thưởng chevron_right']"))
            # )
            # select_list_account.click()

            select_list_account = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[starts-with(@text, 'kiếm thưởng chevron_right')]"))
            )
            select_list_account.click()

            account_selected = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f"//*[@resource-id='{facebook_uid}']"))
            )
            account_selected.click()

            try:
                ok_btn = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@text='OK']"))
                )
                ok_btn.click()
            except:
                pass
            # driver.background_app("com.golike")
            return "success"
        except:
            return "error"

if __name__ == "__main__":
    driver = driver_init(
        adb_path="adb",
        ask_udid=False,
        device_id="192.168.1.246:5555",
        appium_port=1000
    )
    golike_init(driver)

    gl_obj = GolikeFacebook()
    gl_obj.gl_init(driver)
    gl_obj.set_account_run(driver, "61579390404117")
    # input(">>> ")
    print(gl_obj.get_task(driver))
    time.sleep(4)

    for i in range(5):
        if gl_obj.verify_job(driver) == "error":
            print(f"Lỗi xác minh job thử lại {i+1}/5")
        else:
            print("Xác minh job thành công!")
            break
    else:
        print("Lỗi xác minh job, tiến hành bỏ job")
        if gl_obj.drop_job(driver) == "success":
            print("Đã bỏ job thành công")
        else:
            print("Đã bỏ job thất bại")
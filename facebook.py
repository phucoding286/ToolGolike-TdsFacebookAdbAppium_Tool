from modules import *

class FacebookInteract:
    def __init__(self, logging=True, adb_path=None, device_id=None):
        self.logging = logging
        self.adb_path = adb_path
        self.device_id = device_id

    def like_page(self, driver: webdriver.Remote, page_link: str):
        size = driver.get_window_size()
        x = size['width'] // 2
        y = size['height'] // 2

        try:
            driver.activate_app("com.facebook.lite")

            os.system(f"{self.adb_path} -s {self.device_id} shell am start -n com.facebook.lite/.MainActivity -a android.intent.action.VIEW -d {page_link}")
            for i in range(3):
                try:
                    like_follow_btn = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup[2]"))
                    )
                    like_follow_btn.click()
                    return "success"
                except:
                    try:
                        like_follow_btn = WebDriverWait(driver, 1).until(
                            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup[2]"))
                        )
                        like_follow_btn.click()
                        return "success"
                    except:
                        try:
                            like_follow_btn = WebDriverWait(driver, 1).until(
                                EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[4]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[2]"))
                            )
                            like_follow_btn.click()
                            return "success"
                        except:
                            try:
                                like_follow_btn = WebDriverWait(driver, 1).until(
                                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[4]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup[2]"))
                                )
                                like_follow_btn.click()
                                return "success"
                            except:
                                try:
                                    like_follow_btn = WebDriverWait(driver, 1).until(
                                        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[4]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup[2]"))
                                    )
                                    like_follow_btn.click()
                                    return "success"
                                except:
                                    driver.swipe(x, y/2, x, 0, 500)
            else:
                return "error"
        except:
            return "error"

    
    def find_and_like_post(self, driver: webdriver.Remote, fb_id, feed=True):
        try:
            driver.activate_app("com.facebook.lite")

            size = driver.get_window_size()
            x = size['width'] // 2
            y = size['height'] // 2
            os.system(f"{self.adb_path} -s {self.device_id} shell am start -n com.facebook.lite/.MainActivity -a android.intent.action.VIEW -d https://www.facebook.com/")

            time.sleep(2)
        
            find_btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.View"))
            )
            find_btn.click()

            find_cell = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.MultiAutoCompleteTextView"))
            )
            find_cell.send_keys("https://www.facebook.com/" + fb_id)
            driver.press_keycode(66)
 
            time.sleep(4)

            for i in range(4):
                try:
                    like_btn = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.View[1]"))
                    )
                    like_btn.click()
                    os.system(f"{self.adb_path} -s {self.device_id} shell input keyevent 4")
                    time.sleep(2)
                    os.system(f"{self.adb_path} -s {self.device_id} shell input keyevent 4")
                    return "success"
                except:
                    print(error_color(f"[! {self.device_id}] like bài viết thất bại, thử kéo xuống tìm nút like"))
                    driver.swipe(x, y, x, 0, 500)
                    continue
            else:
                return "error"
        except:
            return "error"

        
if __name__ == "__main__":
    driver = driver_init(
        adb_path="adb",
        ask_udid=False,
        device_id="192.168.1.250:5555",
        appium_port=1000
    )
    fb = FacebookInteract(True, "adb", "192.168.1.250:5555")
    fb.find_and_like_post(driver, "pfbid05o7PRSL9i2qNh4eBpqcHY5biEioTBWeNoVqPugroQr4SfngKJKTrGFnsBZRbbikcl")
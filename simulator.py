from modules import *

class ActionsSimulator:
    def __init__(self, logging=True, adb_path="adb", device_id=None):
        self.logging = logging
        self.adb_path = adb_path
        self.device_id = device_id

    
    def __most_relevant_btn_click_in_post__(self, driver: webdriver.Remote):
        try:
            return WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup"))
            ).click()
        except:
            try:
                return WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.View[1]"))
                ).click()
            except:
                try:
                    return WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.View[2]"))
                    ).click()
                except:
                    return {"error": "cant_click"}
                
    
    def __like_post__(self, driver: webdriver.Remote):
        try:
            try:
                WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[2]"))
                ).click()
            except:
                WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[2]"))
                ).click()
            return "success"
        except:
            return "error"
        
    def __cmt__(self, driver: webdriver.Remote):
        cmt_list = [
            "Xin chào",
            "Chào",
            "Chao ban nha",
            "Chuc mot ngay tot lanh",
            "Hi",
            "Chúc may mắn nhé.",
            "Hello"
        ]
        try:
            try:
                cmt_cell = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.MultiAutoCompleteTextView"))
                )
            except:
                cmt_cell = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.MultiAutoCompleteTextView"))
                )
            cmt_cell.send_keys(random.choice(cmt_list))
            time.sleep(1)
            try:
                send_btn = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[5]/android.view.View"))
                )
                send_btn.click()
            except:
                try:
                    send_btn = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.View"))
                    )
                    send_btn.click()
                except:
                    send_btn = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.View"))
                    )
                    send_btn.click()
            return "success"
        except:
            return "error"
        

    def __share_post__(self, driver: webdriver.Remote):
        try:
            try:
                share_btn = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[5]"))
                )
                share_btn.click()
            except:
                share_btn = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[4]"))
                )
                share_btn.click()
            
            time.sleep(1)
            
            try:
                share_to_profile_btn = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]"))
                )
                share_to_profile_btn.click()
            except:
                share_to_profile_btn = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]"))
                )
                share_to_profile_btn.click()

            time.sleep(1)

            share_btn_last = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[3]"))
            )
            share_btn_last.click()
            return "success"
        except:
            return "error"
                
    
    def __reels_viewer__(self, driver: webdriver.Remote, x: int, y: int):
        desicion_reel_click = random.uniform(0.1, 1) < 0.5
        if not desicion_reel_click:
            return
        if self.logging:
            print(system_color(f"[> {self.device_id}] chọn lướt reel"))

        try:
            try:
                reel_btn = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[11]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View[3]"))
                )
                reel_btn.click()
            except:
                try:
                    reel_btn = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[11]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.View[3]"))
                    )
                    reel_btn.click()
                except:
                    reel_btn = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[11]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.View[2]"))
                    )
                    reel_btn.click()
            
            scroll_times = random.randint(4, 7)
            for i in range(scroll_times):
                driver.activate_app("com.facebook.lite")
                driver.swipe(x, y, x, 0, 500)
                rdn_time_j = 0
                while rdn_time_j < 0.8:
                    rdn_time_j = random.random()
                    time.sleep(rdn_time_j)
                print(system_color(f"[> {self.device_id}] scroll reel times {i+1}/{scroll_times}"))

            os.system(f"{self.adb_path} -s {self.device_id} shell input keyevent 4")   
        except:
            if self.logging:
                print(error_color(f"[! {self.device_id}] Lỗi khi nhấn lướt reel!"))
            return {"error": "reel_click_error"}


    def __comment_in_comment_viewer__(self, driver: webdriver.Remote):
        try:
            view_previous_reply_btn = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[3]"))
            )
            view_previous_reply_btn.click()

            try:
                try:
                    WebDriverWait(driver, 2).until( # most relevant btn
                        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup"))
                    )
                except:
                    WebDriverWait(driver, 1).until( # most relevant btn
                        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup[1]"))
                    )
                return False
            except:
                if self.logging:
                    print(success_color(f"[# {self.device_id}] In comment successfuly"))
                
                return True
        except:
            return False


    def __comment_viewer__(self, driver: webdriver.Remote, x: int, y: int):
        try:
            desicion_cmt_click = random.uniform(0.1, 1) < 0.4
            if not desicion_cmt_click:
                return
            else:
                print(system_color(f"[> {self.device_id}] chọn nhấn vào xem comment"))
            
            try:
                cmt_btn = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[11]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.View"))
                )
                cmt_btn.click()
            except:
                try:
                    cmt_btn = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[11]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup[3]/android.view.View"))
                    )
                    cmt_btn.click()
                except:
                    try:
                        cmt_btn = WebDriverWait(driver, 1).until(
                            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[11]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup[3]/android.view.View"))
                        )
                        cmt_btn.click()
                    except:
                        cmt_btn = WebDriverWait(driver, 1).until(
                            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[11]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.View"))
                        )
                        cmt_btn.click()

            try:
                WebDriverWait(driver, 2).until( # most relevant btn
                    EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup"))
                )
            except:
                try:
                    WebDriverWait(driver, 1).until( # most relevant btn
                        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup[1]"))
                    )
                except:
                    os.system(f"{self.adb_path} -s {self.device_id} shell input keyevent 4")
                    if self.logging:
                        print(error_color(f"[! {self.device_id}] bài viết chưa có comment nào"))
                    return

            if self.logging:
                print(system_color(f"[> {self.device_id}] view in comment..."))

            if random.uniform(0.1, 1) < 0.3:
                if self.logging:
                    print(system_color(f"[> {self.device_id}] chọn thực hiện like"))
                r = self.__like_post__(driver)
                if r == "error":
                    print(error_color(f"[! {self.device_id}] lỗi khi like"))
                else:
                    print(success_color(f"[# {self.device_id}] like thành công"))
            else:
                print(system_color(f"[> {self.device_id}] không chọn thực hiện like"))
            
            if random.uniform(0.1, 1) < 0.2:
                if self.logging:
                    print(system_color(f"[> {self.device_id}] chọn thực hiện comment"))
                r = self.__cmt__(driver)
                if r == "error":
                    print(error_color(f"[! {self.device_id}] lỗi khi comment"))
                else:
                    print(success_color(f"[# {self.device_id}] comment thành công"))
            else:
                print(system_color(f"[> {self.device_id}] không chọn thực hiện comment"))

            if random.uniform(0.1, 1) < 0.3:
                if self.logging:
                    print(system_color(f"[> {self.device_id}] chọn thực hiện share post"))
                r = self.__share_post__(driver)
                if r == "error":
                    print(error_color(f"[! {self.device_id}] lỗi khi share post"))
                else:
                    print(success_color(f"[# {self.device_id}] share post thành công"))
            else:
                print(system_color(f"[> {self.device_id}] không chọn thực hiện share post"))
            
            in_comment_flag = False
            scroll_times = random.randint(4, 7)
            for i in range(scroll_times):
                driver.activate_app("com.facebook.lite")
                
                r = self.__comment_in_comment_viewer__(driver)
                if r is True:
                    in_comment_flag = True

                reverse_scroll = random.uniform(0.1, 1) < 0.25
                if reverse_scroll:
                    driver.swipe(x, y, x, y*2, 500)
                else:
                    driver.swipe(x, y, x, 0, 500)

                rdn_time_j = 0
                while rdn_time_j < 0.8:
                    rdn_time_j = random.random()
                    time.sleep(rdn_time_j)

                print(system_color(f"[> {self.device_id}] scroll comment times {i+1}/{scroll_times}"))
            
            if in_comment_flag:
                os.system(f"{self.adb_path} -s {self.device_id} shell input keyevent 4")
                time.sleep(1.5)
            os.system(f"{self.adb_path} -s {self.device_id} shell input keyevent 4")
        except:
            if self.logging:
                print(error_color(f"[! {self.device_id}] Lỗi khi vào xem comment bài viết"))


    def feed_scroller(self, driver: webdriver.Remote, action_times: int, back_when_num_times: int = 20, reel_viewer=True, back_home=True):
        try:
            driver.activate_app("com.facebook.lite")
            size = driver.get_window_size()
            x = size['width'] // 2
            y = size['height'] // 2
            if back_home:
                os.system(f"{self.adb_path} -s {self.device_id} shell am start -n com.facebook.lite/.MainActivity -a android.intent.action.VIEW -d https://www.facebook.com/")

            for i in range(1, action_times+1):
                driver.activate_app("com.facebook.lite")
                if (i - back_when_num_times) == 0:
                    os.system(f"{self.adb_path} -s {self.device_id} shell input keyevent 4")

                reverse_scroll = random.random() < 0.05
                if reverse_scroll:
                    driver.swipe(x, y, x, y*2, 500)
                else:
                    driver.swipe(x, y, x, 0, 500)

                rdn_time_i = 0
                while rdn_time_i < 0.6:
                    rdn_time_i = random.random()
                    time.sleep(rdn_time_i)

                if self.logging:
                    print(system_color(f"[> {self.device_id}] had scroll {i}/{action_times}"))

                self.__comment_viewer__(driver, x, y)
                if reel_viewer:
                    self.__reels_viewer__(driver, x, y)
        except:
            return {"error": "unknown"}


if __name__ == "__main__":
    driver = driver_init(
        adb_path="adb",
        ask_udid=False,
        device_id="192.168.1.250:5555",
        appium_port=1000
    )
    facebook_init(driver, "250:5555")
    action_sim = ActionsSimulator(
        logging=True,
        adb_path="adb",
        device_id="192.168.1.250:5555"
    )

    action_sim.feed_scroller(driver, 10, 10)
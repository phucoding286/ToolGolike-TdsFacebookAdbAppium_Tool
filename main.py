from modules import *
from simulator import ActionsSimulator
from traodoisub import TraodoisubAPI
from facebook import FacebookInteract
from golike import GolikeFacebook
prices = 0

class MainProgram:
    def __init__(self, worker_account_link: str, logging=True, device_id=None, adb_path=None,
                 tds_token=None, tds_cookie=None, appium_port=None, tds_username=None, tds_password=None,
                 max_error_times_for_break=-1):
        self.adb_path = adb_path
        self.device_id = device_id
        self.tds_token = tds_token
        self.logging = logging
        self.tds_cookie = tds_cookie
        self.appium_port = appium_port
        self.worker_account_link = worker_account_link
        self.tds_username = tds_username
        self.tds_password = tds_password
        self.max_error_times_for_break = max_error_times_for_break

        self.action_sim = ActionsSimulator(
            logging=logging,
            adb_path=adb_path,
            device_id=device_id
        )
        self.tds_login()
        self.tds = TraodoisubAPI(
            tds_cookie=self.tds_cookie,
            tds_token=self.tds_token
        )
        self.fb = FacebookInteract(
            logging=logging,
            adb_path=adb_path,
            device_id=device_id
        )
        self.gl_fb = GolikeFacebook()

    def tds_login(self):
        if self.tds_cookie is None and (self.tds_username is not None and self.tds_password is not None):
            while True:
                try:
                    response = scraper.post(
                        url="https://traodoisub.com/scr/login.php",
                        data={"username": self.tds_username, "password": self.tds_password},
                        timeout=10
                    )
                    cookies = response.cookies.get_dict()
                    for k,v in cookies.items():
                        self.tds_cookie = f"{k}={v}"
                    response = scraper.get(
                        url="https://traodoisub.com/scr/user.php",
                        headers={"cookie": self.tds_cookie}
                    )
                    if self.logging:
                        print(success_color(f"[# {self.device_id}] Đăng nhập thành công"))
                        print("TDS_COOKIE:", self.tds_cookie)
                    break
                except:
                    if self.logging:
                        print(error_color(f"[! {self.device_id}] Lỗi khi login thử lại..."))
                        time.sleep(2)
                        continue

    def doing_task(self, action_times, back_when_num_times, action_times_in_page, feed_mode=False):
        r = self.tds.setup_worker_account(self.worker_account_link)
        if self.logging:
            print(f"{self.device_id} SET_WORKER_ACC: {r}")

        driver = driver_init(
            adb_path=self.adb_path,
            ask_udid=False,
            device_id=self.device_id,
            appium_port=self.appium_port
        )
        facebook_init(driver, self.device_id)
        
        error_count, success_count = 1, 0
        error_get_task_counter = 0
        error_get_task_try_counter = 0
        like_error_counter = 0
        error_facebook_init = 0
        error_sim_counter = 0
        while True:
            if feed_mode:
                print(f"FEED_MODE: thiết bị '{self.device_id}' với account tds '{self.tds_username}' bạn đang trong chế độ nuôi tài khoản'")
                r = self.action_sim.feed_scroller(
                    driver,
                    action_times * error_count,
                    back_when_num_times * error_count
                )
                if isinstance(r, dict) and "error" in r:
                    if error_facebook_init >= 10:
                        break
                    if error_sim_counter >= 5:
                        return
                    print(error_color(f"[! {self.device_id}] lỗi khi simulate."))
                    try: facebook_init(driver, self.device_id)
                    except: error_facebook_init += 1
                    error_sim_counter +=1
                    continue
                else:
                    error_facebook_init = 0
                    error_sim_counter = 0
                continue

            r = self.tds.get_task_facebook_fanpage(False)
            if "error" in r and self.logging:
                print(f"{self.device_id} GET_TASK_ERROR!")
                time.sleep(2)
                error_get_task_counter += 1
                if error_get_task_counter >= 10:
                    print(error_color(f"[! {self.device_id}] vượt quá số lần nhận task, thử đăng nhập lại tds"))
                    self.tds_cookie = None
                    self.tds_login()
                    self.tds = TraodoisubAPI(
                        tds_cookie=self.tds_cookie,
                        tds_token=self.tds_token
                    )
                    error_get_task_counter = 0
                    error_get_task_try_counter += 1
                    if error_get_task_try_counter >= 4:
                        break
                continue
            else:
                error_get_task_try_counter = 0
            
            like_error = False
            try_sim_times_counter = 0
            for infor in r:
                r = self.action_sim.feed_scroller(
                    driver,
                    action_times * error_count,
                    back_when_num_times * 2 if error_count != 1 else back_when_num_times
                )
                if isinstance(r, dict) and "error" in r and not like_error:
                    print(error_color(f"[! {self.device_id}] simulate lỗi."))
                    if try_sim_times_counter >= 4:
                        return
                    if error_facebook_init >= 10:
                        break
                    try: driver.quit()
                    except: pass
                    try: facebook_init(driver, self.device_id)
                    except: error_facebook_init += 1
                    try_sim_times_counter += 1
                    continue
                else:
                    try_sim_times_counter = 0

                if self.fb.like_page(driver, page_link=infor['link']) == "success":
                    if self.logging:
                        print(success_color(f"[# {self.device_id}] like trang thành công."))
                        r = self.action_sim.feed_scroller(
                            driver,
                            action_times_in_page,
                            action_times_in_page * 2,
                            reel_viewer=False,
                            back_home=False
                        )
                        if isinstance(r, dict) and "error" in r:
                            if error_facebook_init >= 10:
                                break
                            if error_sim_counter >= 5:
                                return
                            print(error_color(f"[! {self.device_id}] lỗi khi simulate."))
                            try: facebook_init(driver, self.device_id)
                            except: error_facebook_init += 1
                            error_sim_counter += 1
                        else:
                            error_facebook_init = 0
                            error_sim_counter = 0
                        os.system(f"{self.adb_path} -s {self.device_id} shell input keyevent 4")
                        like_error = False
                        like_error_counter = 0
                else:
                    if self.logging:
                        print(error_color(f"[! {self.device_id}] like page thất bại"))
                    os.system(f"{self.adb_path} -s {self.device_id} shell input keyevent 4")
                    like_error = True
                    like_error_counter += 1
                    if like_error_counter >= 2:
                        break
                    continue
                
                for k in range(2):
                    time.sleep(1)
                    r = self.tds.get_coin_in_fanpage_task(infor['id'])
                    if r == "error":
                        if self.logging:
                            print(error_color(f"[! {self.device_id}] xác minh job nhận coin thất bại, thử lại..."))
                        if self.logging:
                            print(system_color(f'[> {self.device_id}] thử đăng nhập lại..'))
                        self.tds_cookie = None
                        self.tds_login()
                        self.tds = TraodoisubAPI(
                            tds_cookie=self.tds_cookie,
                            tds_token=self.tds_token
                        )
                        time.sleep(2)
                    else:
                        if self.logging:
                            print(success_color(f"[# {self.device_id}] xác minh job và nhận coin thành công."))
                        success_count += 1
                        if success_count >= 2:
                            error_count = 1
                            success_count = 0
                        break
                else:
                    print(error_color(f"[! {self.device_id}] xác minh job nhận coin thất bại"))
                    error_count += 1
                    success_count = 0
                    if self.max_error_times_for_break != -1 and error_count >= self.max_error_times_for_break:
                        break
                
                for i in range(5):
                    r = self.tds.get_current_coin()
                    if r == "error":
                        print(f"{self.tds_username} ERR_GET_CURR_COIN: try again.")
                        time.sleep(2)
                        continue
                    print(success_color(f"[$ {self.device_id}] tổng số coin hiện có trong account tds '{self.tds_username}' hiện tại là: {r}"))
                    break
            
            if self.max_error_times_for_break != -1 and error_count >= self.max_error_times_for_break:
                break
            if like_error_counter >= 2:
                break

    
    def doing_golike_task(self, action_times, back_when_num_times):
        global prices
        success_times = 0
        driver = driver_init(
            adb_path=self.adb_path,
            ask_udid=False,
            device_id=self.device_id,
            appium_port=self.appium_port
        )
        err = 0
        while err < 10:
            golike_init(driver)
            time.sleep(5)
            if self.gl_fb.gl_init(driver) == "success" and self.gl_fb.set_account_run(driver, self.tds.get_id_facebook_account(self.worker_account_link)) == "success":
                print(success_color(f"[# {self.device_id}] khởi tạo driver golike thành công."))
                break
            else:
                print(error_color(f"[! {self.device_id}] lỗi khi khởi tạo driver golike, thử lại..."))
                try: golike_init(driver)
                except: pass
                err += 1
                continue

        facebook_init(
            driver=driver,
            device_id=self.device_id
        )
        
        error_vrfj_counter = 0
        error_facebook_init = 0
        like_error_counter = 0
        error_sim_counter = 0
        while True:
            r = self.action_sim.feed_scroller(
                driver,
                action_times,
                back_when_num_times
            )
            if isinstance(r, dict) and "error" in r:
                if error_facebook_init >= 10:
                    break
                if error_sim_counter >= 5:
                    return
                print(error_color(f"[! {self.device_id}] lỗi khi simulate."))
                try: facebook_init(driver, self.device_id)
                except: error_facebook_init += 1
                error_sim_counter += 1
                continue
            else:
                error_facebook_init = 0
                error_sim_counter = 0
            
            r = self.gl_fb.get_task(driver)
            while r[0].strip() != "TĂNG LIKE CHO BÀI VIẾT":
                if r == "error":
                    print(error_color(f"[! {self.device_id}] lỗi khi nhận job, bỏ qua luồng làm việc golike này."))
                    return
                print(error_color(f"[! {self.device_id}] không phải nhiệm vụ like bài viết, bỏ qua job và thử lại..."))
                if self.gl_fb.drop_job(driver) == "success":
                    print(success_color(f"[# {self.device_id}] bỏ job thành công"))
                else:
                    print(error_color(f"[! {self.device_id}] bỏ job thất bại, bỏ qua luồng làm việc golike này."))
                    return
                r = self.gl_fb.get_task(driver)

            rlp = self.fb.find_and_like_post(driver, r[1])
            if rlp == "error":
                print(error_color(f"[! {self.device_id}] like bài viết thất bại, tạo lại fb driver và bỏ job"))
                like_error_counter += 1
                if like_error_counter >= 5:
                    return
                if self.gl_fb.drop_job(driver) == "success":
                    print(success_color(f"[# {self.device_id}] bỏ job thành công"))
                else:
                    print(error_color(f"[! {self.device_id}] bỏ job thất bại, bỏ qua luồng làm việc golike này."))
                    return
                if error_facebook_init >= 10:
                    break
                try: facebook_init(driver, self.device_id)
                except: error_facebook_init += 1
                continue
            else:
                like_error_counter = 0
                print(success_color(f"[$ {self.device_id}] like bài viết thành công, tiến hành xác minh job"))
                pass
            
            for i in range(2):
                rvj = self.gl_fb.verify_job(driver)
                if rvj == "error":
                    print(error_color(f"[! {self.device_id}] xác minh job thất bại, thử lại {i+1}/2"))
                    continue
                else:
                    prices += 35
                    print(success_color(f"[$ {self.device_id}] xác minh job thành công, tổng tiền mà tool đã làm trong phiên là {prices}đ"))
                    error_vrfj_counter = 0
                    success_times += 1
                    break
            else:
                print(error_color(f"[! {self.device_id}] xác minh job thất bại, bỏ job"))
                if self.gl_fb.drop_job(driver) == "success":
                    print(success_color(f"[# {self.device_id}] bỏ job thành công"))
                else:
                    print(error_color(f"[! {self.device_id}] bỏ job thất bại, bỏ qua luồng làm việc golike này."))
                    return
                error_vrfj_counter += 1
                if error_vrfj_counter >= 2:
                    return
                
                
def run():
    config = json.load(open("config.json", "r", encoding="utf-8"))    
    workers = config['workers_information']
    random.shuffle(workers)
    while True:
        for worker in workers:
            if not worker['run'] or worker['run_mode'] == "nuôi tài khoản":
                continue
            
            result = subprocess.run(
                 [config['memuc_path'], 'listvms'],
                 capture_output=True,
                 text=True
            )

            vm_id = -1
            for inf_res in result.stdout.splitlines():
                if inf_res.split(",")[1] == worker['device_ipv4']:
                    subprocess.run(
                        [config['memuc_path'], 'start', "-i", inf_res.split(",")[0]],
                        capture_output=True,
                        text=True
                    )
                    vm_id = inf_res.split(",")[0]
                    break

            m = MainProgram(
                worker_account_link=worker['facebook_worker_link'],
                logging=config['logging'],
                device_id=worker['device_ipv4'] + ":5555",
                adb_path=config['adb_path'],
                tds_token=worker['tds_token'],
                tds_cookie=worker['tds_cookie'],
                appium_port=config['appium_port'],
                tds_username=worker['tds_username'],
                tds_password=worker['tds_password'],
                max_error_times_for_break=config['max_error_times_for_break']
            )
            
            try:
                m.doing_task(
                    config['action_times_when_feed_mode'] if worker['run_mode'].lower().strip() == "nuôi tài khoản" else config['action_times'],
                    config['action_times_when_feed_mode'] if worker['run_mode'].lower().strip() == "nuôi tài khoản" else config['back_when_num_times'],
                    config['action_times_in_page'],
                    worker['run_mode'].lower().strip() == "nuôi tài khoản"
                )
            except:
                pass
            
            try:
                m.doing_golike_task(
                    config['action_times_when_feed_mode'] if worker['run_mode'].lower().strip() == "nuôi tài khoản" else config['action_times'],
                    config['action_times_when_feed_mode'] if worker['run_mode'].lower().strip() == "nuôi tài khoản" else config['back_when_num_times']
                )
            except:
                pass

            subprocess.run(
                [config['memuc_path'], 'stop', "-i", vm_id],
                capture_output=True,
                text=True
            )


if __name__ == "__main__":
    # t = multiprocessing.Process(target=run)
    # t.daemon = True
    # t.start()
    run()
    while True:
        try: input(">>> ")
        except: pass
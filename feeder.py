from modules import *
from simulator import ActionsSimulator


def thread(adb_path, device_id, appium_port, memuc_path, action_times, back_when_num_times):
    result = subprocess.run(
        [memuc_path, 'listvms'],
        capture_output=True,
        text=True
    )

    vm_id = -1
    for inf_res in result.stdout.splitlines():
        if inf_res.split(",")[1] == device_id:
            subprocess.run(
                [memuc_path, 'start', "-i", inf_res.split(",")[0]],
                capture_output=True,
                text=True
            )
            vm_id = inf_res.split(",")[0]
            break
    
    action_sim = ActionsSimulator(
        logging=True,
        adb_path=adb_path,
        device_id=device_id
    )

    driver = driver_init(
        adb_path=adb_path,
        ask_udid=False,
        device_id=device_id + ":5555",
        appium_port=appium_port
    )
    
    facebook_init(
        driver=driver,
        device_id=device_id
    )
        
    while True:
        r = action_sim.feed_scroller(
            driver,
            action_times,
            back_when_num_times
        )
        if isinstance(r, dict) and "error" in r:
            try: facebook_init(driver, device_id)
            except: pass
            continue


def run():
    config = json.load(open("config.json", "r", encoding="utf-8"))    
    workers = config['workers_information']
    for worker in workers:
        if not worker['run'] or worker['run_mode'] != "nuôi tài khoản":
            continue
        t = multiprocessing.Process(
            target=thread,
            args=[
                config['adb_path'],
                worker['device_ipv4'],
                config['appium_port'],
                config['memuc_path'],
                config['action_times'],
                config['back_when_num_times']
            ]
        )
        t.daemon = True
        t.start()

    while True:
        try: input()
        except: pass


if __name__ == "__main__":
    run()
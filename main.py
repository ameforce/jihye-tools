import win32gui
import win32con
import time


def auto_closer(window_name: str, exec_count: int = 1, latency: float = 1) -> None:
    count = 0
    while True:
        if count >= exec_count:
            break
        print(f'Detecting [{window_name}]...', end='')
        handle = win32gui.FindWindow(None, window_name)
        if handle:
            print('Success')
            win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)
            count += 1
        else:
            print('Fail')
        time.sleep(latency)


def main() -> None:
    auto_closer('AhnLab V3 Lite', 1, 0.5)
    # auto_closer(r'DeepL  ', 1, 0.5)


if __name__ == '__main__':
    main()

from seleniumbase import SB

with SB(uc=True, test=True) as iga:

    if True:
        url = "https://kick.com/brutalles"
        iga.uc_open_with_reconnect(url, 5)
        iga.uc_gui_click_captcha()
        iga.sleep(1)
        iga.uc_gui_handle_captcha()
        iga.sleep(1)
        if iga.is_element_present('button:contains("Accept")'):
            iga.uc_click('button:contains("Accept")', reconnect_time=4)
        if iga.is_element_visible('#injected-channel-player'):
            while iga.is_element_visible('#injected-channel-player'):
                iga.sleep(10)
            

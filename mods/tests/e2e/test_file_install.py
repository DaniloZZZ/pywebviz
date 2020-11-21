from importlib import reload
from selenium import webdriver
import os

import time

import libvis_mods
import libvis


os.environ['MOZ_HEADLESS'] = '1'

def test_init_instal(tmp_path):
    import libvis.modules.installed as modules
    """
    1. Initialize a module from template
    2. Itstall the module
    3. Start the Libvis
    4. Test front with selenium
    """
    print("Starting Selenium...")
    browser = webdriver.Firefox()

    # 1.
    target_dir = tmp_path/'tmp_mods'
    target_dir.mkdir()
    modname = 'TestMod'
    libvis_mods.init_file(modname, output_dir=target_dir)

    # 2.
    libvis_mods.install(modname,
                        target_dir/f"{modname}/{modname}_back.py",
                        target_dir/f"{modname}/{modname}-front.coffee"
                       )
    try:
        modules = reload(modules)
        print("Installed:", libvis_mods.installed())

        # 3.
        v = libvis.Vis(ws_port=7700, vis_port=7000, debug=True)
        try:
            m = modules.TestMod(foo='bar')
            assert m.serial()

            v.vars.test = m

            # 4.
            browser.get('http://localhost:7000')

            widget = add_widget(browser, 'test')
            # Wait for libvis to answer. 
            # This is probably not the best way, since loading time may vary 
            # for complex visualisations or big data. 
            # May cause false negatives
            time.sleep(0.1)
            test_root = widget.find_element_by_xpath(
                f".//*[@class=\"{modname}-presenter\"]")
            assert test_root

        finally:
            v.stop()

    finally:
        libvis_mods.uninstall(modname)

    browser.quit()


def add_widget(browser, name):
    add_button = browser.find_element_by_class_name('add-widget')
    add_button.click()
    widget = browser.find_element_by_xpath(
        '(//*[@id="root"]/div/div[2]/div/div)[last()]'
    )
    varname_input = widget.find_element_by_xpath('.//input')
    varname_input.clear()
    varname_input.send_keys(name)
    return widget

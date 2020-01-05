from importlib import reload
from selenium import webdriver
import time

import webvis_mods
import webvis


def test_init_instal(tmp_path):
    import webvis.modules.installed as modules
    """
    1. Initialize a module from template
    2. Itstall the module
    3. Start the WebVis
    4. Test front with selenium
    """

    # 1.
    target_dir = tmp_path/'tmp_mods'
    target_dir.mkdir()
    modname = 'TestMod'
    webvis_mods.init_file(modname, output_dir=target_dir)

    # 2.
    webvis_mods.install(modname,
                        target_dir/f"{modname}/{modname}_back.py",
                        target_dir/f"{modname}/{modname}-front.coffee"
                       )
    try:
        modules = reload(modules)

        # 3.
        v = webvis.Vis(ws_port=7700, vis_port=7000)
        m = modules.TestMod(foo='bar')
        assert m.serial()

        v.start()
        v.vars.test = m

        # 4.
        browser = webdriver.Firefox()
        browser.get('http://localhost:7000')

        widget = add_widget(browser, 'test')
        # Wait for webvis to answer. 
        # This is probably not the best way, since this time may vary 
        # for complex visualisations or big data. 
        # May cause false negatives
        time.sleep(.05)
        test_root = widget.find_element_by_xpath(
            f".//*[@class=\"{modname}-presenter\"]")
        assert test_root

    finally:
        webvis_mods.uninstall(modname)
        v.stop()


def add_widget(browser, name):
    add_button = browser.find_element_by_class_name('add-widget')
    add_button.click()
    widget = browser.find_element_by_xpath(
        '(//*[@id="root"]/div/div[2]/div/div)[last()]'
    )
    print(widget.get_attribute('class'))
    varname_input = widget.find_element_by_xpath('.//input')
    varname_input.clear()
    varname_input.send_keys(name)
    return widget

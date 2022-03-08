class Driver:
    def __init__(self, web_driver, driver_manager):
        self.driver_manager = driver_manager
        self.web_driver = web_driver

    def install_driver(self):
        driver_path = self.driver_manager().install()
        return driver_path

    def get_driver(self):
        driver = self.web_driver(self.install_driver())
        return driver


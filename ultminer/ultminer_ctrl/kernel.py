from abc import abstractmethod


class Kernel:
    def __init__(self):
        self.kernel_dir_name = "kernels"
        self.log_dir_name = "logs"

    @abstractmethod
    def get_log_path(self):
        """
        Check kernel is installed or not
        :return: Kernel is installed or not
        """
        pass

    @abstractmethod
    def install_check(self):
        """
        Check kernel is installed or not
        :return: Kernel is installed or not
        """
        pass

    @abstractmethod
    def install_kernel(self):
        """
        Download and install kernel
        :return:
        """
        pass

    @abstractmethod
    def get_command(self, pool_url, wallet_address, miner_name):
        """
        Return mining command
        :param pool_url:
        :param wallet_address:
        :param miner_name:
        :return: Mining command
        """
        pass

    @abstractmethod
    def get_drawable_properties(self):
        """
        Return unit, range (undefined range will be considered as unlimited) of drawable data dict (key is
        data name) to initialize GUI :return: Properties dict
        """

    @abstractmethod
    def get_new_drawable_data(self, new_line):
        """
        Return new drawable data dict from log line. Will be called everytime a new log line is caught
        :param new_line: New log line
        :return: Data dict
        """
        pass



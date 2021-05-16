import os
import shutil
from time import localtime, strftime

import requests
from platform import system
from zipfile import ZipFile
import tarfile
from ultminer.ultminer_ctrl.kernel import Kernel
from re import findall


class NBKernel(Kernel):
    def __init__(self):
        super().__init__()

        self.kernel_name = "nbminer"

        os_type = system()
        if os_type == "Linux":
            self.exec = self.kernel_name
            self.suffix = ".tgz"
        elif os_type == "Windows":
            self.exec = self.kernel_name + ".exe"
            self.suffix = ".zip"
        else:
            raise Exception("Unsupported platform")

        self.kernel_dir = self.kernel_dir_name + os.sep + self.kernel_name

        self.log_dir = self.log_dir_name + os.sep + self.kernel_name

        self.log_filename = "log_" + strftime("%Y.%m.%d-%H.%M.%S", localtime()) + ".txt"

        self.data_name = [
            "ID",
            "Device",
            "Hashrate",
            "Accept",
            "Reject",
            "Inv",
            "Powr",
            "Temp",
            "Fan",
            "CClk",
            "GMClk",
            "MUtl",
            "Eff/Watt",
        ]

        self.sample_next_line = False

        if not os.path.exists(self.kernel_dir):
            os.makedirs(self.kernel_dir)

        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def get_log_path(self):
        return self.log_dir + os.sep + self.log_filename

    def install_check(self):
        return os.path.exists(self.kernel_dir + os.sep + self.exec)

    def install_kernel(self):
        dl_url = self.fetch_dl_url_from_release_api("https://api.github.com/repos/NebuTech/NBMiner/releases/latest")
        save_path = self.fetch_kernel_from_dl_url(dl_url, self.kernel_dir)
        self.extract_kernel(save_path)

    def get_command(self, pool_url, wallet_address, miner_name):
        return "{path}{separator}{exec} -a {algorithm} -o {pool} -u {wallet}.{miner} --log-file {log_filename}".format(
            separator=os.sep,
            exec=self.exec,
            path=self.kernel_dir,
            algorithm="ethash",
            pool=pool_url,
            wallet=wallet_address,
            miner=miner_name,
            log_filename=self.get_log_path()
        )

    def fetch_dl_url_from_release_api(self, url):
        response = requests.get(url).json()

        for asset in response["assets"]:
            if asset["name"].endswith(self.suffix):
                return asset["browser_download_url"]

    def fetch_kernel_from_dl_url(self, url, save_dir):
        """
        Fetch and save kernel from download url to path
        :param url: Kernel Download url
        :param save_dir: Kernel save path
        :return: Path to saved file
        """
        save_path = save_dir + os.sep + "tmp" + self.suffix
        response = requests.get(url)

        with open(save_dir + os.sep + "tmp" + self.suffix, "wb") as kernel_file:
            kernel_file.write(response.content)

        return save_path

    def extract_kernel(self, save_path):
        """
        Extract kernel from compressed file
        :param save_path: Path to saved file
        :return:
        """
        # TAR and ZIP file names always use "/"
        if self.suffix == ".tgz":
            sub_dir = "NBMiner_Linux"
            tar_obj = tarfile.open(save_path)
            tar_obj.extract(sub_dir + "/" + self.exec, self.kernel_dir)
            tar_obj.close()
        elif self.suffix == ".zip":
            sub_dir = "NBMiner_Win"
            zip_obj = ZipFile(save_path)
            zip_obj.extract(sub_dir + "/" + self.exec, self.kernel_dir)
            zip_obj.close()
        else:
            raise Exception("Unsupported file type: {}", self.suffix)

        shutil.move(self.kernel_dir + os.sep + sub_dir + os.sep + self.exec, self.kernel_dir + os.sep + self.exec)
        os.rmdir(self.kernel_dir + os.sep + sub_dir)
        os.remove(save_path)

    def get_drawable_properties(self):
        return {
            "哈希率": {
                "unit": "MH/s"
            },
            "接受率": {
                "unit": "%%",
                "range": (0, 100)
            },
            "拒绝率": {
                "unit": "%%",
                "range": (0, 100)
            },
            "无效率": {
                "unit": "%%",
                "range": (0, 100)
            },
            "功耗": {
                "unit": "W"
            },
            "温度": {
                "unit": "C"
            },
            "风扇利用率": {
                "unit": "%%",
                "range": (0, 100)
            },
            "核心频率": {
                "unit": "MHz"
            },
            "显存频率": {
                "unit": "MHz"
            },
            "显存利用率": {
                "unit": "%%",
                "range": (0, 100)
            },
            "效率": {
                "unit": "KH/J"
            },
        }

    def get_new_drawable_data(self, new_line):
        if len(new_line.strip()) == 0:
            return None
        elif "|ID|Device|Hashrate|Accept|Reject|Inv|Powr|Temp|Fan|CClk|GMClk|MUtl|Eff/Watt|" in new_line:
            self.sample_next_line = True
            return None
        elif self.sample_next_line:
            self.sample_next_line = False
            raw_list = findall(r"\|[ ]*([a-zA-Z0-9.]+)", new_line)
            data_dict = dict(zip(self.data_name, raw_list))
            total_shares = float(data_dict["Accept"]) + float(data_dict["Reject"]) + float(data_dict["Inv"])
            if total_shares == 0:
                total_shares = 1
            drawable_dict = {
                "哈希率": float(data_dict["Hashrate"]),
                "接受率": float(data_dict["Accept"]) * 100 / total_shares,
                "拒绝率": float(data_dict["Reject"]) * 100 / total_shares,
                "无效率": float(data_dict["Inv"]) * 100 / total_shares,
                "功耗": float(data_dict["Powr"]),
                "温度": float(data_dict["Temp"]),
                "风扇利用率": float(data_dict["Fan"]),
                "核心频率": float(data_dict["CClk"]),
                "显存频率": float(data_dict["GMClk"]),
                "显存利用率": float(data_dict["MUtl"]),
                "效率": float(data_dict["Eff/Watt"]),
            }
            return drawable_dict
